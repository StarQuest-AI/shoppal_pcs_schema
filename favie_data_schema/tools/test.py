import re
from typing import List, Optional,Union,ForwardRef


def extract_type_name(type_str):
    # 匹配 Optional[List['...']]
    match = re.search(r"Optional\[List\['(.+?)'\]\]", type_str)
    if match:
        return f"List[{match.group(1).split('.')[-1]}]"
    
    # 匹配 Optional[ForwardRef('...')]
    match = re.search(r"Optional\[ForwardRef\('(.+?)'\)\]", type_str)
    if match:
        return f"Optional[{match.group(1).split('.')[-1]}]"
    
    # 匹配 List[ForwardRef('...')]
    match = re.search(r"List\[ForwardRef\('(.+?)'\)\]", type_str)
    if match:
        return f"List[{match.group(1).split('.')[-1]}]"
    
    # 匹配 ForwardRef('...')
    match = re.search(r"ForwardRef\('(.+?)'\)", type_str)
    if match:
        return match.group(1).split(".")[-1]

    # 匹配 List['...']
    match = re.search(r"List\['(.+?)'\]", type_str)
    if match:
        return f"List[{match.group(1).split('.')[-1]}]"

    # 匹配 Optional[List[...]]
    match = re.search(r"Optional\[List\[(.+?)\]\]", type_str)
    if match:
        return f"List[{match.group(1)}]"

    # 匹配 Optional[...]
    match = re.search(r"Optional\[(.+?)\]", type_str)
    if match:
        return f"Optional[{match.group(1)}]"

    # 匹配 List[...]
    match = re.search(r"List\[(.+?)\]", type_str)
    if match:
        return f"List[{match.group(1)}]"

    # 匹配 '...'
    match = re.search(r"'\s*(.+?)\s*'", type_str)
    if match:
        return match.group(1).split(".")[-1]
    
    # 如果没有匹配，返回原始字符串
    return type_str

# 示例用法
print(extract_type_name("Optional[List['module.TypeName']]"))  # 输出: List[TypeName]
print(extract_type_name("Optional[ForwardRef('module.TypeName')]"))  # 输出: Optional[TypeName]
print(extract_type_name("List[ForwardRef('module.TypeName')]"))  # 输出: List[TypeName]
print(extract_type_name("ForwardRef('module.TypeName')"))  # 输出: TypeName
print(extract_type_name("List['module.TypeName']"))  # 输出: List[TypeName]
print(extract_type_name("'module.TypeName'"))  # 输出: TypeName
print(extract_type_name("Optional[List[str]]"))  # 输出: List[str]
print(extract_type_name("Optional[str]"))  # 输出: Optional[str]
print(extract_type_name("List[str]"))  # 输出: List[str]
print(extract_type_name("int"))  # 输出: int

test = ForwardRef('hello')

print(str(test))
print(str.__name__)