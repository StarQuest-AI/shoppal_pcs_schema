"""
search result schemas
"""

# pylint: disable=too-few-public-methods
from typing import Optional

from pydantic import BaseModel


class ProductSearchResult(BaseModel):
    """
    Search result model
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

        symbol: str
        value: float
        currency: str
        raw: str
        asin: str
        link: str

    position: Optional[int] = None
    title: str
    price: Price
    asin: Optional[str] = None
    link: Optional[str] = None
    recent_sales: Optional[str] = None
    categories: Optional[list[Category]] = None
    image: Optional[str] = None
    is_prime: Optional[bool] = None
    rating: Optional[float] = None
    ratings_total: Optional[int] = None
    is_amazon_brand: Optional[bool] = None


class VideoBlock(BaseModel):
    """
    Video block model
    """

    video_link: str
    thumbnail_link: str
    campaign_id: str
    advertiser_id: str
    has_audio: Optional[bool] = True


class ProductSearchResults(BaseModel):
    """
    product search result data model
    """

    results: list[ProductSearchResult]
    related_searches: Optional[list[str]] = None
    video_blocks: Optional[list[str]] = None