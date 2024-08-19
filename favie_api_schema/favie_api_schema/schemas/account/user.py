from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class UserType(str, Enum):
    """User type enum."""

    REGISTERED = "registered"
    UNREGISTERED = "unregistered"


class User(BaseModel):
    """User model."""

    uid: int
    email: str
    firebase_uid: str
    is_active: bool = True
    name: Optional[str] = Field(None, max_length=50)
    bio: Optional[str] = None
    description: Optional[str] = None
    avatar: Optional[str] = None
    phone_number: Optional[str] = None


class UserUpdate(BaseModel):
    """Update user request model."""

    name: Optional[str] = None
    bio: Optional[str] = None
    description: Optional[str] = None
    avatar: Optional[str] = None


class JWTToken(BaseModel):
    """jwt response"""

    access_token: str
    token_type: str = "bearer"
    expires_in: int


class VerfiyUser(BaseModel):
    """Verify user model."""

    uid: int
    email: str
    name: Optional[str] = None
    user_type: Optional[UserType] = None


class UnifyUser(User):
    """统一注册和未注册用户返回 model"""

    uid: int
    user_type: Optional[UserType] = UserType.REGISTERED
    email: Optional[str] = None
    firebase_uid: Optional[str] = None
