
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


class Content(BaseModel):
    title: str
    author: Optional[str]
    hostname: str
    date: str
    fingerprint: str
    id: Optional[str]
    license: Optional[str]
    comments: Optional[str]
    raw_text: str
    text: str
    language: Optional[str]
    image: str
    pagetype: str
    filedate: str
    source: str
    source_hostname: str
    excerpt: str
    categories: str
    tags: str


class CrawlerResult(BaseModel):
    crawler_request_info: CrawlerRequestInfo
    original_status: int = Field(200, ge=-2**31, le=(2**31 - 1))
    pc_status: int = Field(200, ge=-2**31, le=(2**31 - 1))
    original_url: str
    url: str
    html: str = ""
    content: Content
    doc_filter_result: List[str]
