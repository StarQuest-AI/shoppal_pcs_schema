"""
post model
"""

from enum import Enum
# pylint: disable=too-few-public-methods
from typing import Optional

from pydantic import BaseModel


class BaseMixin(BaseModel):
    """
    Base mixin model
    """

    created_at: str
    updated_at: str


class PostStatus(Enum):
    """
    Post status enum
    """

    GENERATING = "Generating"
    COMPLETED = "Completed"
    DELETED = "Deleted"


class PublicStatus(Enum):
    """
    Public status enum
    """

    PUBLIC = "public"
    PRIVATE = "private"


class ConversationMessage(BaseMixin):
    """
    Conversation message model
    """

    user_id: str
    content: str


class Post(BaseMixin):
    """
    Post model
    """

    title: str
    src_title: Optional[str] = None
    # content: str
    # user_id: str
    is_public: Optional[str] = PublicStatus.PRIVATE.value
    status: Optional[str] = PostStatus.COMPLETED.value
    refer_post_id: Optional[str] = None
    product_id: Optional[str] = None
