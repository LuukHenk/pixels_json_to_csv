"""Main file of the pixels simplifier, which combines the other files in this folder
Used to convert a pixels json output (pixels v4.3.2) to a csv file
"""

from pathlib import Path
from typing import Optional

from lib.data_conversions.json_file_to_pixels import json_file_to_pixels
from lib.data_conversions.pixels_to_csv import pixels_to_csv


def pixels_json_to_csv(
    json_file_path: Path,  # pylint:disable=bad-continuation
    csv_file_path: Optional[Path] = None,  # pylint:disable=bad-continuation
) -> None:
    """Convert a complex pixels json file to a csv file
    Arg - json_file_path (Path): The path to the json file to be loaded
    Optional - csv_file_path (Path): The saving path of the csv file.
        The csv will be written to the same folder as the json file if the path is not
        given
    """
    csv_file_path = (
        csv_file_path if csv_file_path else __generate_csv_file_path(json_file_path)
    )
    pixels_to_csv(json_file_to_pixels(json_file_path), csv_file_path)


def __generate_csv_file_path(file_path: Path) -> Path:
    """Replaces the file path its extensions with .csv
    Arg - file_path (Path): The file path
    Returns (Path): The file path with a .csv extension
    """
    return file_path.rename(file_path.with_suffix(".csv"))
