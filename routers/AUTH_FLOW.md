# Authentication Flow Documentation

## 🔐 Complete Authentication Flows

### 1. Registration Flow (Email Verification Required)

```
User Registration → OTP Sent → Verify OTP → Account Activated → Login
```

**Step 1: Register**
```bash
curl -X POST http://localhost:4000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "email": "john@example.com",
    "password": "password123"
  }'
```

Response:
```json
{
  "message": "Registration successful. Please verify your email with the OTP sent.",
  "email": "john@example.com",
  "user_id": 1
}
```

**Note:** Check console for OTP (in development). In production, OTP will be sent via email.

**Step 2: Verify Email**
```bash
curl -X POST http://localhost:4000/api/auth/verify-email \
  -H "Content-Type: application/json" \
  -d '{
    "email": "john@example.com",
    "otp": "123456"
  }' \
  -c cookies.txt
```

Response:
```json
{
  "user": {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com",
    "role": "student",
    "is_verified": true
  }
}
```

**Step 3: Login (after verification)**
```bash
curl -X POST http://localhost:4000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "john@example.com",
    "password": "password123"
  }' \
  -c cookies.txt
```

---

### 2. Password Reset Flow (OTP-based)

```
Forgot Password → OTP Sent → Verify OTP → New Password Set
```

**Step 1: Request Password Reset**
```bash
curl -X POST http://localhost:4000/api/auth/forgot-password \
  -H "Content-Type: application/json" \
  -d '{
    "email": "john@example.com"
  }'
```

Response:
```json
{
  "message": "If the email exists, a password reset OTP has been sent"
}
```

**Note:** Check console for reset OTP (in development). OTP expires in 10 minutes.

**Step 2: Reset Password with OTP**
```bash
curl -X POST http://localhost:4000/api/auth/reset-password \
  -H "Content-Type: application/json" \
  -d '{
    "email": "john@example.com",
    "otp": "123456",
    "new_password": "newpassword123"
  }'
```

Response:
```json
{
  "message": "Password reset successfully"
}
```

---

### 3. Resend Verification OTP

If user didn't receive OTP or it expired:

```bash
curl -X POST http://localhost:4000/api/auth/resend-verification-otp \
  -H "Content-Type: application/json" \
  -d '{
    "email": "john@example.com"
  }'
```

---

## 🔒 Security Features

### OTP Security
- **Expiration:** Verification OTPs expire in 5 minutes, password reset OTPs in 10 minutes
- **Brute-force Protection:** Max 5 failed attempts per hour
- **Rate Limiting:** 
  - Register: 10 requests/minute
  - Verify: 10 requests/minute
  - Resend: 3 requests/minute
  - Forgot Password: 3 requests/minute
  - Reset Password: 5 requests/minute

### Password Security
- Hashed with bcrypt (industry standard)
- Minimum requirements can be added in validation

### Token Security
- JWT tokens stored in HTTP-only cookies
- Secure flag enabled in production
- SameSite: strict
- 7-day expiration

---

## 🚫 Error Handling

### Common Errors

**Unverified User Trying to Login:**
```json
{
  "detail": "Please verify your email before logging in"
}
```

**Invalid/Expired OTP:**
```json
{
  "detail": "Invalid or expired OTP"
}
```

**Too Many Failed Attempts:**
```json
{
  "detail": "Too many failed attempts. Please request a new OTP."
}
```

**Email Already Registered:**
```json
{
  "detail": "Email already in use"
}
```

**Invalid Credentials:**
```json
{
  "detail": "Invalid credentials"
}
```

---

## 🎯 User States

| State | Can Login? | Action Required |
|-------|-----------|-----------------|
| Just Registered | ❌ No | Verify email with OTP |
| Email Verified | ✅ Yes | Can login normally |
| Forgot Password | ❌ No | Reset password with OTP, then login |

---

## 💻 Frontend Integration Example

```javascript
// 1. Register User
const register = async (name, email, password) => {
  const response = await fetch('http://localhost:4000/api/auth/register', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ name, email, password })
  });
  return await response.json();
};

// 2. Verify Email
const verifyEmail = async (email, otp) => {
  const response = await fetch('http://localhost:4000/api/auth/verify-email', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    credentials: 'include', // Important for cookies!
    body: JSON.stringify({ email, otp })
  });
  return await response.json();
};

// 3. Login
const login = async (email, password) => {
  const response = await fetch('http://localhost:4000/api/auth/login', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    credentials: 'include', // Important for cookies!
    body: JSON.stringify({ email, password })
  });
  return await response.json();
};

// 4. Get Current User
const getCurrentUser = async () => {
  const response = await fetch('http://localhost:4000/api/auth/me', {
    credentials: 'include' // Important for cookies!
  });
  return await response.json();
};

// 5. Forgot Password
const forgotPassword = async (email) => {
  const response = await fetch('http://localhost:4000/api/auth/forgot-password', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email })
  });
  return await response.json();
};

// 6. Reset Password
const resetPassword = async (email, otp, newPassword) => {
  const response = await fetch('http://localhost:4000/api/auth/reset-password', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ 
      email, 
      otp, 
      new_password: newPassword 
    })
  });
  return await response.json();
};

// 7. Resend Verification OTP
const resendVerificationOTP = async (email) => {
  const response = await fetch('http://localhost:4000/api/auth/resend-verification-otp', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email })
  });
  return await response.json();
};

// 8. Logout
const logout = async () => {
  const response = await fetch('http://localhost:4000/api/auth/logout', {
    method: 'POST',
    credentials: 'include'
  });
  return await response.json();
};
```

---

## 📱 Complete React Example

```jsx
import { useState } from 'react';

function RegistrationFlow() {
  const [step, setStep] = useState('register'); // 'register' | 'verify'
  const [email, setEmail] = useState('');
  const [otp, setOtp] = useState('');
  const [message, setMessage] = useState('');

  const handleRegister = async (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);
    
    try {
      const response = await fetch('http://localhost:4000/api/auth/register', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          name: formData.get('name'),
          email: formData.get('email'),
          password: formData.get('password')
        })
      });
      
      const data = await response.json();
      
      if (response.ok) {
        setEmail(data.email);
        setStep('verify');
        setMessage('OTP sent to your email. Please check and verify.');
      } else {
        setMessage(data.detail || 'Registration failed');
      }
    } catch (error) {
      setMessage('Network error occurred');
    }
  };

  const handleVerify = async (e) => {
    e.preventDefault();
    
    try {
      const response = await fetch('http://localhost:4000/api/auth/verify-email', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        credentials: 'include',
        body: JSON.stringify({ email, otp })
      });
      
      const data = await response.json();
      
      if (response.ok) {
        setMessage('Email verified! You can now login.');
        // Redirect to dashboard or home
        window.location.href = '/dashboard';
      } else {
        setMessage(data.detail || 'Verification failed');
      }
    } catch (error) {
      setMessage('Network error occurred');
    }
  };

  const handleResendOTP = async () => {
    try {
      const response = await fetch('http://localhost:4000/api/auth/resend-verification-otp', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email })
      });
      
      if (response.ok) {
        setMessage('New OTP sent to your email');
      }
    } catch (error) {
      setMessage('Failed to resend OTP');
    }
  };

  if (step === 'register') {
    return (
      <div>
        <h2>Register</h2>
        <form onSubmit={handleRegister}>
          <input type="text" name="name" placeholder="Name" required />
          <input type="email" name="email" placeholder="Email" required />
          <input type="password" name="password" placeholder="Password" required />
          <button type="submit">Register</button>
        </form>
        {message && <p>{message}</p>}
      </div>
    );
  }

  if (step === 'verify') {
    return (
      <div>
        <h2>Verify Email</h2>
        <p>Enter the OTP sent to {email}</p>
        <form onSubmit={handleVerify}>
          <input 
            type="text" 
            value={otp} 
            onChange={(e) => setOtp(e.target.value)}
            placeholder="Enter OTP" 
            maxLength="6"
            required 
          />
          <button type="submit">Verify</button>
        </form>
        <button onClick={handleResendOTP}>Resend OTP</button>
        {message && <p>{message}</p>}
      </div>
    );
  }
}

function PasswordResetFlow() {
  const [step, setStep] = useState('request'); // 'request' | 'reset'
  const [email, setEmail] = useState('');
  const [otp, setOtp] = useState('');
  const [newPassword, setNewPassword] = useState('');
  const [message, setMessage] = useState('');

  const handleForgotPassword = async (e) => {
    e.preventDefault();
    
    try {
      const response = await fetch('http://localhost:4000/api/auth/forgot-password', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email })
      });
      
      if (response.ok) {
        setStep('reset');
        setMessage('OTP sent to your email');
      }
    } catch (error) {
      setMessage('Network error occurred');
    }
  };

  const handleResetPassword = async (e) => {
    e.preventDefault();
    
    try {
      const response = await fetch('http://localhost:4000/api/auth/reset-password', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ 
          email, 
          otp, 
          new_password: newPassword 
        })
      });
      
      const data = await response.json();
      
      if (response.ok) {
        setMessage('Password reset successful! You can now login.');
        // Redirect to login
        setTimeout(() => window.location.href = '/login', 2000);
      } else {
        setMessage(data.detail || 'Reset failed');
      }
    } catch (error) {
      setMessage('Network error occurred');
    }
  };

  if (step === 'request') {
    return (
      <div>
        <h2>Forgot Password</h2>
        <form onSubmit={handleForgotPassword}>
          <input 
            type="email" 
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="Enter your email" 
            required 
          />
          <button type="submit">Send OTP</button>
        </form>
        {message && <p>{message}</p>}
      </div>
    );
  }

  if (step === 'reset') {
    return (
      <div>
        <h2>Reset Password</h2>
        <p>Enter the OTP sent to {email}</p>
        <form onSubmit={handleResetPassword}>
          <input 
            type="text" 
            value={otp}
            onChange={(e) => setOtp(e.target.value)}
            placeholder="Enter OTP" 
            maxLength="6"
            required 
          />
          <input 
            type="password" 
            value={newPassword}
            onChange={(e) => setNewPassword(e.target.value)}
            placeholder="New Password" 
            required 
          />
          <button type="submit">Reset Password</button>
        </form>
        {message && <p>{message}</p>}
      </div>
    );
  }
}

export { RegistrationFlow, PasswordResetFlow };
```

---

## 🧪 Testing Checklist

### Registration Flow
- [ ] Register with valid email
- [ ] Try to register with existing email (should fail)
- [ ] Verify email with correct OTP
- [ ] Try to verify with wrong OTP (should fail)
- [ ] Try to verify with expired OTP (wait 5+ minutes)
- [ ] Try to login before verification (should fail)
- [ ] Resend OTP and verify
- [ ] Login after successful verification

### Password Reset Flow
- [ ] Request password reset for existing email
- [ ] Request password reset for non-existing email (should still show success)
- [ ] Reset password with correct OTP
- [ ] Try to reset with wrong OTP (should fail)
- [ ] Try to reset with expired OTP (wait 10+ minutes)
- [ ] Login with new password

### Security Tests
- [ ] Try to verify OTP more than 5 times with wrong code (should block)
- [ ] Try to generate OTP more than rate limit (should block)
- [ ] Check that passwords are hashed in database
- [ ] Verify JWT token is in HTTP-only cookie
- [ ] Test logout clears the cookie

---

## 🔧 Configuration Options

### OTP Settings (in service file)

```python
# In services/otp_memory_service.py or services/otp_service.py

# Change OTP expiry time (default 300 seconds = 5 minutes)
otp_service = InMemoryOTPService(expiry_seconds=600)  # 10 minutes

# Change OTP length (default 6 digits)
otp = otp_service.generate_otp(length=8, numeric_only=True)

# Change max attempts (default 5)
attempts = otp_service.increment_attempt(identifier, max_attempts=3)

# Change attempt window (default 3600 seconds = 1 hour)
attempts = otp_service.increment_attempt(identifier, window_seconds=1800)  # 30 minutes
```

### Rate Limiting (in router file)

```python
# In routers/auth_integrated.py

@router.post("/register")
@limiter.limit("10/minute")  # Change to "5/minute" or "20/minute"
async def register(...):
    ...
```

---

## 📧 Email Integration (Production)

To send real emails in production, integrate with an email service:

### Example with SendGrid

```python
# Install: pip install sendgrid

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_otp_email(to_email: str, otp: str, purpose: str = "verification"):
    message = Mail(
        from_email='noreply@yourapp.com',
        to_emails=to_email,
        subject=f'Your {purpose} OTP',
        html_content=f'''
            <h2>Your OTP Code</h2>
            <p>Your OTP code is: <strong>{otp}</strong></p>
            <p>This code will expire in 5 minutes.</p>
        '''
    )
    
    try:
        sg = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))
        response = sg.send(message)
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False
```

Then replace the print statements in the router:

```python
# Instead of:
print(f"[DEVELOPMENT] OTP for {user.email}: {otp}")

# Use:
send_otp_email(user.email, otp, "verification")
```

---

## 🎉 Summary

Your authentication system now includes:

✅ **Email verification with OTP** - Users must verify email before login  
✅ **Password reset with OTP** - Secure password recovery  
✅ **In-memory OTP storage** - No Redis required (but can be added)  
✅ **Brute-force protection** - Rate limiting and attempt tracking  
✅ **Secure tokens** - HTTP-only cookies with JWT  
✅ **Complete error handling** - Clear error messages  
✅ **Production-ready** - Just add email service integration  

Ready to deploy! 🚀