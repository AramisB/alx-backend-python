#!/usr/bin/env python3
"""
Create a TestAccessNestedMap class that inherits from unittest.TestCase.
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    Tests that the method returns what it is supposed to.
    Decorate the method with @parameterized.expand
    to test the function for inputs
    For each of these inputs, test with assertEqual
    that the function returns the expected result.
    The body of the test method should not be longer than 2 lines.
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test that access_nested_map is working
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)
