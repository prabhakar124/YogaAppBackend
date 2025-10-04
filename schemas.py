from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserRegister(BaseModel):
    name: Optional[str] = None
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class VerifyEmailRequest(BaseModel):
    email: EmailStr
    otp: str

class ForgotPasswordRequest(BaseModel):
    email: EmailStr

class ResetPasswordRequest(BaseModel):
    email: EmailStr
    otp: str
    new_password: str

class UserResponse(BaseModel):
    id: int
    name: Optional[str]
    email: str
    role: Optional[str] = "student"
    is_verified: Optional[bool] = False
    created_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True

class UserOut(BaseModel):
    user: UserResponse

class MessageResponse(BaseModel):
    message: str