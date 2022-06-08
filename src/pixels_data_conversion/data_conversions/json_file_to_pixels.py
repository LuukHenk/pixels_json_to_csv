"""Loads a pixels json file of pixels v4.3.2 and converts it to a python datamodel"""

from pathlib import Path
from typing import Dict, List

from pixels_data_conversion.utils.file_handling import load_json
from pixels_data_conversion.models.pixel import Pixel, Tag


def json_file_to_pixels(file_path: Path) -> List[Pixel]:
    """Convert a json file exported by the pixels app version 4.3.2.,
    to a python datamodel
    arg - file_path (Path): The path to the pixels json file
    returns (List[Pixel]): A list pixels
    """
    return __get_pixels(load_json(file_path))


def __get_pixels(pixels_json: Dict[str, any]) -> List[Pixel]:
    """Get Pixels from a pixels json output
    Arg - pixels_json (Dict[str, any]): A pixels json file of pixels v4.3.2
    Returns (List[Pixel]): A list of pixels
    """
    return [Pixel(tags=__get_pixel_tags(pixel_json)) for pixel_json in pixels_json]


def __get_pixel_tags(pixel_json: Dict[str, any]) -> List[Tag]:
    """Gets static and personalized pixel tags
    Arg - pixels_json (Dict[str, any]): A pixels json file of pixels v4.3.2
    Returns (List[Tag]): A list of pixel tags
    """
    tags = []
    try:
        tags.append(Tag(name="date", value=pixel_json["date"]))
        notes_json_entry = pixel_json["entries"][0]["notes"].replace("\n", "|")
        tags.append(Tag(name="notes", value=notes_json_entry))
        tags.append(Tag(name="rating", value=str(pixel_json["entries"][0]["value"])))
        for tag in pixel_json["entries"][0]["tags"]:
            tags.append(Tag(name=tag["type"], value="|".join(tag["entries"])))
    except KeyError as err:
        print(
            f"Missing static pixel entry {err}. Make sure you are using data of pixels version 4.3.2"  # pylint:disable=line-too-long
        )
    return tags
