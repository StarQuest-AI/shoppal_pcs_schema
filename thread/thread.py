"""
thread model
"""

# pylint: disable=too-few-public-methods
from typing import Optional
from enum import Enum

from pydantic import BaseModel


class BaseMixin(BaseModel):
    """
    Base mixin model
    """

    created_at: str
    updated_at: str


class ThreadStatus(Enum):
    """
    Thread status enum
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


class PostThread(BaseMixin):
    """
    Thread model
    """

    title: str
    src_title: Optional[str] = None
    # content: str
    # user_id: str
    is_public: Optional[str] = PublicStatus.PRIVATE.value
    status: Optional[str] = ThreadStatus.COMPLETED.value
    refer_thread_id: Optional[str] = None  # 引用嵌套的thread的id
    product_id: Optional[str] = None  # thread所属的产品id
