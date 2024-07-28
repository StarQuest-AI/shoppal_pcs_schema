import os

def get_files_in_directory(directory):
    try:
        # 获取指定目录中的所有文件和子目录
        files_and_dirs = os.listdir(directory)

        # 过滤出文件
        files = [f for f in files_and_dirs if os.path.isfile(os.path.join(directory, f))]
        
        return files
    except Exception as e:
        print(f"Error accessing directory {directory}: {e}")
        return []

# 示例用法
directory_path = '/Users/pangbaohui/workspace/shoppal_pcs_schema/favie_data_schema/avsc'
files = get_files_in_directory(directory_path)
print(files)