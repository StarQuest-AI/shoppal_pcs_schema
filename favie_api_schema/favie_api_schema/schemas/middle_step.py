from typing import Literal, Optional, TypedDict

from favie_api_schema.schemas.product_detail import ProductDetail


class SearchOutput(TypedDict):
    """search output"""

    title: str = ""
    favicon: str = ""
    link: str = ""
    snippet: str = ""
    source: str = ""
    thumbnail: str = ""
    timestamp: str = ""
    other_info: dict = {}
    type: Literal["webpage", "youtube"] = ""
    raw_result: dict = {}


class MiddleStepPlan(TypedDict):
    """ " plan for middle step"""

    plan: list[str]


class MiddleStepResponse(TypedDict):
    """service middle step"""

    workflow_flow: Optional[MiddleStepPlan] = None
    search: Optional[list[SearchOutput]] = None
    search_detail: Optional[dict[str, str]] = None
    search_product: Optional[dict[str, ProductDetail]] = None  # ProductDetail is a pydantic model_dump()
