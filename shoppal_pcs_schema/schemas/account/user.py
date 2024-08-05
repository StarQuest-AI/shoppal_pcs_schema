from typing import Optional

from pydantic import BaseModel, Field

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