"""
srag common pydantic
"""

from typing import Optional

from shoppal_pcs_schema.schemas.common_search_result import GoogleSearchResult


class CitationResponse(GoogleSearchResult):
    """citation response"""

    cover_images: Optional[list[str]]
