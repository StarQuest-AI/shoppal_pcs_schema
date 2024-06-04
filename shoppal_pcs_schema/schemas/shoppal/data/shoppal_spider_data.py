
from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field
from shoppal_pcs_schema.schemas.shoppal.data.crawler_result import CrawlerResult

class ShoppalSpiderData(BaseModel):
    id: str # UUID1
    url: str # URL
    spider: Optional[str] = None # used for spider
    source: Optional[int] = 0 # 数据来源，0：未知，1：Spider，2: DataService
    crawl_result: Optional[CrawlerResult] # 爬虫结果
    crawl_result_md5: Optional[str] # 爬虫结果MD5
    crawl_time: Optional[datetime] # 爬虫写入时间
    update_time: Optional[datetime] # 数据更新时间
    