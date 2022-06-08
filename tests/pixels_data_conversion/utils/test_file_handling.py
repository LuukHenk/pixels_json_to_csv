"""Tests the file handling file"""

from unittest import TestCase, main
from unittest.mock import patch
from pathlib import Path

from pixels_data_conversion.utils.file_handling import (
    load_json,
    replace_suffix,
    validate_file,
    write_file,
)

FILE_PATH = "pixels_data_conversion.utils.file_handling"


class TestFileHandling(TestCase):
    """Tests the file handling file"""

    @patch(f"{FILE_PATH}.load")
    @patch("builtins.open")
    def test_load_json(self, open_patch, load_patch):
        """Test loading a json file"""
        # Arrange
        input_path = "path"
        expected_out_data = "data"
        load_patch.return_value = expected_out_data
        # Act
        out_data = load_json(input_path)
        # Assert
        load_patch.assert_called_once()
        open_patch.assert_called_once_with(input_path)
        self.assertEqual(expected_out_data, out_data)

    @staticmethod
    @patch("builtins.open")
    def test_write_file(open_patch):
        """Test writing a file"""
        # Arrange
        input_path = "path"
        input_data = "data"
        # Act
        write_file(input_path, input_data)
        # Assert
        open_patch.assert_called_once_with(input_path, "w")

    @patch(f"{FILE_PATH}.Path")
    def test_validate_file_invalid_file(self, path_patch):
        """Test file validation when the file is invalid"""
        # Arrange
        path_patch.is_file().return_value = False
        # Act & assert
        self.assertRaises(ValueError, validate_file, path_patch, "")

    @patch(f"{FILE_PATH}.Path")
    def test_validate_file_invalid_suffix(self, path_patch):
        """Test file validation when the suffix is invalid"""
        # Arrange
        path_patch.is_file.return_value = True
        # Act & Assert
        self.assertRaises(ValueError, validate_file, path_patch, ".py")

    @staticmethod
    @patch(f"{FILE_PATH}.Path")
    def test_validate_file_valid_file_and_valid_suffix(path_patch):
        """Test file validation when the file and suffix are valid"""
        # Arrange
        suffix = ".py"
        path_patch.is_file.return_value = True
        path_patch.suffix = suffix
        # Act & Assert
        validate_file(path_patch, suffix)  # No error should be raised

    def test_replace_suffix(self):
        """Tests the replace suffix function"""
        # Arrange
        path = Path("home/file.json")
        new_suffix = ".csv"
        expected_new_file = path.parent / f"{path.stem}{new_suffix}"
        # Act
        new_file = replace_suffix(path, new_suffix)
        # Assert
        self.assertEqual(expected_new_file, new_file)


if __name__ == "__main__":
    main()
