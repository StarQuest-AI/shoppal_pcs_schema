from typing import List, Optional
from pydantic import BaseModel, Field

class Images(BaseModel):
    main_image: Optional[str] = None
    images: List[str] = None

