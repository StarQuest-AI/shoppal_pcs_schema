"""
common schemas
"""

from enum import Enum

# pylint: disable=too-few-public-methods
from typing import Optional

from pydantic import BaseModel

from shoppal_pcs_schema.schemas.common_search_result import (
    GoogleSearchResult,
    PageSource,
)
from shoppal_pcs_schema.schemas.product_detail import ProductDetail
from shoppal_pcs_schema.schemas.video_detail import VideoBaseInfos

SESSION_START_QUESTIONS = [
    {
        "question": "Pros & cons of the product",
        "icon_url": "https://copilot.buildagi.dev/icon%2Fproduct.png",
        "action": {
            "router": "pros_and_cons",
            "type": "shoppal_pcs_schema.schemas.common.ProsConsRequest",
        },
    },
    {
        "question": "Top expert opinions",
        "icon_url": "https://copilot.buildagi.dev/icon%2Fworth.png",
        "action": {
            "router": "reviews_feed",
            "type": "shoppal_pcs_schema.schemas.common.ReviewRequest",
        },
    },
    {
        "question": "Other popular choices",
        "icon_url": "https://copilot.buildagi.dev/icon%2Fpopular.png",
        "action": {
            "router": "product_recommendation",
            "type": "shoppal_pcs_schema.schemas.common.RecommendProductRequest",
        },
    },
]

DEFAULT_THREAD_LIST = [
    {
        "question": "Pros & cons of the product",
        "icon_url": "https://copilot.buildagi.dev/icon%2Fproduct.png",
        "action": {
            "router": "pros_and_cons",
            "type": "shoppal_pcs_schema.schemas.common.ProsConsRequest",
        },
    },
    {
        "question": "Top expert opinions",
        "icon_url": "https://copilot.buildagi.dev/icon%2Fworth.png",
        "action": {
            "router": "reviews_feed",
            "type": "shoppal_pcs_schema.schemas.common.ReviewRequest",
        },
    },
    {
        "question": "Other popular choices",
        "icon_url": "https://copilot.buildagi.dev/icon%2Fpopular.png",
        "action": {
            "router": "product_recommendation",
            "type": "shoppal_pcs_schema.schemas.common.RecommendProductRequest",
        },
    },
    {
        "question": "Quick overview of this product",
        "icon_url": "",
        "action": {
            "router": "generic",
            "type": "shoppal_pcs_schema.schemas.common.GenericRequest",
        }
    },
    {
        "question": "How to choose",
        "icon_url": "",
        "action": {
            "router": "generic",
            "type": "shoppal_pcs_schema.schemas.common.GenericRequest",
        }
    },
    {
        "question": "Best choice at each price",
        "icon_url": "",
        "action": {
            "router": "generic",
            "type": "shoppal_pcs_schema.schemas.common.GenericRequest",
        }
    },
    {
        "question": "Product Demo",
        "icon_url": "",
        "action": {
            "router": "generic",
            "type": "shoppal_pcs_schema.schemas.common.GenericRequest",
        }
    },
]


WEBPAGE_EXCLUDE_SITES = [
    "amazon.*",
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
    "youtube.com",
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


class BaseResponse(BaseModel):
    """
    Base Response
    """

    latency: Optional[float] = None
    data_format: Optional[str] = None
    content: Optional[str] = None
    end_content: Optional[str] = None
    sources: Optional[list[PageSource]] = None


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
    type: Optional[str] = None


class SessionStartQuestionResult(BaseResponse):
    """
    Related Response
    """

    class Question(BaseModel):
        """
        Question
        """

        question: str
        icon_url: str
        action: Optional[FunctionAction]
        id: Optional[str] = None
        image_url: Optional[str] = None

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
