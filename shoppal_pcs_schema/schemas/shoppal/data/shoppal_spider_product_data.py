import uuid
from datetime import datetime
from enum import IntEnum
from typing import Optional

from pydantic import BaseModel, Field

from shoppal_pcs_schema.schemas.shoppal.data.rainforest_product_detail import \
    RainforestProductDetail


class Source(IntEnum):
    # 未知
    UNKNOWN = 0
    # 爬虫爬取页面
    SPIDER = 1
    # 数据服务写入
    DATA_SERVICE = 2
    # 爬虫调用RF API获取
    SPIDER_CALL_RF_API = 3
    # 离线数据修复
    OFFLINE = 4


class ShoppalSpiderProductData(BaseModel):
    id: str = uuid.uuid1().hex  # UUID1
    url: str  # URL
    host: str  # 商品所在网站的域名，比如：www.amazon.com
    product_id: Optional[str] = None  # 商品ID，比如：Amazon为ASIN: B0CBLKS51N
    product_title: Optional[str] = None  # 商品Title
    parser_name: Optional[str] = None  # used for spider
    source: Optional[Source] = 0  # 数据来源
    raw_result: Optional[str] = (
        None  # 原始抓取结果，如果为Rainforest则为API则为Response的json结果，如果为自研爬虫则为原始html
    )
    crawl_result: Optional[RainforestProductDetail] = None  # 商品解析结果，存储为JSON格式，遵循RainForest的数据模型
    crawl_time: Optional[datetime] = datetime.now()  # 爬虫写入时间
    update_time: Optional[datetime] = datetime.now()  # 数据更新时间
