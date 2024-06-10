"""
srag response pydantic
"""

from shoppal_pcs_schema.schemas.common_search_result import GoogleSearchResult


class CitationResponse(GoogleSearchResult):
    """citation response"""

    cover_images: list[str]
