import uuid
from datetime import datetime
from enum import Enum, IntEnum
from typing import Optional

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


class Source(IntEnum):
    # 未知
    UNKNOWN = 0
    # 爬虫爬取页面
    SPIDER = 1
    # 数据服务写入
    DATA_SERVICE = 2
    # 爬虫调用RF API获取
    SPIDER_CALL_RF_API = 3


class ShoppalSpiderData(BaseModel):
    id: str = uuid.uuid1().hex  # UUID1
    url: str  # URL
    content_type: Optional[ContentType] = ContentType.OTHER  # used for spider
    source: Optional[Source] = 0  # 数据来源
    spider: Optional[str] = None  # 爬虫名称, 由不同的content_type交给不同的爬虫处理解析
    crawl_result: Optional[CrawlerResult] = None  # 爬虫结果
    crawl_time: Optional[datetime] = datetime.now()  # 爬虫写入时间
    update_time: Optional[datetime] = datetime.now()  # 数据更新时间
