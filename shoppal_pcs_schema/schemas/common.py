"""
common schemas
"""

from enum import Enum

# pylint: disable=too-few-public-methods
from typing import Optional

from pydantic import BaseModel

from .common_search_result import GoogleSearchResult, PageSource
from .product_detail import ProductDetail
from .video_detail import VideoBaseInfos


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

    use_cache: Optional[bool] = False


class BaseResponse(BaseModel):
    """
    Base Response
    """

    latency: Optional[float] = None
    data_format: Optional[DataFormat] = None
    content: Optional[str] = None
    end_content: Optional[str] = None


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

    content: Optional[str] = None
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

    review_type: ReviewType = ReviewType.NEUTRAL
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
    data_format: Optional[DataFormat] = DataFormat.MARKDOWN


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
