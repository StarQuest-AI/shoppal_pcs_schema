"""
search result schemas
"""

# pylint: disable=too-few-public-methods
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class SearchSource(Enum):
    """
    Search source enum
    """

    AMAZON = "amazon"
    GOOGLE = "google"
    YOUTUBE = "youtube"
    GOOGLE_SHOPPING = "google_shopping"


class SearchFilter(BaseModel):
    """
    Search filter model
    """

    class Category(BaseModel):
        """
        category model
        """

        name: str
        id: str

    class Price(BaseModel):
        """
        price model
        """

        min: Optional[float] = None
        max: Optional[float] = None

    price: Optional[Price] = None
    categories: Optional[list[Category]] = None
    keyword_tags: Optional[list[str]] = None


class SearchRequest(BaseModel):
    """
    Search request model
    """

    q: str
    limit: Optional[int] = 10
    offset: Optional[int] = 0
    source: Optional[str] = None
    filter: Optional[SearchFilter] = None
