# schemas/__init__.py

from schemas.auth import (
    UserRegister,
    UserLogin,
    VerifyEmailRequest,
    ForgotPasswordRequest,
    ResetPasswordRequest,
    UserResponse,
    UserOut,
    MessageResponse
)

from schemas.blog import (
    BlogSectionSchema,
    BlogCreateSchema,
    BlogUpdateSchema,
    BlogResponseSchema,
    BlogListResponseSchema,
    BlogListResponse
)

__all__ = [
    # Auth schemas
    "UserRegister",
    "UserLogin",
    "VerifyEmailRequest",
    "ForgotPasswordRequest",
    "ResetPasswordRequest",
    "UserResponse",
    "UserOut",
    "MessageResponse",
    # Blog schemas
    "BlogSectionSchema",
    "BlogCreateSchema",
    "BlogUpdateSchema",
    "BlogResponseSchema",
    "BlogListResponseSchema",
    "BlogListResponse"
]