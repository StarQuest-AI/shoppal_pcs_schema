# 管理后台相关 schema 定义在此处
from typing import Optional

from pydantic import BaseModel


class PersonalConfig(BaseModel):
    """落地页个性化配置"""

    source_id: str
    redirect_url: str
    banner: str
    click_url: Optional[str] = None
    show: Optional[int] = 0
