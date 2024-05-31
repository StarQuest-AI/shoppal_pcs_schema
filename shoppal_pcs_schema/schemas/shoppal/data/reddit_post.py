from datetime import date, datetime, time
from decimal import Decimal
from enum import Enum
from typing import Dict, List, Optional, Union
from uuid import UUID

from pydantic import BaseModel, Field


class RedditPost(BaseModel):
    id: str
    type_name: str
    oid: str
    uid: str
    url: str
    upvotes_count: str
    comments_count: str
    creation_time: str
    json_data: str
    crawl_time: str
