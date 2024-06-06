from datetime import datetime
from enum import Enum
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field

from shoppal_pcs_schema.schemas.shoppal.data.crawler_result import \
    CrawlerResult


class ContentType(str, Enum):
    OTHER = "other"
    WEBPAGE = "webpage"
    SUBTITLE = "subtitle"
    AUDIO = "audio"
    VIDEO = "video"
    IMAGE = "image"


class ShoppalSpiderData(BaseModel):
    id: str  # UUID1
    url: str  # URL
    content_type: Optional[ContentType] = ContentType.OTHER  # used for spider
    source: Optional[int] = 0  # 数据来源，0：未知，1：Spider，2: DataService
    spider: Optional[str] = None  # 爬虫名称, 由不同的content_type交给不同的爬虫处理解析
    crawl_result: Optional[CrawlerResult] = None  # 爬虫结果
    crawl_result_md5: Optional[str] = None  # 爬虫结果MD5
    crawl_time: Optional[datetime] = None  # 爬虫写入时间
    update_time: Optional[datetime] = None  # 数据更新时间
