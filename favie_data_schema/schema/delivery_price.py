from datetime import date, datetime, time
from decimal import Decimal
from enum import Enum
from typing import Dict, List, Optional, Union
from uuid import UUID

from pydantic import BaseModel, Field


class AttributeItem(BaseModel):
    title: Optional[str] = None
    value: Optional[str] = None
