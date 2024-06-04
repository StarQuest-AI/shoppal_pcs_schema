
from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field
from shoppal_pcs_schema.schemas.shoppal.data.rainforest_product_detail import RainforestProductDetail

class ShoppalSpiderProductData(BaseModel):
    id: str # UUID1
    url: str # URL
    host: str # 商品所在网站的域名，比如：www.amazon.com
    product_id: Optional[str] # 商品ID，比如：Amazon为ASIN: B0CBLKS51N
    spider: Optional[str] = None # used for spider
    source: Optional[int] = 0 # 数据来源，0：未知，1：Spider，2: DataService
    crawl_result: Optional[RainforestProductDetail] # 商品解析结果，存储为JSON格式，遵循RainForest的数据模型
    crawl_result_md5: Optional[str] # 商品解析结果MD5
    crawl_time: datetime # 爬虫写入时间
    update_time: datetime # 数据更新时间
