
from datetime import date, datetime, time
from decimal import Decimal
from enum import Enum
from typing import List, Optional, Dict, Union
from uuid import UUID

from pydantic import BaseModel, Field


class CrawlerRequestInfo(BaseModel):
    use_api: bool = True
    api_base: str = "https://api.scrapfly.io/scrape"
    api_params: str


class UrlLinkInfo(BaseModel):
    title: str
    link: str


class Content(BaseModel):
    title: str
    links: List[UrlLinkInfo]


class CrawlerResult(BaseModel):
    crawler_request_info: CrawlerRequestInfo
    original_status: int = Field(..., ge=-2**31, le=(2**31 - 1))
    pc_status: int = Field(..., ge=-2**31, le=(2**31 - 1))
    original_url: str
    url: str
    html: str = ""
    content: Content
