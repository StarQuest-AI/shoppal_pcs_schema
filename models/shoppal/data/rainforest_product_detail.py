
from datetime import date, datetime, time
from decimal import Decimal
from enum import Enum
from typing import List, Optional, Dict, Union
from uuid import UUID

from pydantic import BaseModel, Field


class request_info(BaseModel):
    success: bool
    credits_used: int
    credits_remaining: int


class request_metadata(BaseModel):
    id: str
    created_at: str
    processed_at: str
    total_time_taken: float
    amazon_url: str


class request_parameters(BaseModel):
    type: str
    url: str


class price(BaseModel):
    symbol: str
    currency: str
    value: int
    raw: str


class variants(BaseModel):
    asin: str
    text: str
    dimensions: Optional[str]
    link: str
    price: price


class categories(BaseModel):
    name: str
    link: str
    category_id: str


class bestsellers_rank(BaseModel):
    category: str
    rank: int
    link: str


class summarization_attributes(BaseModel):
    name: str
    value: float
    id: str


class amazons_choice(BaseModel):
    keywords: str
    link: str


class climate_pledge_friendly(BaseModel):
    text: str
    image: str
    link: str


class promotions(BaseModel):
    name: str


class first_available(BaseModel):
    raw: str
    utc: str


class sub_title(BaseModel):
    text: str
    link: str


class date(BaseModel):
    raw: str
    utc: str


class profile(BaseModel):
    name: str
    link: str
    id: str


class top_reviews(BaseModel):
    id: str
    title: str
    body: str
    body_html: str
    link: str
    rating: int
    date: date
    profile: profile
    vine_program: bool
    verified_purchase: bool
    helpful_votes: int
    review_country: str
    is_global_review: bool


class main_image(BaseModel):
    link: str


class images(BaseModel):
    link: str


class videos(BaseModel):
    duration_seconds: int
    width: int
    height: int
    url: str
    thumbnail: str
    is_hero_video: bool
    variant: str
    title: str
    group_id: str
    group_type: str


class sections(BaseModel):
    title: str
    body: str


class important_information(BaseModel):
    sections: List[sections]


class more_buying_choices(BaseModel):
    price: price
    seller_name: str
    seller_link: str
    free_shipping: Optional[bool]
    position: int


class specifications(BaseModel):
    name: str
    value: str


class services(BaseModel):
    title: str
    price: price
    whats_included: List[str]


class attributes(BaseModel):
    name: str
    value: str


class product(BaseModel):
    title: str
    variants: List[variants]
    keywords: str
    keywords_list: List[str]
    link: str
    parent_asin: str
    categories: List[categories]
    bestsellers_rank: List[bestsellers_rank]
    summarization_attributes: List[summarization_attributes]
    amazons_choice: amazons_choice
    climate_pledge_friendly: climate_pledge_friendly
    kindle_unlimited: bool
    has_coupon: bool
    coupon_text: str
    promotions: List[promotions]
    brand: str
    weight: str
    shipping_weight: str
    first_available: first_available
    delivery_message: str
    dimensions: str
    sub_title: sub_title
    rating: float
    ratings_total: int
    reviews_total: int
    top_reviews: List[top_reviews]
    main_image: main_image
    images: List[images]
    videos: List[videos]
    is_bundle: bool
    feature_bullets: List[str]
    important_information: important_information
    more_buying_choices: List[more_buying_choices]
    specifications: List[specifications]
    services: List[services]
    attributes: List[attributes]


class total_price(BaseModel):
    symbol: str
    value: float
    currency: str
    raw: str


class products(BaseModel):
    asin: str
    title: str
    link: str
    price: price


class frequently_bought_together(BaseModel):
    total_price: total_price
    products: List[products]


class also_viewed(BaseModel):
    title: str
    link: str
    image: str
    rating: float
    ratings_total: int
    is_prime: bool
    price: price


class rrp(BaseModel):
    value: float
    currency: str
    raw: str


class bundles(BaseModel):
    asin: str
    title: str
    link: str
    image: str
    rating: float
    ratings_total: int
    item_count: int
    price: price
    rrp: Optional[rrp]


class bundle_contents(BaseModel):
    asin: str
    title: str
    link: str
    image: str
    rating: float
    ratings_total: int
    item_count: int
    price: price


class sponsored_products(BaseModel):
    title: str
    link: str
    image: str
    rating: float
    ratings_total: int
    is_prime: bool
    price: price


class items(BaseModel):
    asin: str
    link: str
    title: str
    image: str
    is_prime: bool
    price: price
    ratings_total: Optional[int]


class shop_by_look(BaseModel):
    title: str
    items: List[items]


class RainforestProductDetail(BaseModel):
    request_info: request_info
    request_metadata: request_metadata
    request_parameters: request_parameters
    product: product
    frequently_bought_together: frequently_bought_together
    also_viewed: List[also_viewed]
    bundles: List[bundles]
    bundle_contents: List[bundle_contents]
    sponsored_products: List[sponsored_products]
    shop_by_look: shop_by_look
