"""
srag response pydantic
"""

from favie_api_schema.schemas.common_search_result import GoogleSearchResult


class CitationResponse(GoogleSearchResult):
    """citation response"""

    cover_images: list[str]
