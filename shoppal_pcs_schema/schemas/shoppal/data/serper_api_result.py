from datetime import date, datetime, time
from decimal import Decimal
from enum import Enum
from typing import Dict, List, Optional, Union
from uuid import UUID

from pydantic import BaseModel, Field


class SearchMetadata(BaseModel):
    id: str
    status: str
    json_endpoint: str
    created_at: str
    processed_at: str
    google_url: str
    raw_html_file: str
    total_time_taken: float


class SearchParameters(BaseModel):
    engine: str
    q: str
    location_requested: str
    location_used: str
    google_domain: str
    hl: str
    gl: str
    safe: str
    start: int
    num: str
    device: str


class SearchInformation(BaseModel):
    organic_results_state: str
    query_displayed: str
    total_results: int
    page_number: int
    time_taken_displayed: float


class source(BaseModel):
    description: str
    icon: Optional[str]


class AboutThisResult(BaseModel):
    source: source
    keywords: List[str]
    related_keywords: Optional[List[str]]
    languages: List[str]
    regions: List[str]


class DetectedExtensions(BaseModel):
    rating: int
    review_by_jennaviles: int


class top(BaseModel):
    detected_extensions: DetectedExtensions
    extensions: List[str]


class RichSnippet(BaseModel):
    top: top


class OrganicResults(BaseModel):
    position: int
    title: str
    link: str
    redirect_link: Optional[str]
    displayed_link: str
    thumbnail: Optional[str]
    date: Optional[str]
    snippet: str
    snippet_highlighted_words: List[str]
    about_this_result: AboutThisResult
    about_page_link: str
    about_page_serpapi_link: str
    cached_page_link: str
    related_pages_link: Optional[str]
    rich_snippet: Optional[RichSnippet]
    reirect_link: Optional[str]


class RelatedSearches(BaseModel):
    query: str
    link: str


class Pagination(BaseModel):
    current: int
    previous: str
    next: str


class SerpapiPagination(BaseModel):
    current: int
    previous_link: str
    previous: str
    next_link: str
    next: str


class SerperAPiResult(BaseModel):
    search_metadata: SearchMetadata
    search_parameters: SearchParameters
    search_information: SearchInformation
    organic_results: List[OrganicResults]
    related_searches: List[RelatedSearches]
    pagination: Pagination
    serpapi_pagination: SerpapiPagination
