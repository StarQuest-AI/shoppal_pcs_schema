"""
question recommendation message schemas
"""

# pylint: disable=too-few-public-methods
from typing import Optional

from pydantic import BaseModel


class Message(BaseModel):
    """
    Message
    """

    role: str = "user"
    content: str


class QRecRequest(BaseModel):
    """
    Question Recommendation Request
    """

    model: Optional[str] = None
    messages: list[Message]


class Question(BaseModel):
    """
    Question
    """

    display_question: str = None
    search_question: str = None
    llm_question: str = None
    image_url: Optional[str] = None


class QRecResponse(BaseModel):
    """
    Question Recommendation Response
    """

    data: list[Question] = None
