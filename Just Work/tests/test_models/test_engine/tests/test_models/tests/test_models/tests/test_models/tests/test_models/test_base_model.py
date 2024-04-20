#!/usr/bin/python3
"""
Unit tests for the BaseModel class.
"""

from models.base_model import BaseModel
import unittest
import datetime
import json
import os

class TestBaseModel(unittest.TestCase):
    """
    Test class for the BaseModel model.
    """

    def __init__(self, *args, **kwargs):
        """Initializes the test class."""
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """Set up any necessary resources for the test cases."""
        pass

    def tearDown(self):
        """Clean up any resources created during the test cases."""
        try:
            os.remove('file.json')
        except:
            pass

    def test_default(self):
        """Test case to check if an instance of \
                BaseModel is created properly."""
        i = self.value()
        self.assertEqual(type(i), self.value)

    # Other test methods...
