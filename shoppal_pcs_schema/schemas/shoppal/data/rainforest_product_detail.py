
from datetime import date, datetime, time
from decimal import Decimal
from enum import Enum
from typing import List, Optional, Dict, Union
from uuid import UUID

from pydantic import BaseModel, Field


class RequestInfo(BaseModel):
    success: Optional[bool]
    credits_used: Optional[int]
    credits_remaining: Optional[int]


class RequestMetadata(BaseModel):
    id: Optional[str]
    created_at: Optional[str]
    processed_at: Optional[str]
    total_time_taken: Optional[float]
    amazon_url: Optional[str]


class RequestParameters(BaseModel):
    type: Optional[str]
    url: Optional[str]


class Price(BaseModel):
    symbol: Optional[str]
    currency: Optional[str]
    value: Optional[int]
    raw: Optional[str]


class Variants(BaseModel):
    asin: Optional[str]
    text: Optional[str]
    dimensions: Optional[str]
    link: Optional[str]
    price: Optional[Price]


class Categories(BaseModel):
    name: Optional[str]
    link: Optional[str]
    category_id: Optional[str]


class BestsellersRank(BaseModel):
    category: Optional[str]
    rank: Optional[int]
    link: Optional[str]


class SummarizationAttributes(BaseModel):
    name: Optional[str]
    value: Optional[float]
    id: Optional[str]


class AmazonsChoice(BaseModel):
    keywords: Optional[str]
    link: Optional[str]


class ClimatePledgeFriendly(BaseModel):
    text: Optional[str]
    image: Optional[str]
    link: Optional[str]


class Promotions(BaseModel):
    name: Optional[str]


class FirstAvailable(BaseModel):
    raw: Optional[str]
    utc: Optional[str]


class SubTitle(BaseModel):
    text: Optional[str]
    link: Optional[str]


class Date(BaseModel):
    raw: Optional[str]
    utc: Optional[str]


class Profile(BaseModel):
    name: Optional[str]
    link: Optional[str]
    id: Optional[str]


class TopReviews(BaseModel):
    id: Optional[str]
    title: Optional[str]
    body: Optional[str]
    body_html: Optional[str]
    link: Optional[str]
    rating: Optional[int]
    date: Optional[Date]
    profile: Optional[Profile]
    vine_program: Optional[bool]
    verified_purchase: Optional[bool]
    helpful_votes: Optional[int]
    review_country: Optional[str]
    is_global_review: Optional[bool]


class MainImage(BaseModel):
    link: Optional[str]


class Images(BaseModel):
    link: Optional[str]


class Videos(BaseModel):
    duration_seconds: Optional[int]
    width: Optional[int]
    height: Optional[int]
    url: Optional[str]
    thumbnail: Optional[str]
    is_hero_video: Optional[bool]
    variant: Optional[str]
    title: Optional[str]
    group_id: Optional[str]
    group_type: Optional[str]


class Sections(BaseModel):
    title: Optional[str]
    body: Optional[str]


class ImportantInformation(BaseModel):
    sections: Optional[List[Sections]]


class MinimumOrderQuantity(BaseModel):
    value: Optional[int]
    message: Optional[str]


class Availability(BaseModel):
    type: Optional[str]
    raw: Optional[str]
    dispatch_days: Optional[int]


class ThirdPartySeller(BaseModel):
    name: Optional[str]
    link: Optional[str]


class Fulfillment(BaseModel):
    type: Optional[str]
    is_sold_by_amazon: Optional[bool]
    is_fulfilled_by_amazon: Optional[bool]
    is_fulfilled_by_third_party: Optional[bool]
    is_sold_by_third_party: Optional[bool]
    third_party_seller: Optional[ThirdPartySeller]


class Claimed(BaseModel):
    percentage: Optional[int]
    raw: Optional[str]


class Timing(BaseModel):
    raw: Optional[str]
    ends_at: Optional[str]
    remaining_hours: Optional[int]
    remaining_minutes: Optional[int]
    remaining_seconds: Optional[int]


class Deal(BaseModel):
    claimed: Optional[Claimed]
    timing: Optional[Timing]


class NewOffersFrom(BaseModel):
    symbol: Optional[str]
    value: Optional[float]
    currency: Optional[str]
    raw: Optional[str]


class UsedOffersFrom(BaseModel):
    symbol: Optional[str]
    value: Optional[float]
    currency: Optional[str]
    raw: Optional[str]


class MixedOffersFrom(BaseModel):
    symbol: Optional[str]
    value: Optional[float]
    currency: Optional[str]
    raw: Optional[str]


class BuyboxWinner(BaseModel):
    minimum_order_quantity: Optional[MinimumOrderQuantity]
    offer_id: Optional[str]
    is_prime: Optional[bool]
    is_prime_exclusive_deal: Optional[bool]
    availability: Optional[Availability]
    fulfillment: Optional[Fulfillment]
    deal: Optional[Deal]
    price: Optional[Price]
    new_offers_count: Optional[int]
    new_offers_from: Optional[NewOffersFrom]
    used_offers_count: Optional[int]
    used_offers_from: Optional[UsedOffersFrom]
    mixed_offers_count: Optional[int]
    mixed_offers_from: Optional[MixedOffersFrom]


class MoreBuyingChoices(BaseModel):
    price: Optional[Price]
    seller_name: Optional[str]
    seller_link: Optional[str]
    free_shipping: Optional[bool]
    position: Optional[int]


class Specifications(BaseModel):
    name: Optional[str]
    value: Optional[str]


class Services(BaseModel):
    title: Optional[str]
    price: Optional[Price]
    whats_included: Optional[List[str]]


class Attributes(BaseModel):
    name: Optional[str]
    value: Optional[str]


class Product(BaseModel):
    title: Optional[str]
    variants: Optional[List[Variants]]
    keywords: Optional[str]
    keywords_list: Optional[List[str]]
    link: Optional[str]
    parent_asin: Optional[str]
    categories: Optional[List[Categories]]
    bestsellers_rank: Optional[List[BestsellersRank]]
    summarization_attributes: Optional[List[SummarizationAttributes]]
    amazons_choice: Optional[AmazonsChoice]
    climate_pledge_friendly: Optional[ClimatePledgeFriendly]
    kindle_unlimited: Optional[bool]
    has_coupon: Optional[bool]
    coupon_text: Optional[str]
    promotions: Optional[List[Promotions]]
    brand: Optional[str]
    weight: Optional[str]
    shipping_weight: Optional[str]
    first_available: Optional[FirstAvailable]
    delivery_message: Optional[str]
    dimensions: Optional[str]
    sub_title: Optional[SubTitle]
    rating: Optional[float]
    ratings_total: Optional[int]
    reviews_total: Optional[int]
    top_reviews: Optional[List[TopReviews]]
    main_image: Optional[MainImage]
    images: Optional[List[Images]]
    videos: Optional[List[Videos]]
    is_bundle: Optional[bool]
    feature_bullets: Optional[List[str]]
    important_information: Optional[ImportantInformation]
    buybox_winner: Optional[BuyboxWinner]
    more_buying_choices: Optional[List[MoreBuyingChoices]]
    specifications: Optional[List[Specifications]]
    services: Optional[List[Services]]
    attributes: Optional[List[Attributes]]


class TotalPrice(BaseModel):
    symbol: Optional[str]
    value: Optional[float]
    currency: Optional[str]
    raw: Optional[str]


class Products(BaseModel):
    asin: Optional[str]
    title: Optional[str]
    link: Optional[str]
    price: Optional[Price]


class FrequentlyBoughtTogether(BaseModel):
    total_price: Optional[TotalPrice]
    products: Optional[List[Products]]


class AlsoViewed(BaseModel):
    title: Optional[str]
    link: Optional[str]
    image: Optional[str]
    rating: Optional[float]
    ratings_total: Optional[int]
    is_prime: Optional[bool]
    price: Optional[Price]


class RRP(BaseModel):
    value: Optional[float]
    currency: Optional[str]
    raw: Optional[str]


class Bundles(BaseModel):
    asin: Optional[str]
    title: Optional[str]
    link: Optional[str]
    image: Optional[str]
    rating: Optional[float]
    ratings_total: Optional[int]
    item_count: Optional[int]
    price: Optional[Price]
    rrp: Optional[RRP]


class BundleContents(BaseModel):
    asin: Optional[str]
    title: Optional[str]
    link: Optional[str]
    image: Optional[str]
    rating: Optional[float]
    ratings_total: Optional[int]
    item_count: Optional[int]
    price: Optional[Price]


class SponsoredProducts(BaseModel):
    title: Optional[str]
    link: Optional[str]
    image: Optional[str]
    rating: Optional[float]
    ratings_total: Optional[int]
    is_prime: Optional[bool]
    price: Optional[Price]


class Items(BaseModel):
    asin: Optional[str]
    link: Optional[str]
    title: Optional[str]
    image: Optional[str]
    is_prime: Optional[bool]
    price: Optional[Price]
    ratings_total: Optional[int]


class ShopByLook(BaseModel):
    title: Optional[str]
    items: Optional[List[Items]]


class RainforestProductDetail(BaseModel):
    request_info: Optional[RequestInfo]
    request_metadata: Optional[RequestMetadata]
    request_parameters: Optional[RequestParameters]
    product: Optional[Product]
    frequently_bought_together: Optional[FrequentlyBoughtTogether]
    also_viewed: Optional[List[AlsoViewed]]
    bundles: Optional[List[Bundles]]
    bundle_contents: Optional[List[BundleContents]]
    sponsored_products: Optional[List[SponsoredProducts]]
    shop_by_look: Optional[ShopByLook]
