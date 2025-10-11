from fastapi import APIRouter, Depends, HTTPException, status, Response, Request
from sqlalchemy.orm import Session
import bcrypt  # Using bcrypt directly instead of passlib
from slowapi import Limiter
from slowapi.util import get_remote_address

from database import get_db
from models.user import User
from schemas import (
    UserRegister, UserLogin, UserOut, MessageResponse, UserResponse,
    VerifyEmailRequest, ForgotPasswordRequest, ResetPasswordRequest
)
from middleware.auth import create_access_token, get_current_user
from services.otp_memory_service import otp_service  # Using in-memory (no Redis needed)
from services.email_service import email_service
# Or use: from services.otp_service import otp_service  # For Redis version
import os

router = APIRouter()
limiter = Limiter(key_func=get_remote_address)

# Password hashing with bcrypt directly
def hash_password(password: str) -> str:
    """Hash password using bcrypt"""
    # Ensure password is bytes and truncate if needed
    password_bytes = password.encode('utf-8')
    if len(password_bytes) > 72:
        password_bytes = password_bytes[:72]
    
    # Generate salt and hash
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)
    return hashed.decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify password using bcrypt"""
    # Ensure inputs are bytes
    password_bytes = plain_password.encode('utf-8')
    if len(password_bytes) > 72:
        password_bytes = password_bytes[:72]
    
    hashed_bytes = hashed_password.encode('utf-8')
    
    return bcrypt.checkpw(password_bytes, hashed_bytes)

def set_token_cookie(response: Response, token: str):
    """Set token in httpOnly cookie"""
    is_production = os.getenv("NODE_ENV") == "production"
    response.set_cookie(
        key="token",
        value=token,
        httponly=True,
        secure=is_production,
        samesite="strict",
        max_age=7 * 24 * 60 * 60  # 7 days in seconds
    )

@router.post("/register", status_code=status.HTTP_201_CREATED)
@limiter.limit("10/minute")
async def register(
    request: Request,
    user_data: UserRegister,
    db: Session = Depends(get_db)
):
    """
    Register a new user and send OTP for email verification
    User account is created but not verified until OTP is confirmed
    """
    # Check if user already exists
    existing_user = db.query(User).filter(User.email == user_data.email.lower()).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already in use"
        )
    
    # Hash password
    hashed_password = hash_password(user_data.password)
    
    # Create new user (unverified)
    new_user = User(
        name=user_data.name,
        email=user_data.email.lower(),
        password=hashed_password,
        is_verified=False
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    # Generate and store OTP
    otp = otp_service.generate_otp(length=6, numeric_only=True)
    otp_service.store_otp(new_user.email, otp, expiry=300)  # 5 minutes
    
    # Send OTP via email
    email_sent = email_service.send_verification_otp(new_user.email, otp, new_user.name)
    
    if not email_sent:
        # Fallback: print to console if email fails
        print(f"[FALLBACK] OTP for {new_user.email}: {otp}")
    
    return {
        "message": "Registration successful. Please verify your email with the OTP sent.",
        "email": new_user.email,
        "user_id": new_user.id
    }

@router.post("/verify-email", response_model=UserOut)
@limiter.limit("10/minute")
async def verify_email(
    request: Request,
    response: Response,
    verify_data: VerifyEmailRequest,
    db: Session = Depends(get_db)
):
    """
    Verify email with OTP and complete registration
    Returns JWT token on successful verification
    """
    # Find user
    user = db.query(User).filter(User.email == verify_data.email.lower()).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    # Check if already verified
    if user.is_verified:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already verified"
        )
    
    # Verify OTP
    is_valid = otp_service.verify_otp(verify_data.email.lower(), verify_data.otp, delete_on_verify=True)
    
    if not is_valid:
        # Track failed attempts
        attempts = otp_service.increment_attempt(f"verify:{verify_data.email}", max_attempts=5)
        if attempts >= 5:
            raise HTTPException(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                detail="Too many failed attempts. Please request a new OTP."
            )
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid or expired OTP"
        )
    
    # Mark user as verified
    user.is_verified = True
    db.commit()
    db.refresh(user)
    
    # Reset verification attempts
    otp_service.reset_attempts(f"verify:{verify_data.email}")
    
    # Send welcome email
    email_service.send_welcome_email(user.email, user.name or "User")
    
    # Generate token
    token = create_access_token({"id": user.id, "email": user.email})
    
    # Set cookie
    set_token_cookie(response, token)
    
    return {"user": UserResponse.from_orm(user)}

@router.post("/resend-verification-otp")
@limiter.limit("3/minute")
async def resend_verification_otp(
    request: Request,
    email_request: ForgotPasswordRequest,
    db: Session = Depends(get_db)
):
    """Resend verification OTP"""
    user = db.query(User).filter(User.email == email_request.email.lower()).first()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    if user.is_verified:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already verified"
        )
    
    # Generate new OTP
    otp = otp_service.generate_otp(length=6, numeric_only=True)
    otp_service.store_otp(user.email, otp, expiry=300)
    
    # Send OTP via email
    email_sent = email_service.send_verification_otp(user.email, otp, user.name)
    
    if not email_sent:
        print(f"[FALLBACK] New OTP for {user.email}: {otp}")
    
    return {"message": "Verification OTP resent successfully"}

@router.post("/login", response_model=UserOut)
@limiter.limit("10/minute")
async def login(
    request: Request,
    response: Response,
    credentials: UserLogin,
    db: Session = Depends(get_db)
):
    """
    Login user (email must be verified)
    """
    # Find user
    user = db.query(User).filter(User.email == credentials.email.lower()).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid credentials"
        )
    
    # Verify password
    if not verify_password(credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid credentials"
        )
    
    # Check if email is verified
    if not user.is_verified:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Please verify your email before logging in"
        )
    
    # Generate token
    token = create_access_token({"id": user.id, "email": user.email})
    
    # Set cookie
    set_token_cookie(response, token)
    
    return {"user": UserResponse.from_orm(user)}

@router.post("/forgot-password")
@limiter.limit("3/minute")
async def forgot_password(
    request: Request,
    forgot_request: ForgotPasswordRequest,
    db: Session = Depends(get_db)
):
    """
    Request password reset OTP
    """
    # Find user
    user = db.query(User).filter(User.email == forgot_request.email.lower()).first()
    
    # Don't reveal if user exists (security best practice)
    # Always return success message
    
    if user:
        # Generate OTP
        otp = otp_service.generate_otp(length=6, numeric_only=True)
        otp_service.store_otp(f"reset:{user.email}", otp, expiry=600)  # 10 minutes for password reset
        
        # Send OTP via email
        email_sent = email_service.send_password_reset_otp(user.email, otp, user.name)
        
        if not email_sent:
            print(f"[FALLBACK] Password reset OTP for {user.email}: {otp}")
    
    return {"message": "If the email exists, a password reset OTP has been sent"}

@router.post("/reset-password")
@limiter.limit("5/minute")
async def reset_password(
    request: Request,
    reset_data: ResetPasswordRequest,
    db: Session = Depends(get_db)
):
    """
    Reset password using OTP
    """
    # Find user
    user = db.query(User).filter(User.email == reset_data.email.lower()).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    # Verify OTP (using reset: prefix)
    is_valid = otp_service.verify_otp(
        f"reset:{reset_data.email.lower()}", 
        reset_data.otp, 
        delete_on_verify=True
    )
    
    if not is_valid:
        # Track failed attempts
        attempts = otp_service.increment_attempt(f"reset_verify:{reset_data.email}", max_attempts=5)
        if attempts >= 5:
            raise HTTPException(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                detail="Too many failed attempts. Please request a new OTP."
            )
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid or expired OTP"
        )
    
    # Hash new password
    hashed_password = hash_password(reset_data.new_password)
    
    # Update password
    user.password = hashed_password
    db.commit()
    
    # Reset attempts
    otp_service.reset_attempts(f"reset_verify:{reset_data.email}")
    
    return {"message": "Password reset successfully"}

@router.post("/logout", response_model=MessageResponse)
async def logout(response: Response):
    """Logout user by clearing cookie"""
    response.delete_cookie(key="token")
    return {"message": "Logged out"}

@router.get("/me", response_model=UserOut)
@limiter.limit("100/minute")
async def get_me(
    request: Request,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get current user information"""
    user = db.query(User).filter(User.id == current_user["id"]).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    return {"user": UserResponse.from_orm(user)}