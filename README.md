# FastAPI Authentication API with MySQL

This is a complete conversion of your Express.js authentication backend to FastAPI with MySQL.

## Features

- **User registration with email verification (OTP)**
- **Password reset with OTP**
- Password hashing with bcrypt
- HTTP-only cookie-based sessions
- Token-based authentication (supports both cookies and Bearer tokens)
- **OTP generation and verification with in-memory caching (no Redis required!)**
- **Brute-force protection for OTP attempts**
- Rate limiting on all endpoints
- Security headers (Helmet equivalent)
- CORS support
- MySQL database with SQLAlchemy ORM

## Project Structure

```
.
├── main.py                 # Application entry point
├── database.py            # Database connection and session
├── redis_client.py        # Redis connection
├── models.py              # SQLAlchemy models
├── schemas.py             # Pydantic schemas for validation
├── schemas_otp.py         # OTP-related schemas
├── services/
│   └── otp_service.py    # OTP business logic
├── middleware/
│   └── auth.py           # JWT authentication middleware
├── routers/
│   ├── auth.py           # Authentication routes
│   └── otp.py            # OTP routes
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
└── README.md             # This file
```

## Installation

1. **Create and activate a virtual environment:**

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Set up MySQL database:**

Create a MySQL database:
```sql
CREATE DATABASE authdb CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

4. **Install and start Redis (OPTIONAL - Using in-memory storage by default):**

If you want to use Redis instead of in-memory storage, edit `routers/auth_integrated.py`:
```python
# Change from:
from services.otp_memory_service import otp_service
# To:
from services.otp_service import otp_service
```

**Windows:**
- Download Redis from: https://github.com/microsoftarchive/redis/releases
- Or use WSL: `sudo apt-get install redis-server && redis-server`
- Or use Docker: `docker run -d -p 6379:6379 redis`

**macOS:**
```bash
brew install redis
brew services start redis
```

**Linux:**
```bash
sudo apt-get install redis-server
sudo systemctl start redis
```

5. **Configure environment variables:**

Copy `.env.example` to `.env` and update the values:
```bash
cp .env.example .env
```

Edit `.env` with your configuration:
- Update `MYSQL_URI` with your MySQL credentials
- Update `REDIS_HOST`, `REDIS_PORT` if using custom Redis setup
- Change `JWT_SECRET` to a secure random string
- Set `CORS_ORIGIN` to your frontend URL
- Set `NODE_ENV` to `production` when deploying

6. **Run the application:**

```bash
python main.py
```

Or with uvicorn directly:
```bash
uvicorn main:app --reload --port 4000
```

The server will start at `http://localhost:4000`

## API Endpoints

### Authentication Routes (prefix: `/api/auth`)

#### Register (Step 1: Create Account)
- **POST** `/api/auth/register`
- Body: `{ "name": "John Doe", "email": "john@example.com", "password": "password123" }`
- Response: `{ "message": "Registration successful. Please verify your email with the OTP sent.", "email": "john@example.com", "user_id": 1 }`
- Note: User is created but not verified. OTP is sent (printed in console for development)

#### Verify Email (Step 2: Verify with OTP)
- **POST** `/api/auth/verify-email`
- Body: `{ "email": "john@example.com", "otp": "123456" }`
- Response: `{ "user": { "id": 1, "name": "John Doe", "email": "john@example.com", "is_verified": true } }`
- Sets JWT token cookie on success

#### Resend Verification OTP
- **POST** `/api/auth/resend-verification-otp`
- Body: `{ "email": "john@example.com" }`
- Response: `{ "message": "Verification OTP resent successfully" }`

#### Login
- **POST** `/api/auth/login`
- Body: `{ "email": "john@example.com", "password": "password123" }`
- Response: `{ "user": { "id": 1, "name": "John Doe", "email": "john@example.com", "is_verified": true } }`
- Note: Only verified users can login

#### Forgot Password (Step 1: Request Reset)
- **POST** `/api/auth/forgot-password`
- Body: `{ "email": "john@example.com" }`
- Response: `{ "message": "If the email exists, a password reset OTP has been sent" }`

#### Reset Password (Step 2: Reset with OTP)
- **POST** `/api/auth/reset-password`
- Body: `{ "email": "john@example.com", "otp": "123456", "new_password": "newpassword123" }`
- Response: `{ "message": "Password reset successfully" }`

#### Logout
- **POST** `/api/auth/logout`
- Response: `{ "message": "Logged out" }`

#### Get Current User
- **GET** `/api/auth/me`
- Headers: `Authorization: Bearer <token>` (or use cookie)
- Response: `{ "user": { "id": 1, "name": "John Doe", "email": "john@example.com", "is_verified": true } }`

### OTP Routes (prefix: `/api/otp`)

#### Generate OTP
- **POST** `/api/otp/generate`
- Body: `{ "email": "john@example.com" }`
- Response: `{ "message": "OTP sent successfully", "expires_in": 300 }`
- Note: OTP is printed in console for development (remove in production)

#### Verify OTP
- **POST** `/api/otp/verify`
- Body: `{ "email": "john@example.com", "otp": "123456" }`
- Response: `{ "success": true, "message": "OTP verified successfully" }`

#### Revoke OTP
- **DELETE** `/api/otp/revoke`
- Body: `{ "email": "john@example.com" }`
- Response: `{ "message": "OTP revoked successfully" }`

## Key Differences from Express.js

1. **Database**: MongoDB → MySQL with SQLAlchemy ORM
2. **Password Hashing**: bcryptjs → passlib with bcrypt
3. **JWT**: jsonwebtoken → python-jose
4. **Rate Limiting**: express-rate-limit → slowapi
5. **Security Headers**: helmet → custom middleware
6. **Validation**: Manual validation → Pydantic schemas

## Security Features

- HTTP-only cookies for token storage
- CSRF protection with SameSite cookies
- Secure cookies in production
- Rate limiting on all endpoints
- Password hashing with bcrypt
- JWT token expiration
- Security headers (XSS, MIME sniffing, clickjacking protection)

## Development

To run in development mode with auto-reload:
```bash
uvicorn main:app --reload --port 4000
```

## Production Deployment

1. Set `NODE_ENV=production` in your `.env` file
2. Use a production-grade ASGI server like Gunicorn with Uvicorn workers:

```bash
pip install gunicorn
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:4000
```

## Testing with cURL

Register a user:
```bash
curl -X POST http://localhost:4000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{"name":"John Doe","email":"john@example.com","password":"password123"}' \
  -c cookies.txt
```

Get current user:
```bash
curl -X GET http://localhost:4000/api/auth/me \
  -b cookies.txt
```

Logout:
```bash
curl -X POST http://localhost:4000/api/auth/logout \
  -b cookies.txt
```

## API Documentation

FastAPI automatically generates interactive API documentation:
- Swagger UI: `http://localhost:4000/docs`
- ReDoc: `http://localhost:4000/redoc`