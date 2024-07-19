from datetime import datetime, timezone
from typing import Annotated, Optional

from pydantic import BaseModel, ConfigDict, Field
from pydantic.functional_validators import BeforeValidator

PyObjectId = Annotated[str, BeforeValidator(str)]


class SuccessResponse(BaseModel):
    """Success response model."""

    status: Optional[str] = "ok"


class NotFoundResponse(BaseModel):
    """Not found response model."""

    status: Optional[str] = "not found"


class BaseMixin(BaseModel):
    """Base model for all mongodb models."""

    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    created_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(tz=timezone.utc))
    updated_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(tz=timezone.utc))

    model_config = ConfigDict(use_enum_values=True, populate_by_name=True)
