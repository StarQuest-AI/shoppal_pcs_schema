from enum import Enum
from typing import Optional

from pydantic import BaseModel

from shoppal_pcs_schema.schemas.shoppal.data.shoppal_spider_data import (
    ContentType, ShoppalSpiderData)


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
