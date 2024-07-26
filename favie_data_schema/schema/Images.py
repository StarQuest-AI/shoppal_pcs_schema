from datetime import date, datetime, time
from decimal import Decimal
from enum import Enum
from typing import Dict, List, Optional, Union
from uuid import UUID

from pydantic import BaseModel, Field


class Images(BaseModel):
    main_image: Optional[str] = None
    images: List[str] = []
