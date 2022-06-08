"""Main file of the pixels simplifier, which combines the other files in this folder
Used to convert a pixels json output (pixels v4.3.2) to a csv file
"""

from pathlib import Path
from typing import Optional, Union

from pixels_data_conversion.data_conversions.json_file_to_pixels import (
    json_file_to_pixels,
)
from pixels_data_conversion.data_conversions.pixels_to_csv import pixels_to_csv
from pixels_data_conversion.utils.file_handling import validate_file, update_file_suffix

JSON_SUFFIX = ".json"
CSV_SUFFIX = ".csv"


def pixels_json_to_csv(
    json_file_path: Union[Path, str],  # pylint:disable=bad-continuation
    csv_file_path: Optional[Union[Path, str]] = None,  # pylint:disable=bad-continuation
):
    """Convert a complex pixels json file to a csv file
    Arg - json_file_path (Path): The path to the json file to be loaded
    Optional - csv_file_path (Path): The saving path of the csv file.
        The csv will be written to the same folder as the json file if the path is not
        given
    """
    json_file_path = Path(json_file_path)
    validate_file(json_file_path, JSON_SUFFIX)

    csv_file_path = (
        Path(csv_file_path)
        if csv_file_path
        else update_file_suffix(json_file_path, CSV_SUFFIX)
    )
    pixels_to_csv(json_file_to_pixels(json_file_path), csv_file_path)
