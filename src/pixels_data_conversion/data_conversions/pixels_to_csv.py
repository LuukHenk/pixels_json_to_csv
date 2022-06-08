"""Converts the pixels datamodel data to a csv format"""


from copy import deepcopy
from pathlib import Path
from typing import Dict, List, Set

from pixels_data_conversion.models.pixel import Pixel
from pixels_data_conversion.utils.file_handling import write_file


def pixels_to_csv(pixels: List[Pixel], csv_file_path: Path) -> None:
    """Convert pixels data to a csv file
    Arg - pixels (List[Pixel]): A list of pixels to be converted
    Arg - csv_file_path (Path): The path to the csv file to be saved
    """
    headers = __get_headers(pixels)
    write_file(
        csv_file_path, __generate_csv(__structure_pixels_data(pixels, headers), headers)
    )


def __structure_pixels_data(pixels: List[Pixel], headers: Set[str]) -> Dict[str, str]:
    """Structure the pixels data to a row-column structure"""
    data = {header: [] for header in headers}
    for pixel in pixels:
        headers_to_cover = deepcopy(headers)
        for tag in pixel.tags:
            data[tag.name].append(tag.value)
            headers_to_cover.remove(tag.name)
        for header in headers_to_cover:
            data[header].append("")
    return data


def __get_headers(pixels: List[Pixel]) -> Set[str]:
    return {tag.name for pixel in pixels for tag in pixel.tags}


def __generate_csv(data: Dict[str, str], headers: Set[str]) -> str:
    seperator = ","
    fixated_headers = sorted(list(headers))
    csv = f"{seperator.join(fixated_headers)}\n"
    for row in range(len(next(iter(data.values())))):
        csv += f"{seperator.join([data[header][row] for header in fixated_headers])}\n"
    return csv
