import os

def get_project_root() -> str:
    return os.path.dirname(os.path.abspath(__file__))
