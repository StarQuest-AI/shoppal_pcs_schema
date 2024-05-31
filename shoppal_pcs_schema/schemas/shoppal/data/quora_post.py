from datetime import date, datetime, time
from decimal import Decimal
from enum import Enum
from typing import Dict, List, Optional, Union
from uuid import UUID

from pydantic import BaseModel, Field


class QuoraPost(BaseModel):
    id: str
    type_name: str
    id_str: str
    oid: str
    uid: str
    url: str
    views_count: str
    upvotes_count: str
    shares_count: str
    comments_count: str
    creation_time: str
    updated_time: str
    cursor: str
    json_raw: str
    crawl_time: str
