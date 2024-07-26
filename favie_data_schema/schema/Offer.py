from typing import Dict, List, Optional, Union

from delivery_price import DeliveryPrice
from pydantic import BaseModel


class Delivery(BaseModel):
    fulfilled_by_platform: Optional[bool] = None
    countdown: Optional[str] = None
    comments: Optional[str] = None
    price: Optional[DeliveryPrice] = None
