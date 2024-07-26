import json

from fastavro.schema import load_schema


def validate_avro_schema(file_path):
    try:
        schema = load_schema(file_path)
        print(f"Schema {file_path} is valid.")
    except Exception as e:
        print(f"Schema {file_path} is invalid: {e}")


# 验证 Price Schema
validate_avro_schema("/Users/pangbaohui/workspace/shoppal_pcs_schema/favie_data_schema/avsc/images.avsc")
