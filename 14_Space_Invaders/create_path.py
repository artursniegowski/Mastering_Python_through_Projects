# function for creating a path to the specific files resideing in this project
import os
from pathlib import Path

def return_path(sub_folder_name: str, file_name: str) -> Path:
    """function for resolving the path for the given file name
    """
    assert isinstance(sub_folder_name, str), "Error: sub_folder_name has to be of type string!"
    assert isinstance(file_name, str), "Error: file_name has to be of type string!"
    assert len(sub_folder_name.strip())>2 and len(file_name.strip())>2, "Error: sub_folder_name and file_name have to be at least 3 characters long each!"

    return (Path(__file__).parent / os.path.join(sub_folder_name,file_name)).resolve()