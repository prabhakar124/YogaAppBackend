# FastAPI Authentication Backend with OTP

Complete authentication system with email verification and password reset using OTP.

## ✨ Features

- ✅ User registration with email verification (OTP)
- ✅ Secure login with JWT tokens
- ✅ Password reset with OTP
- ✅ HTTP-only cookie sessions
- ✅ In-memory OTP storage (no Redis needed)
- ✅ Brute-force protection
- ✅ Rate limiting
- ✅ Security headers
- ✅ MySQL database

## 📁 Project Structure

```
backend/
├── main.py                      # App entry point
├── database.py                  # MySQL connection
├── models.py                    # User model
├── schemas.py                   # Validation schemas
├── requirements.txt             # Dependencies
├── .env.example                 # Environment template
├── .gitignore
├── README.md
├── AUTH_FLOW.md                 # Detailed auth guide
├── middleware/
│   └── auth.py                  # JWT middleware
├── routers/
│   └── auth_integrated.py       # Auth endpoints
└── services/
    └── otp_memory_service.py    # OTP service
```

## 🚀 Quick Start

### 1. Create Virtual Environment

```bash
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (macOS/Linux)
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Setup MySQL Database

```sql
CREATE DATABASE authdb CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 4. Configure Environment

```bash
cp .env.example .env
# Edit .env with your MySQL credentials
```

### 5. Run the Server

```bash
python main.py
```

Server runs at: http://localhost:4000
- API Docs: http://localhost:4000/docs
- Alternative Docs: http://localhost:4000/redoc

## 📚 API Endpoints

### Registration Flow

**1. Register (sends OTP)**
```bash
POST /api/auth/register
Body: { "name": "John", "email": "john@example.com", "password": "pass123" }
```

**2. Verify Email**
```bash
POST /api/auth/verify-email
Body: { "email": "john@example.com", "otp": "123456" }
```

**3. Login**
```bash
POST /api/auth/login
Body: { "email": "john@example.com", "password": "pass123" }
```

### Password Reset Flow

**1. Request Reset**
```bash
POST /api/auth/forgot-password
Body: { "email": "john@example.com" }
```

**2. Reset Password**
```bash
POST /api/auth/reset-password
Body: { "email": "john@example.com", "otp": "123456", "new_password": "newpass123" }
```

### Other Endpoints

- `POST /api/auth/resend-verification-otp` - Resend OTP
- `POST /api/auth/logout` - Logout
- `GET /api/auth/me` - Get current user

## 🔒 Security Features

- Passwords hashed with bcrypt
- JWT tokens in HTTP-only cookies
- Rate limiting on all endpoints
- OTP expiration (5 min verification, 10 min reset)
- Max 5 failed OTP attempts
- CORS protection
- Security headers

## 🧪 Testing

Check console for OTP codes during development.

In production, integrate email service:
- SendGrid
- AWS SES
- Mailgun
- Twilio (SMS)

## 📖 Detailed Documentation

See `AUTH_FLOW.md` for:
- Complete API examples
- React/Frontend integration
- Error handling
- Email service integration

## 🛠️ Tech Stack

- FastAPI - Web framework
- SQLAlchemy - ORM
- MySQL - Database
- PyJWT - JWT tokens
- Bcrypt - Password hashing
- Pydantic - Validation

## 📝 License

MIT License - Free to use!