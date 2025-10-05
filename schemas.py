from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional
from datetime import datetime

class UserRegister(BaseModel):
    name: Optional[str] = None
    email: EmailStr
    password: str
    
    @field_validator('password')
    @classmethod
    def validate_password(cls, v):
        if len(v) < 6:
            raise ValueError('Password must be at least 6 characters long')
        if len(v) > 72:
            raise ValueError('Password must be less than 72 characters')
        return v

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
    
    @field_validator('new_password')
    @classmethod
    def validate_new_password(cls, v):
        if len(v) < 6:
            raise ValueError('Password must be at least 6 characters long')
        if len(v) > 72:
            raise ValueError('Password must be less than 72 characters')
        return v

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