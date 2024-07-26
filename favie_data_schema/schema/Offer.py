from pydantic import BaseModel
from typing import List, Dict, Optional, Union
from delivery_price import DeliveryPrice


class Delivery(BaseModel):
    fulfilled_by_platform: Optional[bool] = None
    countdown: Optional[str] = None
    comments: Optional[str] = None
    price: Optional[DeliveryPrice] = None
