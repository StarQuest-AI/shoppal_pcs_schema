
from datetime import date, datetime, time
from decimal import Decimal
from enum import Enum
from typing import List, Optional, Dict, Union
from uuid import UUID

from pydantic import BaseModel, Field


class RequestInfo(BaseModel):
    success: bool
    credits_used: int
    credits_remaining: int


class RequestMetadata(BaseModel):
    id: str
    created_at: str
    processed_at: str
    total_time_taken: float
    amazon_url: str


class RequestParameters(BaseModel):
    type: str
    url: str


class Price(BaseModel):
    symbol: str
    currency: str
    value: int
    raw: str


class Variants(BaseModel):
    asin: str
    text: str
    dimensions: Optional[str]
    link: str
    price: Price


class Categories(BaseModel):
    name: str
    link: str
    category_id: str


class BestsellersRank(BaseModel):
    category: str
    rank: int
    link: str


class SummarizationAttributes(BaseModel):
    name: str
    value: float
    id: str


class AmazonsChoice(BaseModel):
    keywords: str
    link: str


class ClimatePledgeFriendly(BaseModel):
    text: str
    image: str
    link: str


class Promotions(BaseModel):
    name: str


class FirstAvailable(BaseModel):
    raw: str
    utc: str


class SubTitle(BaseModel):
    text: str
    link: str


class Date(BaseModel):
    raw: str
    utc: str


class Profile(BaseModel):
    name: str
    link: str
    id: str


class TopReviews(BaseModel):
    id: str
    title: str
    body: str
    body_html: str
    link: str
    rating: int
    date: Date
    profile: Profile
    vine_program: bool
    verified_purchase: bool
    helpful_votes: int
    review_country: str
    is_global_review: bool


class MainImage(BaseModel):
    link: str


class Images(BaseModel):
    link: str


class Videos(BaseModel):
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


class Sections(BaseModel):
    title: str
    body: str


class ImportantInformation(BaseModel):
    sections: List[Sections]


class MoreBuyingChoices(BaseModel):
    price: Price
    seller_name: str
    seller_link: str
    free_shipping: Optional[bool]
    position: int


class Specifications(BaseModel):
    name: str
    value: str


class Services(BaseModel):
    title: str
    price: Price
    whats_included: List[str]


class Attributes(BaseModel):
    name: str
    value: str


class Product(BaseModel):
    title: str
    variants: List[Variants]
    keywords: str
    keywords_list: List[str]
    link: str
    parent_asin: str
    categories: List[Categories]
    bestsellers_rank: List[BestsellersRank]
    summarization_attributes: List[SummarizationAttributes]
    amazons_choice: AmazonsChoice
    climate_pledge_friendly: ClimatePledgeFriendly
    kindle_unlimited: bool
    has_coupon: bool
    coupon_text: str
    promotions: List[Promotions]
    brand: str
    weight: str
    shipping_weight: str
    first_available: FirstAvailable
    delivery_message: str
    dimensions: str
    sub_title: SubTitle
    rating: float
    ratings_total: int
    reviews_total: int
    top_reviews: List[TopReviews]
    main_image: MainImage
    images: List[Images]
    videos: List[Videos]
    is_bundle: bool
    feature_bullets: List[str]
    important_information: ImportantInformation
    more_buying_choices: List[MoreBuyingChoices]
    specifications: List[Specifications]
    services: List[Services]
    attributes: List[Attributes]


class TotalPrice(BaseModel):
    symbol: str
    value: float
    currency: str
    raw: str


class Products(BaseModel):
    asin: str
    title: str
    link: str
    price: Price


class FrequentlyBoughtTogether(BaseModel):
    total_price: TotalPrice
    products: List[Products]


class AlsoViewed(BaseModel):
    title: str
    link: str
    image: str
    rating: float
    ratings_total: int
    is_prime: bool
    price: Price


class RRP(BaseModel):
    value: float
    currency: str
    raw: str


class Bundles(BaseModel):
    asin: str
    title: str
    link: str
    image: str
    rating: float
    ratings_total: int
    item_count: int
    price: Price
    rrp: Optional[RRP]


class BundleContents(BaseModel):
    asin: str
    title: str
    link: str
    image: str
    rating: float
    ratings_total: int
    item_count: int
    price: Price


class SponsoredProducts(BaseModel):
    title: str
    link: str
    image: str
    rating: float
    ratings_total: int
    is_prime: bool
    price: Price


class Items(BaseModel):
    asin: str
    link: str
    title: str
    image: str
    is_prime: bool
    price: Price
    ratings_total: Optional[int]


class ShopByLook(BaseModel):
    title: str
    items: List[Items]


class RainforestProductDetail(BaseModel):
    request_info: RequestInfo
    request_metadata: RequestMetadata
    request_parameters: RequestParameters
    product: Product
    frequently_bought_together: FrequentlyBoughtTogether
    also_viewed: List[AlsoViewed]
    bundles: List[Bundles]
    bundle_contents: List[BundleContents]
    sponsored_products: List[SponsoredProducts]
    shop_by_look: ShopByLook
