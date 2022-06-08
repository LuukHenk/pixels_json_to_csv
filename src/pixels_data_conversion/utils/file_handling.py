"""Handles files"""

from json import load
from pathlib import Path


def load_json(file_path: Path) -> any:
    """Loads a json file
    Arg - file_path (Path): The path to the json file
    """
    with open(file_path, "r") as json_file:
        data = load(json_file)
    return data


def write_file(file_path: Path, data: str) -> None:
    """Writes data to a file. Lets the user know if the file is saved by printing
    Arg - file_path (Path): The path of the file to be saved
    Arg - data (str): The data to be saved
    """
    with open(file_path, "w") as file_to_save:
        file_to_save.write(data)
        print(f"File '{file_path}' written")


def validate_file(file_path: Path, expected_suffix: str) -> None:
    """Validates if an input file is a legit file and has the expected suffix.
    Raises value error if the suffix or the file is invalid
    Arg - file_path (Path):  the path to check
    Arg - expected_suffix (str): The expected suffix
    """
    if not file_path.is_file():
        raise ValueError(f"Invalid file path: {file_path}")
    if not file_path.suffix == expected_suffix:
        raise ValueError(f"File {file_path} must be of type {expected_suffix}")


def replace_suffix(file_path: Path, new_suffix: str) -> Path:
    """Replaces the file path its suffix with the new suffix
    Arg - file_path (Path): The file path
    Returns (Path): The file path with a new suffix
    """
    return file_path.parent / Path(f"{file_path.stem}{new_suffix}")
