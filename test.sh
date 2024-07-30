#!/bin/bash

echo "合并avro代码..."
python -m favie_data_schema.tools.combine_schemas_with_unique_define --source-directory="/Users/pangbaohui/workspace/shoppal_pcs_schema/favie_data_schema/avsc" --output-file="/Users/pangbaohui/workspace/shoppal_pcs_schema/favie_data_schema/avsc/combine_output/favie_product.avsc" --main-schema="favie.data.FavieProduct"
echo "合并avro代码结束"
echo "合并avro代码结束"

echo "转化合并后的代码..."
python -m favie_data_schema.tools.avro_to_pydantic --avsc="/Users/pangbaohui/workspace/shoppal_pcs_schema/favie_data_schema/avsc/combine_output/favie_product.avsc" --output-file="/Users/pangbaohui/workspace/shoppal_pcs_schema/favie_data_schema/schema/favie_product.py"
echo "转化合并后的代码结束"

# echo "数据加载测试..."
# python -m favie_data_schema.test.favie_product_data_load_test
# echo "数据加载测试结束"
