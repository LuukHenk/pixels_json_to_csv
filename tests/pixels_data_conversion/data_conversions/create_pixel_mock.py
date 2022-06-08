"""Creates a pixel mock for the test files"""

from typing import List
from unittest.mock import MagicMock
from pixels_data_conversion.models.pixel import Pixel, Tag

INPUT_TABLE = [
    {
        "date": "2022-05-24",
        "entries": [
            {
                "type": "Mood",
                "value": 5,
                "notes": "",
                "isHighlighted": False,
                "tags": [
                    {"type": "People", "entries": ["None"]},
                    {"type": "Happyness", "entries": ["6.7"]},
                ],
            }
        ],
    }
]
PIXELS_TAG_NAMES = ["Happyness", "People", "date", "notes", "rating"]
PIXELS_TAG_VALUES = ["6.7", "None", "2022-05-24", "", "5"]
PIXELS_CSV_OUTPUT = 'Happyness,People,date,notes,rating\n6.7,None,2022-05-24,"Hi",5\n'


def create_pixel_mock() -> MagicMock:
    """
    Returns a mock of the pixels model which should be converatable to PIXELS_OUTPUT"""
    pixel = MagicMock(Pixel)
    pixel.tags = __create_pixel_tags()
    return pixel


def __create_pixel_tags() -> List[MagicMock]:
    tags = []
    for tag_name, tag_value in zip(PIXELS_TAG_NAMES, PIXELS_TAG_VALUES):
        tag = MagicMock(Tag)
        tag.name = tag_name
        tag.value = tag_value
        tags.append(tag)
    return tags
