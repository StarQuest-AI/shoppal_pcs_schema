"""
product reviews by e-commerce platform and third party review sites
"""

from typing import Optional

from pydantic import BaseModel

from favie_api_schema.schemas.product_detail import (ProductPlatForm,
                                                       ReviewInfo)


class EcommercePlatformReview(BaseModel):
    """
    e-commerce platform review model
    """

    platform: str = ProductPlatForm.AMAZON.value
    review: ReviewInfo


class ThirdPartyReview(BaseModel):
    """
    third party review model
    """

    url: str
    full_content: str
    trunk_content: Optional[list[str]] = None
    product_ids: Optional[list[str]] = None


class YoutubeReviews(ThirdPartyReview):
    """
    youtube reviews
    """
