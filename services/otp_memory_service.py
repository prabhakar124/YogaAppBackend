import random
import string
from datetime import datetime, timedelta
from typing import Optional, Dict
import threading

class InMemoryOTPService:
    """
    OTP service using in-memory storage (no Redis required)
    Good for: Single-server applications, development, small projects
    Limitations: Data lost on server restart, doesn't work with multiple servers
    """
    
    def __init__(self, expiry_seconds: int = 300):
        self.expiry_seconds = expiry_seconds
        self._storage: Dict[str, dict] = {}
        self._attempts: Dict[str, dict] = {}
        self._lock = threading.Lock()
        
        # Start cleanup thread
        self._start_cleanup_thread()
    
    def _start_cleanup_thread(self):
        """Start a background thread to clean up expired OTPs"""
        def cleanup():
            import time
            while True:
                time.sleep(60)  # Run every minute
                self._cleanup_expired()
        
        thread = threading.Thread(target=cleanup, daemon=True)
        thread.start()
    
    def _cleanup_expired(self):
        """Remove expired OTPs from memory"""
        with self._lock:
            current_time = datetime.utcnow()
            expired_keys = [
                key for key, value in self._storage.items()
                if value['expires_at'] < current_time
            ]
            for key in expired_keys:
                del self._storage[key]
            
            # Cleanup expired attempts
            expired_attempt_keys = [
                key for key, value in self._attempts.items()
                if value['expires_at'] < current_time
            ]
            for key in expired_attempt_keys:
                del self._attempts[key]
    
    def generate_otp(self, length: int = 6, numeric_only: bool = True) -> str:
        """Generate a random OTP"""
        if numeric_only:
            return ''.join(random.choices(string.digits, k=length))
        else:
            return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
    
    def store_otp(self, identifier: str, otp: str, expiry: Optional[int] = None) -> bool:
        """Store OTP in memory with expiration"""
        try:
            with self._lock:
                expiry_time = expiry if expiry else self.expiry_seconds
                expires_at = datetime.utcnow() + timedelta(seconds=expiry_time)
                
                self._storage[identifier] = {
                    'otp': otp,
                    'created_at': datetime.utcnow(),
                    'expires_at': expires_at
                }
            return True
        except Exception as e:
            print(f"Error storing OTP: {e}")
            return False
    
    def verify_otp(self, identifier: str, otp: str, delete_on_verify: bool = True) -> bool:
        """Verify OTP against stored value"""
        try:
            with self._lock:
                stored_data = self._storage.get(identifier)
                
                if not stored_data:
                    return False
                
                # Check if expired
                if datetime.utcnow() > stored_data['expires_at']:
                    del self._storage[identifier]
                    return False
                
                # Verify OTP
                if stored_data['otp'] == otp:
                    if delete_on_verify:
                        del self._storage[identifier]
                    return True
                
                return False
        except Exception as e:
            print(f"Error verifying OTP: {e}")
            return False
    
    def get_remaining_ttl(self, identifier: str) -> int:
        """Get remaining time-to-live for an OTP in seconds"""
        try:
            with self._lock:
                stored_data = self._storage.get(identifier)
                
                if not stored_data:
                    return -1
                
                remaining = (stored_data['expires_at'] - datetime.utcnow()).total_seconds()
                return int(max(0, remaining))
        except Exception as e:
            print(f"Error getting TTL: {e}")
            return -1
    
    def delete_otp(self, identifier: str) -> bool:
        """Manually delete an OTP"""
        try:
            with self._lock:
                if identifier in self._storage:
                    del self._storage[identifier]
            return True
        except Exception as e:
            print(f"Error deleting OTP: {e}")
            return False
    
    def increment_attempt(self, identifier: str, max_attempts: int = 5, window_seconds: int = 3600) -> int:
        """Track failed OTP attempts"""
        try:
            with self._lock:
                current_time = datetime.utcnow()
                
                if identifier not in self._attempts:
                    self._attempts[identifier] = {
                        'count': 1,
                        'created_at': current_time,
                        'expires_at': current_time + timedelta(seconds=window_seconds)
                    }
                    return 1
                
                # Check if expired
                if current_time > self._attempts[identifier]['expires_at']:
                    self._attempts[identifier] = {
                        'count': 1,
                        'created_at': current_time,
                        'expires_at': current_time + timedelta(seconds=window_seconds)
                    }
                    return 1
                
                # Increment count
                self._attempts[identifier]['count'] += 1
                return self._attempts[identifier]['count']
        except Exception as e:
            print(f"Error incrementing attempts: {e}")
            return 0
    
    def get_attempts(self, identifier: str) -> int:
        """Get current attempt count"""
        try:
            with self._lock:
                attempt_data = self._attempts.get(identifier)
                
                if not attempt_data:
                    return 0
                
                # Check if expired
                if datetime.utcnow() > attempt_data['expires_at']:
                    del self._attempts[identifier]
                    return 0
                
                return attempt_data['count']
        except Exception as e:
            print(f"Error getting attempts: {e}")
            return 0
    
    def reset_attempts(self, identifier: str) -> bool:
        """Reset attempt counter"""
        try:
            with self._lock:
                if identifier in self._attempts:
                    del self._attempts[identifier]
            return True
        except Exception as e:
            print(f"Error resetting attempts: {e}")
            return False
    
    def get_stats(self) -> dict:
        """Get service statistics (useful for monitoring)"""
        with self._lock:
            return {
                'total_otps': len(self._storage),
                'total_attempts_tracked': len(self._attempts)
            }

# Create singleton instance
otp_service = InMemoryOTPService(expiry_seconds=300)