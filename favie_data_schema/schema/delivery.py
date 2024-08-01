from typing import List, Optional
from pydantic import BaseModel, Field

class DeliveryPrice(BaseModel):
    raw: Optional[str] = None
    currency: Optional[str] = None
    value: Optional[int] = None
    is_free: Optional[bool] = None

class Delivery(BaseModel):
    fulfilled_by_platform: Optional[bool] = None
    countdown: Optional[str] = None
    comments: Optional[str] = None
    price0: List[DeliveryPrice] = None
    price1: List[DeliveryPrice] = None
