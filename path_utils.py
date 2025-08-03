import os

project_root = os.path.dirname(os.path.abspath(__file__))

def get_image_path(file_name: str) -> str:
    return os.path.join(project_root, "Images", file_name)

def get_root_path(file_name: str) -> str:
    return os.path.join(project_root, file_name)    
