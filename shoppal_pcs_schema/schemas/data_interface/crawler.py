from decimal import Decimal
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field

from shoppal_pcs_schema.schemas.shoppal.data.rainforest_product_review import \
    ShoppalSpiderProductReviewData
from shoppal_pcs_schema.schemas.shoppal.data.shoppal_spider_data import (
    ContentType, ShoppalSpiderData)
from shoppal_pcs_schema.schemas.shoppal.data.shoppal_spider_product_data import \
    ShoppalSpiderProductData


class CrawlerStatus(Enum):
    """每个资源的状态"""

    NOTEXIST = "notexist"
    PROCESSING = "processing"
    SUCCESS = "success"
    FAILED = "failed"


class CrawlerDataRequest(BaseModel):
    """Crawler data request model."""

    url: str
    content_type: Optional[ContentType] = None


class CrawlerDataResponse(BaseModel):
    """Crawler data response model."""

    status: CrawlerStatus
    data: Optional[ShoppalSpiderData] = None


class CrawlerProductDataRequest(BaseModel):
    """Crawler product data request model."""

    product_id: Optional[str] = None
    url: Optional[str] = None


class CrawlerProductDataResponse(BaseModel):
    """Crawler product data response model."""

    status: CrawlerStatus
    data: Optional[ShoppalSpiderProductData] = None


class CrawlerProductReviewDataResponse(BaseModel):
    """Crawler product review data response model."""

    status: CrawlerStatus
    data: Optional[ShoppalSpiderProductReviewData] = None


class MainImage(BaseModel):
    """
    Main image schema.
    """

    link: Optional[str] = None


class ProductCard(BaseModel):
    """
    Product card schema.
    """

    product_id: str = Field(alias="asin")
    title: str
    main_image: Optional[MainImage] = None
    images: Optional[List[MainImage]] = None
    link: Optional[str] = None
    origin_price: Optional[Decimal] = None
    current_price: Optional[Decimal] = None
    currency_symbol: Optional[str] = None
    discount: Optional[Decimal] = None
    rating: Optional[Decimal] = None
    ratings_total: Optional[int] = None
    sell_amount_last_month: Optional[int] = None
    brand: Optional[str] = None
    categories: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)