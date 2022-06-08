"""Tests the pixel model"""

from unittest import TestCase, main

from pixels_data_conversion.models.pixel import Pixel, Tag


class TestFileHandling(TestCase):
    """Tests the pixel model"""

    def test_pixel_initialization(self):
        """Test the initialization of the Pixel model"""
        pixel = Pixel()
        self.assertEqual(pixel.tags, [])

    @staticmethod
    def test_tag_initialization():
        """Test the initialization of the Tag model"""
        _ = Tag(name="name", value="value")


if __name__ == "__main__":
    main()
