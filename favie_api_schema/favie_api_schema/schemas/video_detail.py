"""
youtube video detail schemas
"""

# pylint: disable=too-few-public-methods
from typing import Optional

from pydantic import BaseModel


class VideoBaseInfos(BaseModel):
    """
    base infos model
    """

    class Channel(BaseModel):
        """
        channel model
        """

        name: Optional[str] = None
        thumbnail: Optional[str] = None
        link: Optional[str] = None
        subscribers: Optional[str] = None
        extracted_subscribers: Optional[int] = None

    class Description(BaseModel):
        """
        description model
        """

        content: Optional[str] = None
        links: Optional[list[dict]] = None

    class Chapter(BaseModel):
        """
        chapter model
        """

        title: Optional[str] = None
        thumbnail: Optional[str] = None
        time_start: Optional[int] = None

    title: Optional[str] = None
    link: Optional[str] = None
    thumbnail: Optional[str] = None
    cover_image: Optional[str] = None
    channel: Optional[Channel] = None
    views: Optional[str] = None
    extracted_views: Optional[int] = None
    likes: Optional[str] = None
    published_date: Optional[str] = None
    description: Optional[Description] = None
    chapters: Optional[list[Chapter]] = None
    images: Optional[list[str]] = None


class RelatedVideo(BaseModel):
    """
    youtube related video model
    """

    class Thumbnail(BaseModel):
        """
        thumbnail model
        """

        static: Optional[str] = None
        rich: Optional[str] = None

    class Channel(BaseModel):
        """
        channel model
        """

        name: Optional[str] = None
        link: Optional[str] = None
        thumbnail: Optional[str] = None
        verified: Optional[bool] = None

    video_id: Optional[str] = None
    link: Optional[str] = None
    serpapi_link: Optional[str] = None
    thumbnail: Optional[Thumbnail] = None
    title: Optional[str] = None
    published_date: Optional[str] = None
    views: Optional[str] = None
    extracted_views: Optional[int] = None
    length: Optional[str] = None
    channel: Optional[Channel] = None


class Subtitle(BaseModel):
    """
    subtitle model
    """

    content: Optional[str] = None
    link: Optional[str] = None
    start_time: Optional[int] = None  #  in seconds
    end_time: Optional[int] = None


class VideoDetail(BaseModel):
    """
    youtube video detail model
    """

    base_infos: Optional[VideoBaseInfos] = None
    related_videos: Optional[list[RelatedVideo]] = None
    comment_count: Optional[int] = 0
    subtitle: Optional[list[Subtitle]] = None
