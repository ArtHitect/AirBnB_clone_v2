#!/usr/bin/python3
"""
Unit tests for the Review model.
"""

from tests.test_models.test_base_model import TestBaseModel
from models.review import Review

class TestReview(TestBaseModel):
    """
    Test class for the Review model.
    """

    def __init__(self, *args, **kwargs):
        """Initializes the test class."""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """
        Test case to check the data type of the 'place_id' attribute in the Review model.
        """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """
        Test case to check the data type of the 'user_id' attribute in the Review model.
        """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """
        Test case to check the data type of the 'text' attribute in the Review model.
        """
        new = self.value()
        self.assertEqual(type(new.text), str)
