"""
schemas
"""

# pylint: disable=too-few-public-methods
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class SearchData(BaseModel):
    """
    Search data model
    """

    search: str
    limit: Optional[int] = 10
    offset: Optional[int] = 0


class ProductPlatForm(str, Enum):
    """
    product type Enum
    """

    AMAZON = "amazon"


class Category(BaseModel):
    """
    category model
    """

    name: Optional[str] = None
    link: Optional[str] = None
    category_id: Optional[str] = None


class ImageInfo(BaseModel):
    """
    image info model
    """

    link: str
    variant: Optional[str] = None


class VideoInfo(BaseModel):
    """
    video info model
    """

    duration_seconds: Optional[int] = None
    width: Optional[int] = None
    height: Optional[int] = None
    link: Optional[str] = None
    thumbnail: Optional[str] = None
    is_hero_video: Optional[bool] = None
    variant: Optional[str] = None
    group_id: Optional[str] = None
    group_type: Optional[str] = None
    title: Optional[str] = None


class UserProfile(BaseModel):
    """
    user profile model
    """

    name: Optional[str] = None
    link: Optional[str] = None
    id: Optional[str] = None


class ReviewInfo(BaseModel):
    """
    review info model
    """

    id: Optional[str] = None
    title: Optional[str] = None
    body: Optional[str] = None
    asin: Optional[str] = None
    body_html: Optional[str]
    link: Optional[str] = None
    rating: Optional[int] = None
    date: Optional[dict] = None
    profile: Optional[UserProfile] = None
    vine_program: Optional[bool] = None
    verified_purchase: Optional[bool] = None
    review_country: Optional[str] = None
    is_global_review: Optional[bool] = None


class BestSellerRank(BaseModel):
    """
    best seller rank model
    """

    rank: Optional[int] = None
    category: Optional[str] = None
    link: Optional[str] = None


class AmazonChoice(BaseModel):
    """
    amazon choice model
    """

    keywords: Optional[str] = None


class Price(BaseModel):
    """
    price model
    """

    symbol: Optional[str] = None
    value: Optional[float] = None
    currency: Optional[str] = None
    raw: Optional[str] = None


class BuyBoxWinner(BaseModel):
    """
    buy box winner model
    """

    class MaximumOrderQuantity(BaseModel):
        """
        maximum order quantity model
        """

        value: Optional[int] = None
        hard_maximum: Optional[bool] = None

    class Condition(BaseModel):
        """
        condition model
        """

        is_new: Optional[bool] = None

    class Availability(BaseModel):
        """
        availability model
        """

        type: Optional[str] = None
        raw: Optional[str] = None
        dispatch_days: Optional[int] = None

    class Shipping(BaseModel):
        """
        shipping model
        """

        raw: Optional[str] = None

    maximum_order_quantity: Optional[MaximumOrderQuantity] = None
    is_prime: Optional[bool] = None
    is_prime_exclusive_deal: Optional[bool] = None
    is_amazon_fresh: Optional[bool] = None
    condition: Optional[Condition] = None
    availability: Optional[Availability] = None
    fulfillment: Optional[dict] = None
    price: Optional[Price] = None
    shipping: Optional[Shipping] = None


class ProductBase(BaseModel):
    """
    product base model
    """

    global_id: Optional[str] = None  # global id for product
    external_platform: str = ProductPlatForm.AMAZON.value
    platform: str = ProductPlatForm.AMAZON.value
    id: Optional[str] = None  # "asin" for amazon
    title: str
    link: Optional[str] = None
    short_title: Optional[str] = None


class ProductDetail(ProductBase):
    """
    product detail model
    """

    keywords: Optional[str] = None
    brand: Optional[str] = None
    categories: Optional[list[Category]] = None
    description: Optional[str] = None

    rating: Optional[float] = 0.0
    ratings_total: Optional[int] = 0

    main_image: Optional[ImageInfo] = None
    images: Optional[list[ImageInfo]] = None

    # videos: Optional[list[str]] = None

    # top_reviews: Optional[list[ReviewInfo]] = None
    # specifications: Optional[dict] = None
    bestsellers_rank: Optional[list[BestSellerRank]] = None

    feature_bullets: Optional[list[str]] = None
    # first_available: Optional[str] = None

    color: Optional[str] = None

    dimensions: Optional[str] = None

    buybox_winner: Optional[BuyBoxWinner] = None
    price_history: Optional[list[Price]] = None  # for product price trend

    amazon_choice: Optional[AmazonChoice] = None  # only for amazon

    class Config:
        """
        Config
        """

        arbitrary_types_allowed = True
