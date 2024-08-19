"""
google search result schemas
"""

# pylint: disable=too-few-public-methods
from typing import Optional

from pydantic import BaseModel

from favie_api_schema.schemas import product_detail

DEFAULT_WEBSITE_ICON = "https://img.favie.ai/deal/logo%E5%9C%B0%E7%90%83icon.png"
DEFAULT_YOUTUBE_ICON = "https://img.favie.ai/deal/youtube_website_icon.png"
DEFAULT_WEBSITE_ICONS = [
    "https://img.favie.ai/deal/logo%E5%9C%B0%E7%90%83icon.png",
    "https://img.favie.ai/deal/1.png",
    "https://img.favie.ai/deal/2.png",
    "https://img.favie.ai/deal/3.png",
    "https://img.favie.ai/deal/4.png",
    "https://img.favie.ai/deal/5.png",
    "https://img.favie.ai/deal/6.png",
]


class GoogleSearchResult(BaseModel):
    """
    Google search result model
    """

    position: Optional[int] = None
    title: Optional[str] = None
    link: Optional[str] = None
    redirect_link: Optional[str] = None
    displayed_link: Optional[str] = None
    thumbnail: Optional[str] = None
    favicon: Optional[str] = None
    date: Optional[str] = None
    snippet: Optional[str] = None
    source: Optional[str] = None

    content: Optional[str] = None  #  need crawl to get content
    content_summary: Optional[str] = None  # request llm to get content summary


class InlineVideo(BaseModel):
    """
    inline video model
    """

    class KeyMoment(BaseModel):
        """
        key moment model
        """

        time: str
        title: str
        link: str
        thumbnail: str

    position: Optional[int] = None
    title: Optional[str] = None
    link: Optional[str] = None
    thumbnail: Optional[str] = None
    channel: Optional[str] = None
    duration: Optional[str] = None
    platform: Optional[str] = None
    date: Optional[str] = None
    key_moments: Optional[list[KeyMoment]] = None


class GoogleRelatedQuestion(BaseModel):
    """
    Google related question model
    """

    question: str
    snippet: Optional[str] = None
    title: Optional[str] = None
    date: Optional[str] = None
    link: Optional[str] = None
    displayed_link: Optional[str] = None
    source_logo: Optional[str] = None
    next_page_token: Optional[str] = None
    serpapi_link: Optional[str] = None


class ImmersiveProduct(BaseModel):
    """
    Google immersive product model
    """

    thumbnail: Optional[str] = None
    source: Optional[str] = None
    title: Optional[str] = None
    price: Optional[str] = None
    extracted_price: Optional[float] = None
    immersive_product_page_token: Optional[str] = None
    serpapi_link: Optional[str] = None


class PageSource(BaseModel):
    """
    page source model
    """

    name: Optional[str] = None
    favicon: Optional[str] = DEFAULT_WEBSITE_ICON
    url: Optional[str] = None
    title: Optional[str] = None
    snippet: Optional[str] = None


class CommonSearchResults(BaseModel):
    """
    Google search data model
    """

    results: list[GoogleSearchResult]
    page_source: list[PageSource]
    related_questions: Optional[list[GoogleRelatedQuestion]] = None
    inline_videos: Optional[list[InlineVideo]] = None
    immersive_products: Optional[list[ImmersiveProduct]] = None
    related_searches: Optional[list[str]] = None


class CommonSearchProductResult(product_detail.ProductBase):
    """
    common search product result model
    """

    class RichSnippet(BaseModel):
        """
        rich snippet model
        """

        detected_extensions: dict
        extensions: list[str]

    class CompareResult(BaseModel):
        """
        compare result model
        """

        text: Optional[str] = None
        data_format: Optional[str] = None

    position: Optional[int] = None
    link: Optional[str] = None
    redirect_link: Optional[str] = None
    displayed_link: Optional[str] = None
    thumbnail: Optional[str] = None
    favicon: Optional[str] = None
    snippet: Optional[str] = None
    source: Optional[str] = None
    snippet_highlighted_words: Optional[list[str]] = None
    rich_snippet: Optional[dict] = None
    content: Optional[str] = None
    content_summary: Optional[str] = None
    images: Optional[list[str]] = None
    # KV for product detail TODO
    # rate
    # price
    # review count
