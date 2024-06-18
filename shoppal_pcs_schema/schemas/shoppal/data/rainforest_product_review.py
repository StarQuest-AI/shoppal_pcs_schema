
from datetime import date, datetime, time
from decimal import Decimal
from enum import Enum
from typing import List, Optional, Dict, Union
from uuid import UUID

from pydantic import BaseModel, Field


class request_info(BaseModel):
    success: Optional[bool] = None
    credits_used: Optional[int] = None
    credits_used_this_request: Optional[int] = None
    credits_remaining: Optional[int] = None
    credits_reset_at: Optional[str] = None


class request_parameters(BaseModel):
    amazon_domain: Optional[str] = None
    asin: Optional[str] = None
    type: Optional[str] = None


class request_metadata(BaseModel):
    created_at: Optional[str] = None
    processed_at: Optional[str] = None
    total_time_taken: Optional[float] = None
    amazon_url: Optional[str] = None


class sub_title(BaseModel):
    text: Optional[str] = None
    link: Optional[str] = None


class product(BaseModel):
    title: Optional[str] = None
    link: Optional[str] = None
    sub_title: Optional[sub_title] = None
    image: Optional[str] = None
    asin: Optional[str] = None


class five_star(BaseModel):
    percentage: Optional[int] = None
    count: Optional[int] = None


class four_star(BaseModel):
    percentage: Optional[int] = None
    count: Optional[int] = None


class three_star(BaseModel):
    percentage: Optional[int] = None
    count: Optional[int] = None


class two_star(BaseModel):
    percentage: Optional[int] = None
    count: Optional[int] = None


class one_star(BaseModel):
    percentage: Optional[int] = None
    count: Optional[int] = None


class rating_breakdown(BaseModel):
    five_star: Optional[five_star] = None
    four_star: Optional[four_star] = None
    three_star: Optional[three_star] = None
    two_star: Optional[two_star] = None
    one_star: Optional[one_star] = None


class summary(BaseModel):
    rating: Optional[float] = None
    ratings_total: Optional[int] = None
    ratings_total_filtered: Optional[int] = None
    reviews_total_filtered: Optional[int] = None
    reviews_total: Optional[int] = None
    rating_breakdown: Optional[rating_breakdown] = None


class date(BaseModel):
    raw: Optional[str] = None
    utc: Optional[str] = None


class profile(BaseModel):
    name: Optional[str] = None
    link: Optional[str] = None
    id: Optional[str] = None
    image: Optional[str] = None


class reviews(BaseModel):
    id: Optional[str] = None
    title: Optional[str] = None
    body: Optional[str] = None
    asin: Optional[str] = None
    body_html: Optional[str] = None
    link: Optional[str] = None
    rating: Optional[int] = None
    date: Optional[date] = None
    profile: Optional[profile] = None
    vine_program: Optional[bool] = None
    verified_purchase: Optional[bool] = None
    review_country: Optional[str] = None
    is_global_review: Optional[bool] = None
    position: Optional[int] = None
    helpful_votes: Optional[int] = None


class pagination(BaseModel):
    ratings_total_filtered: Optional[int] = None
    reviews_total_filtered: Optional[int] = None
    reviews_total: Optional[int] = None
    total_results: Optional[int] = None
    total_pages: Optional[int] = None
    message: Optional[str] = None
    current_page: Optional[int] = None
    start: Optional[int] = None
    end: Optional[int] = None


class RainforestProductReview(BaseModel):
    request_info: Optional[request_info] = None
    request_parameters: Optional[request_parameters] = None
    request_metadata: Optional[request_metadata] = None
    product: Optional[product] = None
    summary: Optional[summary] = None
    reviews: Optional[List[reviews]] = None
    pagination: Optional[pagination] = None
