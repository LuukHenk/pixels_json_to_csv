"""Handles files"""

from json import load
from pathlib import Path


def load_json(file_path: Path) -> any:
    """Loads a json file
    Arg - file_path (Path): The path to the json file
    """
    with open(file_path) as json_file:
        data = load(json_file)
    return data


def write_file(file_path: Path, data: str):
    """Writes data to a file
    Arg - file_path (Path): The path of the file to be saved
    Arg - data (str): The data to be saved
    """
    with open(file_path, "w") as file_to_save:
        file_to_save.write(data)
        print(f"File '{file_path}' written")
