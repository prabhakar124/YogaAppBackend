from fastapi import Depends, HTTPException, status, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt
from datetime import datetime, timedelta
import os
from typing import Optional

security = HTTPBearer(auto_error=False)

JWT_SECRET = os.getenv("JWT_SECRET", "your-secret-key")
JWT_ALGORITHM = "HS256"
JWT_EXPIRES_IN = os.getenv("JWT_EXPIRES_IN", "7d")

def parse_expiry(expiry_str: str) -> timedelta:
    """Parse expiry string like '7d', '24h', '30m' to timedelta"""
    if expiry_str.endswith('d'):
        return timedelta(days=int(expiry_str[:-1]))
    elif expiry_str.endswith('h'):
        return timedelta(hours=int(expiry_str[:-1]))
    elif expiry_str.endswith('m'):
        return timedelta(minutes=int(expiry_str[:-1]))
    else:
        return timedelta(days=7)  # default

def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + parse_expiry(JWT_EXPIRES_IN)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return encoded_jwt

def get_token_from_request(request: Request, credentials: Optional[HTTPAuthorizationCredentials] = Depends(security)) -> str:
    """Extract token from cookie or Authorization header"""
    # Check cookie first
    token = request.cookies.get("token")
    
    # If not in cookie, check Authorization header
    if not token and credentials:
        token = credentials.credentials
    
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized"
        )
    
    return token

def verify_token(token: str = Depends(get_token_from_request)) -> dict:
    """Verify JWT token and return payload"""
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )

def get_current_user(payload: dict = Depends(verify_token)) -> dict:
    """Get current user from token payload"""
    user_id = payload.get("id")
    email = payload.get("email")
    
    if not user_id or not email:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )
    
    return {"id": user_id, "email": email}