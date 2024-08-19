"""
common schemas
"""

from enum import Enum
# pylint: disable=too-few-public-methods
from typing import Optional

from pydantic import BaseModel

from favie_api_schema.schemas.common_search_result import (
    GoogleSearchResult, PageSource)
from favie_api_schema.schemas.product_detail import ProductDetail
from favie_api_schema.schemas.video_detail import VideoBaseInfos

DEFAULT_ICON = "https://img.favie.ai/deal/favie-icon.png"
REDDIT_ICON = "https://img.favie.ai/deal/reddit-icon.png"
AMAZON_ICON = "https://www.amazon.com/favicon.ico"

SESSION_START_QUESTIONS = [
    {
        "question": "Uncover top expert insights on this product",
        "icon_url": "https://copilot.buildagi.dev/icon%2Fworth.png",
        "action": {
            "router": "reviews_feed",
            "type": "favie_api_schema.schemas.common.ReviewRequest",
        },
    },
    {
        "question": "Other popular choices",
        "icon_url": "https://copilot.buildagi.dev/icon%2Fpopular.png",
        "action": {
            "router": "product_recommendation",
            "type": "favie_api_schema.schemas.common.RecommendProductRequest",
        },
    },
]

DEFAULT_TOP_POST_LIST = [
    {
        "question": "Get a quick overview of this product",
        "icon_url": DEFAULT_ICON,
        "action": {
            "router": "favie_product_brief",
            "request_type": "favie_api_schema.schemas.common.RecommendProductRequest",
        },
        "template_id": "6",
        "image_url": "https://img.favie.ai/deal/quick_overview.png",
    },
    {
        "question": "Uncover top expert insights on this product",
        "icon_url": DEFAULT_ICON,
        "action": {
            "router": "reviews_feed",
            "request_type": "favie_api_schema.schemas.common.ReviewRequest",
        },
        "template_id": "2",
        "image_url": "https://img.favie.ai/deal/top_export_opinions.png",
    },
]
DEFAULT_IMPORTANT_WEBSITE_POSTS = [
    {
        "question": "What are users saying about this product on Reddit?",
        "icon_url": REDDIT_ICON,
        "action": {
            "router": "",
            "request_type": "favie_api_schema.schemas.common.RecommendProductRequest",
        },
        "template_id": "101",
        "image_url": "https://img.favie.ai/deal/reddit-cover-image.jpeg",
    }
]
DEFAULT_POST_LIST = [
    {
        "question": "Discover the best choices in this category",
        "icon_url": DEFAULT_ICON,
        "action": {
            "router": "product_recommendation",
            "request_type": "favie_api_schema.schemas.common.RecommendProductRequest",
        },
        "template_id": "3",
        "image_url": "https://img.favie.ai/deal/other_popular_choices.png",
    },
    {
        "question": "Key factors for choosing the product that's best for you",
        "icon_url": DEFAULT_ICON,
        "action": {
            "router": "favie_how_to_choose",
            "request_type": "favie_api_schema.schemas.common.RecommendProductRequest",
        },
        "template_id": "4",
        "image_url": "https://img.favie.ai/deal/how_to_choose.png",
    },
    {
        "question": "Find the representative product at each price range",
        "icon_url": DEFAULT_ICON,
        "action": {
            "router": "favie_price_range",
            "request_type": "favie_api_schema.schemas.common.RecommendProductRequest",
        },
        "template_id": "5",
        "image_url": "https://img.favie.ai/deal/best_choice_at_each_price.png",
    },
]

POST_DEFAULT_COVER_IMAGES = [
    "https://img.favie.ai/deal/Anti-valentines%20Facebook%20Post.jpg",
    "https://img.favie.ai/deal/Beige%20Brown%20Add%20to%20Cart%20Instagram.jpg",
    "https://img.favie.ai/deal/screenshot-20240524-181423.jpg",
    "https://img.favie.ai/deal/screenshot-20240524-175724.jpg",
    "https://img.favie.ai/deal/screenshot-20240524-175232.jpg",
    "https://img.favie.ai/deal/Retro%20Gradient%20Quote%20Instagram.jpeg",
    "https://img.favie.ai/deal/Retro%20Cupcake%20Shop%20Quote.jpg",
    "https://img.favie.ai/deal/Powder%20Blue%20Instagram%20Post.jpg",
    "https://img.favie.ai/deal/Easy%20Hopping%20Logo.jpg",
    "https://img.favie.ai/deal/Colorful%20Retro%20Hippie%20Instagram.jpg",
    "https://img.favie.ai/deal/Black Friday Minicart Facebook Post.jpg",
]


WEBPAGE_EXCLUDE_SITES = [
    "ebay.com",
    "temu.com",
    "shein.com",
    "walmart.com",
    "target.com",
    "newegg.com",
    "costco.com",
    "macys.com",
    "shopify.com",
    "craigslist.com",
    "bestbuy.com",
    "etsy.com",
    "homedeopt.com",
    "lowes.com",
    "wayfair.com",
    "taobao.com",
    "jd.com",
    "pinduoduo.com",
]


class SragLLM(Enum):
    """
    llm platform
    """

    OPENAI = "openai"
    CLAUDE = "claude"


class LLMPlatform(Enum):
    """
    llm engine
    """

    PPLX = "pplx"
    SRAG = "srag"


class ItemType(Enum):
    """
    Item Type
    """

    YOUTUBE = "youtube"
    ARTICLE = "article"


class DataFormat(Enum):
    """
    Data Format
    """

    JSON = "json"
    HTML = "html"
    TEXT = "text"
    MARKDOWN = "markdown"


class BaseRequest(BaseModel):
    """
    Base Request
    """

    use_cache: Optional[bool] = True
    version: Optional[str] = None
    post_id: Optional[str] = None


class BaseResponse(BaseModel):
    """
    Base Response
    """

    latency: Optional[float] = None
    data_format: Optional[str] = None
    content: Optional[str] = None
    end_content: Optional[str] = None
    sources: Optional[list[PageSource]] = None
    post_id: Optional[str] = None


class FunctionCallRequestBase(BaseRequest):
    """
    Request Base
    """

    class Message(BaseModel):
        """
        Message
        """

        text: str
        role: str

    class Page(BaseModel):
        """
        Page
        """

        start: int = 0
        num: int = 2

    content: Optional[str] = None
    pages: Optional[Page] = None
    history_content: Optional[list[Message]] = None
    prompt: Optional[str] = ""
    params: Optional[dict] = None
    product: ProductDetail


class GenericRequest(FunctionCallRequestBase):
    """
    Standard Request
    """


class ProsConsRequest(FunctionCallRequestBase):
    """
    Pros and cons request
    """


class ReviewRequest(FunctionCallRequestBase):
    """
    Review Request
    """


class RecommendProductRequest(FunctionCallRequestBase):
    """
    Recommend Product Request
    """


class SessionStartQuestionRequest(FunctionCallRequestBase):
    """
    Related Requestion
    """


class FunctionAction(BaseModel):
    """
    Function Action
    """

    router: Optional[str] = None
    request_type: Optional[str] = None


class SessionStartQuestionResult(BaseResponse):
    """
    Related Response
    """

    class Question(BaseModel):
        """
        Question
        """

        question: str
        icon_url: Optional[str] = None
        action: Optional[FunctionAction] = None
        actions: Optional[list[FunctionAction]] = None
        id: Optional[str] = None
        image_url: Optional[str] = None
        mobile_image_url: Optional[str] = None
        question_for_query: Optional[str] = None
        llm_query: Optional[str] = None
        source_name: Optional[str] = None
        show_question: Optional[str] = None
        username: Optional[str] = None
        avatar: Optional[str] = None

    questions: Optional[list[Question]] = None


class ProsConsResponse(BaseResponse):
    """
    Pros and cons model
    """

    class Entry(BaseModel):
        """
        Entry model
        """

        keyword: str
        content: Optional[str] = None

    pros: Optional[list[Entry]] = None
    cons: Optional[list[Entry]] = None


class ReviewType(Enum):
    """
    Entry Type
    """

    PROS = "pros"
    CONS = "cons"
    NEUTRAL = "neutral"


class SummaryProsCons(BaseModel):
    """
    Summary Pros Cons
    """

    review_type: str = ReviewType.NEUTRAL.value
    keyword: Optional[str]
    content: Optional[str] = None
    color: Optional[str] = "#000000"


class ReviewFeed(BaseResponse):
    """
    Review Feed
    """

    class VideoReview(VideoBaseInfos):
        """
        Video Review
        """

        position: Optional[int] = None
        overview: Optional[str] = None
        pros_cons: Optional[list[SummaryProsCons]] = None
        src: Optional[PageSource] = None

    class WebPageReview(GoogleSearchResult):
        """
        Web Page Review
        """

        position: Optional[int] = None
        overview: Optional[str] = None
        pros_cons: Optional[list[SummaryProsCons]] = None
        src: Optional[PageSource] = None

    sources: Optional[list[PageSource]] = None
    video: Optional[list[VideoReview]] = None
    webpage: Optional[list[WebPageReview]] = None


class CompareRequest(BaseRequest):
    """
    Compare Request
    """

    content: Optional[str] = None
    prompt: Optional[str] = ""
    products: list[ProductDetail]


class CompareResult(BaseResponse):
    """
    Compare Result
    """

    result: Optional[str] = None
    data_format: Optional[str] = DataFormat.MARKDOWN.value


class RecommendProductResult(BaseModel):
    """
    Recommend Product Result
    """

    query: str
    site: Optional[str] = None
    product: Optional[ProductDetail] = None
    compare_result: Optional[CompareResult] = None


class RecommendProductResults(BaseResponse):
    """
    Recommend Product Result
    """

    products: list[RecommendProductResult]


class ProductsRequest(BaseModel):
    """
    Products Request
    """

    products: list[ProductDetail]


class SearchWebRequest(BaseModel):
    """
    SearchWebRequest
    """

    class SearchWebQuery(BaseModel):
        """
        SearchWebQuery
        """

        query: str
        site: Optional[str] = None

    querys: list[SearchWebQuery] = []


class SearchQueryRecommendResponse(BaseModel):
    """
    SearchQueryRecommendResponse
    """

    class SearchQueryRecommend(BaseModel):
        """
        SearchWebQuery
        """

        search_query: str
        title: str

    topics: list[SearchQueryRecommend]
