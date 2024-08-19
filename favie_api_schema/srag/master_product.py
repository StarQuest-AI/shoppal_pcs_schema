"""
master product schema
"""

from typing import Optional

from pydantic import BaseModel

from favie_api_schema.schemas.product_detail import (ProductDetail,
                                                       ProductPlatForm)


class MasterProduct(BaseModel):
    """
    master product model
    """

    class ExternalInfo(BaseModel):
        """
        external info model
        """

        platform: str = ProductPlatForm.AMAZON.value
        id: str
        url: str
        detail: Optional[ProductDetail]

    class InnerInfo(BaseModel):
        """
        inner info model
        """

        detail: Optional[ProductDetail]

    global_id: str
    inner_info: InnerInfo
    external_info: list[ExternalInfo]
