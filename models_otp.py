from sqlalchemy import Column, Integer, String, DateTime, Index
from datetime import datetime, timedelta
from database import Base

class OTP(Base):
    __tablename__ = "otps"
    
    id = Column(Integer, primary_key=True, index=True)
    identifier = Column(String(255), unique=True, index=True, nullable=False)  # email or phone
    otp = Column(String(10), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    expires_at = Column(DateTime, nullable=False)
    attempts = Column(Integer, default=0)
    
    # Add index for faster cleanup queries
    __table_args__ = (
        Index('idx_expires_at', 'expires_at'),
    )
    
    @staticmethod
    def create_otp(identifier: str, otp: str, expiry_seconds: int = 300):
        """Helper to create OTP with expiration"""
        return OTP(
            identifier=identifier,
            otp=otp,
            expires_at=datetime.utcnow() + timedelta(seconds=expiry_seconds)
        )
    
    def is_expired(self) -> bool:
        """Check if OTP is expired"""
        return datetime.utcnow() > self.expires_at

class OTPAttempt(Base):
    __tablename__ = "otp_attempts"
    
    id = Column(Integer, primary_key=True, index=True)
    identifier = Column(String(255), index=True, nullable=False)
    attempts = Column(Integer, default=1)
    created_at = Column(DateTime, default=datetime.utcnow)
    expires_at = Column(DateTime, nullable=False)
    
    __table_args__ = (
        Index('idx_identifier_expires', 'identifier', 'expires_at'),
    )