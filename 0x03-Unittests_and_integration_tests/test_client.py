#!/usr/bin/env python3
"""
declares the TestGithubOrgClient(unittest.TestCase) class
"""
import unittest
from parameterized import parameterized
from unittest.mock import patch
from client import get_json
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    implements the test_org method
    Use @patch as a decorator to make sure get_json is called once
    with the expected argument but make sure it is not executed.
    Use @parameterized.expand as a decorator to parametrize
    the test with a couple of org examples to pass to
    GithubOrgClient.org
    """

    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mocked_get_json):
        """
        test the org method
        """
        client = GithubOrgClient(org_name)
        client.org()
        mocked_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")
