
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


class ParsedWebPageContent(BaseModel):
    title: Optional[str]
    author: Optional[str]
    hostname: Optional[str]
    date: Optional[str]
    fingerprint: Optional[str]
    id: Optional[str]
    license: Optional[str]
    comments: Optional[str]
    raw_text: Optional[str]
    text: Optional[str]
    language: Optional[str]
    image: Optional[str]
    pagetype: Optional[str]
    filedate: Optional[str]
    source: Optional[str]
    source_hostname: Optional[str]
    excerpt: Optional[str]
    categories: Optional[str]
    tags: Optional[str]


class WebPageContent(BaseModel):
    raw_html: Optional[str]
    parsed_webpage_content: Optional[ParsedWebPageContent]


class Content(BaseModel):
    title: Optional[str]
    author: Optional[str]
    hostname: Optional[str]
    date: Optional[str]
    fingerprint: Optional[str]
    id: Optional[str]
    license: Optional[str]
    comments: Optional[str]
    raw_text: Optional[str]
    text: Optional[str]
    language: Optional[str]
    image: Optional[str]
    pagetype: Optional[str]
    filedate: Optional[str]
    source: Optional[str]
    source_hostname: Optional[str]
    excerpt: Optional[str]
    categories: Optional[str]
    tags: Optional[str]


class CrawlerResult(BaseModel):
    crawler_request_info: CrawlerRequestInfo
    original_status: int = Field(200, ge=-2**31, le=(2**31 - 1))
    pc_status: int = Field(200, ge=-2**31, le=(2**31 - 1))
    original_url: str
    url: str
    webpage: Optional[WebPageContent]
    html: str = ""
    content: Optional[Content]
    doc_filter_result: List[str]
