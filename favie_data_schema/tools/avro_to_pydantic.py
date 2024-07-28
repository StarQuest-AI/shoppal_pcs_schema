import json
import os
from fastavro.schema import load_schema
from typing import Dict, Any, List
from pydantic import BaseModel

def avro_type_to_python_type(avro_type: Any, namespace: str, imports: set) -> str:
    if isinstance(avro_type, str):
        return {
            "string": "str",
            "int": "int",
            "long": "int",
            "float": "float",
            "double": "float",
            "boolean": "bool",
            "bytes": "bytes"
        }.get(avro_type, avro_type)
    elif isinstance(avro_type, dict):
        if avro_type["type"] == "array":
            return f"List[{avro_type_to_python_type(avro_type['items'], namespace, imports)}]"
        elif avro_type["type"] == "map":
            return f"Dict[str, {avro_type_to_python_type(avro_type['values'], namespace, imports)}]"
        elif avro_type["type"] == "record":
            return avro_type["name"]
    elif isinstance(avro_type, list):
        # Handle union types, e.g., ["null", "string"] -> Optional[str]
        non_null_types = [t for t in avro_type if t != "null"]
        if len(non_null_types) == 1:
            return f"Optional[{avro_type_to_python_type(non_null_types[0], namespace, imports)}]"
        else:
            return f"Union[{', '.join(avro_type_to_python_type(t, namespace, imports) for t in avro_type)}]"

    # Handle external references
    if "." in avro_type:
        imports.add(avro_type)
        return avro_type.split(".")[-1]

    return "Any"

def generate_pydantic_model(schema: Dict[str, Any], indent: int = 0, namespace: str = "", imports: set = None) -> str:
    if imports is None:
        imports = set()
    indent_str = " " * indent
    if schema["type"] == "record":
        fields_str = "\n".join(
            f"{indent_str}    {field['name']}: {avro_type_to_python_type(field['type'], namespace, imports)} = None"
            for field in schema["fields"]
        )
        return (
            f"{indent_str}class {schema['name']}(BaseModel):\n"
            f"{fields_str}\n"
        )

def generate_pydantic_models(schema: Dict[str, Any], loaded_schemas: Dict[str, Any], namespace: str = "", imports: set = None) -> str:
    if imports is None:
        imports = set()
    models = []
    if schema["type"] == "record":
        for field in schema["fields"]:
            if isinstance(field["type"], dict) and field["type"]["type"] == "record":
                models.append(generate_pydantic_model(field["type"], indent=0, namespace=namespace, imports=imports))
            elif isinstance(field["type"], str) and field["type"] in loaded_schemas:
                # Handle external references
                models.append(generate_pydantic_model(loaded_schemas[field["type"]], indent=0, namespace=namespace, imports=imports))
        models.append(generate_pydantic_model(schema, indent=0, namespace=namespace, imports=imports))
    return "\n".join(models), imports

def load_all_schemas(base_path: str, schema_files: Dict[str, str]) -> Dict[str, Dict[str, Any]]:
    loaded_schemas = {}
    for name, path in schema_files.items():
        full_path = os.path.join(base_path, path)
        with open(full_path, "r") as f:
            schema = json.load(f)
            loaded_schemas[f"{schema['namespace']}.{schema['name']}"] = schema
    return loaded_schemas

if __name__ == "__main__":
    base_path = "/Users/pangbaohui/workspace/shoppal_pcs_schema/favie_data_schema/avsc"
    schema_files: List[str] = [
        "delivery.avsc",
        "delivery_price.avsc"
    ]
    
        
    loaded_schemas: Dict[str, Dict[str, Any]] = load_all_schemas(base_path, schema_files)
    main_schema = loaded_schemas["favie.data.Delivery"]

    pydantic_code, imports = generate_pydantic_models(main_schema, loaded_schemas)

    import_statements = "\n".join([f"from {namespace} import {name}" for namespace, name in (imp.rsplit(".", 1) for imp in imports)])

    pydantic_code = (
        "from pydantic import BaseModel\n"
        "from typing import List, Dict, Optional, Union\n"
        + import_statements + "\n\n"
        + pydantic_code
    )

    output_path = "/Users/pangbaohui/workspace/shoppal_pcs_schema/favie_data_schema/schema/Offer.py"
    with open(output_path, "w") as f:
        f.write(pydantic_code)

    print(f"Pydantic models have been generated and saved to {output_path}")