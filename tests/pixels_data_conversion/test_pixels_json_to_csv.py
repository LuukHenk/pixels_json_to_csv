"""Test file for the pixels json to csv its main function"""

from pathlib import Path
from unittest import TestCase, main
from unittest.mock import patch
from pixels_data_conversion.pixels_json_to_csv import (
    pixels_json_to_csv,
    CSV_SUFFIX,
    JSON_SUFFIX,
)

PIXELS_JSON_TO_CSV_PATH = "pixels_data_conversion.pixels_json_to_csv"

JSON_FILE_PATH = Path("/abc/def.json")
CSV_FILE_PATH = Path("/abc/def.csv")


class TestPixelsJsonToCsv(TestCase):
    """Tests the pixels json to csv class"""

    def test_suffixes(self):
        """Test the global suffixes"""
        self.assertEqual(CSV_SUFFIX, ".csv")
        self.assertEqual(JSON_SUFFIX, ".json")

    @staticmethod
    @patch(f"{PIXELS_JSON_TO_CSV_PATH}.validate_file")
    @patch(f"{PIXELS_JSON_TO_CSV_PATH}.replace_suffix")
    @patch(f"{PIXELS_JSON_TO_CSV_PATH}.pixels_to_csv")
    @patch(f"{PIXELS_JSON_TO_CSV_PATH}.json_file_to_pixels")
    def test_pixels_json_to_csv_no_csv(
        json_file_to_pixels_patch,
        pixels_to_csv_patch,
        replace_suffix_patch,
        validate_file_patch,
    ):
        """Test the main function when there is no csv file"""
        # Arrange
        csv_file_path = "all.csv"
        replace_suffix_patch.return_value = csv_file_path
        # Act
        pixels_json_to_csv(JSON_FILE_PATH)
        # Assert
        validate_file_patch.assert_called_once_with(JSON_FILE_PATH, JSON_SUFFIX)
        replace_suffix_patch.assert_called_once_with(JSON_FILE_PATH, CSV_SUFFIX)
        json_file_to_pixels_patch.assert_called_once_with(JSON_FILE_PATH)
        pixels_to_csv_patch.assert_called_once_with(
            json_file_to_pixels_patch(), csv_file_path
        )

    @staticmethod
    @patch(f"{PIXELS_JSON_TO_CSV_PATH}.validate_file")
    @patch(f"{PIXELS_JSON_TO_CSV_PATH}.replace_suffix")
    @patch(f"{PIXELS_JSON_TO_CSV_PATH}.pixels_to_csv")
    @patch(f"{PIXELS_JSON_TO_CSV_PATH}.json_file_to_pixels")
    def test_pixels_json_to_csv_with_json_and_csv(
        json_file_to_pixels_patch,
        pixels_to_csv_patch,
        replace_suffix_patch,
        validate_file_patch,
    ):
        """Test the main function"""
        # Act
        pixels_json_to_csv(JSON_FILE_PATH, CSV_FILE_PATH)
        # Assert
        validate_file_patch.assert_called_once_with(JSON_FILE_PATH, JSON_SUFFIX)
        replace_suffix_patch.assert_not_called()
        json_file_to_pixels_patch.assert_called_once_with(JSON_FILE_PATH)
        pixels_to_csv_patch.assert_called_once_with(
            json_file_to_pixels_patch(), CSV_FILE_PATH
        )


if __name__ == "__main__":
    main()
