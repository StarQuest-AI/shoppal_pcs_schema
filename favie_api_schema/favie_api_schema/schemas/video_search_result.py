"""
youtube search result schemas
"""

# pylint: disable=too-few-public-methods
from typing import Optional

from pydantic import BaseModel


class VideoSearchResult(BaseModel):
    """
    Youtube search result model
    """

    class Channel(BaseModel):
        """
        Channel model
        """

        name: str
        link: str
        verified: bool
        thumbnail: str

    class Thumbnail(BaseModel):
        """
        Thumbnail model
        """

        static: str
        rich: Optional[str] = None

    position_on_page: Optional[int] = None
    title: Optional[str] = None
    link: Optional[str] = None
    serpapi_link: Optional[str] = None
    watching: Optional[int] = None
    live: Optional[bool] = None
    channel: Optional[Channel] = None
    description: Optional[str] = None
    extensions: Optional[list[str]] = None
    thumbnail: Optional[Thumbnail] = None


class ShortVideoResult(BaseModel):
    """
    Youtube short video result model
    """

    title: Optional[str] = None
    link: Optional[str] = None
    thumbnail: Optional[str] = None
    views_original: Optional[str] = None
    views: Optional[int] = None
    video_id: Optional[str] = None


class VideoSearchResults(BaseModel):
    """
    Youtube search results model
    """

    video_results: Optional[list[VideoSearchResult]] = None
    shorts_results: Optional[list[ShortVideoResult]] = None
    people_also_watched: Optional[list[VideoSearchResult]] = None
