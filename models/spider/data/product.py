
from datetime import date, datetime, time
from decimal import Decimal
from enum import Enum
from typing import List, Optional, Dict, Union
from uuid import UUID

from pydantic import BaseModel, Field


class Platform(str, Enum):
    AMAZON = "AMAZON"
    EBAY = "EBAY"


class Product(BaseModel):
    product_id: str
    platform: Platform
    asin: Optional[str]
