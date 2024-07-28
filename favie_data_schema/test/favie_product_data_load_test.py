import json
from pydantic import ValidationError
from favie_data_schema import FavieProduct

def test_parse_json():
    # 读取 JSON 文件
    with open('/Users/pangbaohui/workspace/shoppal_pcs_schema/favie_data_schema/data/favie_product.json', 'r') as f:
        data = json.load(f)
    try:
        # 将 JSON 数据解析为 Pydantic 对象
        product = FavieProduct(**data)
        print(product.json())
    except ValidationError as e:
        print("Validation error:", e)

# 调用测试函数
if __name__ == "__main__":
    test_parse_json()