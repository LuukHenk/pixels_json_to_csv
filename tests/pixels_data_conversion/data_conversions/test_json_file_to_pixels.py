"""Tests the json to pixels conversion"""

from unittest import TestCase, main
from unittest.mock import patch

from pixels_data_conversion.data_conversions.json_file_to_pixels import (
    json_file_to_pixels,
)
from create_pixel_mock import INPUT_TABLE, PIXELS_TAG_NAMES, PIXELS_TAG_VALUES


FILE_PATH = "pixels_data_conversion.data_conversions.json_file_to_pixels"


class TestJsonToPixels(TestCase):
    """Tests the json to pixels conversion"""

    @patch(f"{FILE_PATH}.load_json")
    def test_json_to_pixels(self, load_json_patch):
        """Tests the json to pixels module"""
        # Arrange
        path = "path"
        load_json_patch.return_value = INPUT_TABLE
        # Act
        pixels = json_file_to_pixels(path)
        pixel = pixels[0]
        names = sorted([tag.name for tag in pixel.tags])
        values = sorted([tag.value for tag in pixel.tags])
        # Assert
        self.assertEqual(1, len(pixels))
        self.assertEqual(sorted(PIXELS_TAG_NAMES), names)
        self.assertAlmostEqual(sorted(PIXELS_TAG_VALUES), values)


if __name__ == "__main__":
    main()
