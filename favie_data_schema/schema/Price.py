
from datetime import date, datetime, time
from decimal import Decimal
from enum import Enum
from typing import List, Optional, Dict, Union
from uuid import UUID

from pydantic import BaseModel, Field


class Price(BaseModel):
    lower_value: Optional[int] = None
    upper_value: Optional[int] = None
    value: Optional[int] = None
    currency: Optional[str] = None
    updates_at: Optional[str] = None
