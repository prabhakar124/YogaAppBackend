## Postman Setup Guide

### Step 1: Create Environment

1. Click "Environments" in left sidebar
2. Click "+" to create new environment
3. Name: `Local Development`
4. Add variable:
   - Variable: `base_url`
   - Initial Value: `http://localhost:4000`
   - Current Value: `http://localhost:4000`
5. Save and select environment from dropdown (top-right)

### Step 2: Create Collection

1. Click "New" → "Collection"
2. Name: `FastAPI Auth Backend`
3. Description: `Complete authentication API with email verification`
4. Click "Create"

### Step 3: Add All 8 Requests

#### Request 1: Register User
- Name: `1. Register User`
- Method: `POST`
- URL: `{{base_url}}/api/auth/register`
- Body → raw → JSON

#### Request 2: Verify Email
- Name: `2. Verify Email`
- Method: `POST`
- URL: `{{base_url}}/api/auth/verify-email`
- Body → raw → JSON

#### Request 3: Login
- Name: `3. Login`
- Method: `POST`
- URL: `{{base_url}}/api/auth/login`
- Body → raw → JSON

#### Request 4: Get Current User
- Name: `4. Get Current User`
- Method: `GET`
- URL: `{{base_url}}/api/auth/me`
- No body needed

#### Request 5: Resend Verification OTP
- Name: `5. Resend Verification OTP`
- Method: `POST`
- URL: `{{base_url}}/api/auth/resend-verification-otp`
- Body → raw → JSON

#### Request 6: Forgot Password
- Name: `6. Forgot Password`
- Method: `POST`
- URL: `{{base_url}}/api/auth/forgot-password`
- Body → raw → JSON

#### Request 7: Reset Password
- Name: `7. Reset Password`
- Method: `POST`
- URL: `{{base_url}}/api/auth/reset-password`
- Body → raw → JSON

#### Request 8: Logout
- Name: `8. Logout`
- Method: `POST`
- URL: `{{base_url}}/api/auth/logout`
- No body needed

---

## Request Bodies

### 1. Register User
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "SecurePass123"
}

### Endpoints Summary

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/api/auth/register` | Register new user | No |
| POST | `/api/auth/verify-email` | Verify email with OTP | No |
| POST | `/api/auth/resend-verification-otp` | Resend verification OTP | No |
| POST | `/api/auth/login` | Login user (verified only) | No |
| POST | `/api/auth/forgot-password` | Request password reset OTP | No |
| POST | `/api/auth/reset-password` | Reset password with OTP | No |
| POST | `/api/auth/logout` | Logout user | Yes (Cookie) |
| GET | `/api/auth/me` | Get current user info | Yes (Cookie) |

---

## Registration & Login Flow

### Visual Flow Diagram

## 🎯 Postman Setup Checklist

```
Step 1: Create Environment
┌─────────────────────────────────────┐
│ Environment Name: Local Dev         │
│                                     │
│ Variables:                          │
│ ┌─────────────┬─────────────────┐  │
│ │ Variable    │ Value           │  │
│ ├─────────────┼─────────────────┤  │
│ │ base_url    │ http://localhost│  │
│ │             │ :4000           │  │
│ └─────────────┴─────────────────┘  │
└─────────────────────────────────────┘

Step 2: Create Collection
┌─────────────────────────────────────┐
│ Collection Name: FastAPI Auth       │
│                                     │
│ Requests:                           │
│ ✅ 1. Register User                 │
│ ✅ 2. Verify Email                  │
│ ✅ 3. Login                         │
│ ✅ 4. Get Current User              │
│ ✅ 5. Resend Verification OTP       │
│ ✅ 6. Forgot Password               │
│ ✅ 7. Reset Password                │
│ ✅ 8. Logout                        │
└─────────────────────────────────────┘

Step 3: Configure Each Request
┌─────────────────────────────────────┐
│ For each request:                   │
│ 1. Set method (POST/GET)            │
│ 2. Set URL: {{base_url}}/api/...   │
│ 3. Add body (if needed)             │
│ 4. Set content-type: application/   │
│    json                             │
│ 5. Save request                     │
└─────────────────────────────────────┘
```

---

## 📋 Quick Copy-Paste Bodies

### Registration
```json
{
  "name": "John Doe",
  "email": "test@example.com",
  "password": "SecurePass123"
}
```

### Verification
```json
{
  "email": "test@example.com",
  "otp": "REPLACE_WITH_OTP_FROM_EMAIL"
}
```

### Login
```json
{
  "email": "test@example.com",
  "password": "SecurePass123"
}
```

### Forgot Password
```json
{
  "email": "test@example.com"
}
```

### Reset Password
```json
{
  "email": "test@example.com",
  "otp": "REPLACE_WITH_OTP_FROM_EMAIL",
  "new_password": "NewSecurePass456"
}
```

### Resend OTP
```json
{
  "email": "test@example.com"
}
```

---

## 🍪 Understanding Cookies in Postman

```
┌──────────────────────────────────────────────────────┐
│  How Cookie Authentication Works                     │
└──────────────────────────────────────────────────────┘

Step 1: Login/Verify
    │
    ▼
Server sets cookie
    │
    ▼
┌───────────────────────────────┐
│ Cookie: token=eyJhbGc...      │
│ HttpOnly: true                │
│ Secure: true (production)     │
│ Expires: 7 days               │
└───────────────────────────────┘
    │
    ▼
Postman automatically saves cookie
    │
    ▼
┌───────────────────────────────┐
│ View in Postman:              │
│ 1. Click "Cookies" button     │
│ 2. Expand localhost:4000      │
│ 3. See "token" cookie         │
└───────────────────────────────┘
    │
    ▼
Cookie sent automatically on next requests
    │
    ▼
Protected endpoints work (e.g., /api/auth/me)
```

---

## ⚡ Postman Keyboard Shortcuts

```
┌─────────────────────────────────────┐
│ Ctrl/Cmd + Enter  → Send Request   │
│ Ctrl/Cmd + S      → Save Request   │
│ Ctrl/Cmd + N      → New Request    │
│ Ctrl/Cmd + T      → New Tab        │
│ Ctrl/Cmd + W      → Close Tab      │
│ Ctrl/Cmd + F      → Search         │
└─────────────────────────────────────┘
```

---

## 🎨 Color-Coded Status Codes

```
┌──────────────────────────────────────┐
│ 🟢 200 OK - Success                  │
│ 🟢 201 Created - Resource created    │
│ 🟡 400 Bad Request - Invalid data    │
│ 🟡 401 Unauthorized - Not logged in  │
│ 🟡 403 Forbidden - No permission     │
│ 🟡 404 Not Found - Resource missing  │
│ 🔴 500 Server Error - Backend issue  │
└──────────────────────────────────────┘
```

---

## 🔍 Troubleshooting Decision Tree

```
Problem: Request fails
    │
    ├─ Is server running?
    │   │
    │   ├─ NO → Start: python main.py
    │   │
    │   └─ YES → Continue
    │
    ├─ Is URL correct?
    │   │
    │   ├─ NO → Check: http://localhost:4000
    │   │
    │   └─ YES → Continue
    │
    ├─ Status 401 Unauthorized?
    │   │
    │   ├─ YES → Login first
    │   │        Check cookies enabled
    │   │
    │   └─ NO → Continue
    │
    ├─ Status 400 Bad Request?
    │   │
    │   ├─ YES → Check request body
    │   │        Verify JSON format
    │   │        Check required fields
    │   │
    │   └─ NO → Continue
    │
    └─ Check server logs for errors
```

---

## 📊 Expected Response Times

```
┌────────────────────────────────────────┐
│ Endpoint              │ Expected Time  │
├────────────────────────────────────────┤
│ Register (with email) │ 300-500ms      │
│ Verify Email          │ 150-250ms      │
│ Login                 │ 100-200ms      │
│ Get Current User      │ 50-100ms       │
│ Forgot Password       │ 200-400ms      │
│ Reset Password        │ 150-250ms      │
│ Logout                │ 50-100ms       │
└────────────────────────────────────────┘

Note: Email sending adds 1-5 seconds
```

---

## ✅ Testing Completion Checklist

```
Registration Flow:
├─ ✅ Register new user
├─ ✅ Email received (verification)
├─ ✅ Verify with OTP
├─ ✅ Welcome email received
├─ ✅ Login successful
├─ ✅ Get user data
└─ ✅ Logout successful

Password Reset Flow:
├─ ✅ Request password reset
├─ ✅ Email received (reset OTP)
├─ ✅ Reset password with OTP
├─ ✅ Login with new password
└─ ✅ Verified new password works

Edge Cases:
├─ ✅ Invalid OTP rejected
├─ ✅ Expired OTP rejected
├─ ✅ Invalid credentials rejected
├─ ✅ Duplicate email rejected
└─ ✅ Unverified user can't login
```

---

## 🎉 Success Screen

```
╔═══════════════════════════════════════╗
║                                       ║
║        🎉 ALL TESTS PASSED! 🎉        ║
║                                       ║
║   Your API is working perfectly!     ║
║                                       ║
║   ✅ Registration                     ║
║   ✅ Email Verification               ║
║   ✅ Login                            ║
║   ✅ Protected Routes                 ║
║   ✅ Password Reset                   ║
║   ✅ Logout                           ║
║                                       ║
║   Ready for production! 🚀            ║
║                                       ║
╚═══════════════════════════════════════╝
```

---

**Happy Testing with Postman! 🚀**

Need more details? Check `POSTMAN_TESTING_GUIDE.md`                   START HERE                             │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│  Step 1: POST /api/auth/register                        │
│  ────────────────────────────────────────────────────   │
│  Body:                                                   │
│  {                                                       │
│    "name": "John Doe",                                   │
│    "email": "john@example.com",                          │
│    "password": "SecurePass123"                           │
│  }                                                       │
│                                                          │
│  ✅ Expected: 201 Created                                │
│  📧 Action: CHECK YOUR EMAIL FOR OTP                     │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│  📧 EMAIL INBOX                                          │
│  ────────────────────────────────────────────────────   │
│  Subject: Verify Your Email Address                     │
│  From: Your App Name                                     │
│                                                          │
│  Your verification code is:                              │
│                                                          │
│          ╔═══════════════╗                               │
│          ║   1 2 3 4 5 6 ║  ← COPY THIS OTP             │
│          ╚═══════════════╝                               │
│                                                          │
│  Expires in 5 minutes                                    │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│  Step 2: POST /api/auth/verify-email                    │
│  ────────────────────────────────────────────────────   │
│  Body:                                                   │
│  {                                                       │
│    "email": "john@example.com",                          │
│    "otp": "123456"  ← PASTE OTP FROM EMAIL               │
│  }                                                       │
│                                                          │
│  ✅ Expected: 200 OK + Cookie Set                        │
│  📧 Action: CHECK EMAIL FOR WELCOME MESSAGE              │
│  🍪 Note: JWT cookie automatically saved                 │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│