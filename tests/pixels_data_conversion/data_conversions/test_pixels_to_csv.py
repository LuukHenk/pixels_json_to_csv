"""Tests the pixels to csv conversion"""

from unittest import TestCase, main
from unittest.mock import patch

from pixels_data_conversion.data_conversions.pixels_to_csv import pixels_to_csv
from create_pixel_mock import create_pixel_mock, PIXELS_CSV_OUTPUT


FILE_PATH = "pixels_data_conversion.data_conversions.pixels_to_csv"


class TestPixelsToCsv(TestCase):
    """Tests the pixels to csv conversion"""

    def test_pixels_to_csv(self):
        """Tests the pixels_to_csv module"""
        # Arrange
        pixels = [create_pixel_mock()]
        csv_file_path = "home/file.csv"
        # Act
        with patch(f"{FILE_PATH}.write_file") as write_file_patch:
            pixels_to_csv(pixels, csv_file_path)
        # Assert
        csv_output = write_file_patch.mock_calls[0].args
        self.assertEqual(csv_file_path, csv_output[0])
        self.assertEqual(PIXELS_CSV_OUTPUT, csv_output[1])


if __name__ == "__main__":
    main()
