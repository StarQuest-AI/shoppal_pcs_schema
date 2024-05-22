
from datetime import date, datetime, time
from decimal import Decimal
from enum import Enum
from typing import List, Optional, Dict, Union
from uuid import UUID

from pydantic import BaseModel, Field


class Review(BaseModel):
    product_id: str
    url: str
    raw_html: Optional[str]
    parsed: Optional[str]
