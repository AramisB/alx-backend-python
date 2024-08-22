#!/usr/bin/env python3
"""
Create a TestAccessNestedMap class that inherits from unittest.TestCase.
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json
from unittest import mock


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

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self,
                                         nested_map, path, exception):
        """
        Test that access_nested_map is working
        """
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Tests for the get_json function
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
        ])
    def test_get_json(self, test_url, test_payload):
        """
        Test that get_json is working
        """
        with mock.patch('utils.requests.get') as mocked_get:
            mocked_get.return_value.json.return_value = test_payload
            self.assertEqual(get_json(test_url), test_payload)
            mocked_get.assert_called_once_with(test_url)
