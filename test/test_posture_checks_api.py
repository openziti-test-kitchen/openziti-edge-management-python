"""
    Ziti Edge Management

    OpenZiti Edge Management API  # noqa: E501

    The version of the OpenAPI document: 0.25.6
    Contact: help@openziti.org
    Generated by: https://openapi-generator.tech
"""


import unittest

import openziti_edge_management
from openziti_edge_management.api.posture_checks_api import PostureChecksApi  # noqa: E501


class TestPostureChecksApi(unittest.TestCase):
    """PostureChecksApi unit test stubs"""

    def setUp(self):
        self.api = PostureChecksApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_posture_check(self):
        """Test case for create_posture_check

        Creates a Posture Checks  # noqa: E501
        """
        pass

    def test_delete_posture_check(self):
        """Test case for delete_posture_check

        Deletes an Posture Checks  # noqa: E501
        """
        pass

    def test_detail_posture_check(self):
        """Test case for detail_posture_check

        Retrieves a single Posture Checks  # noqa: E501
        """
        pass

    def test_detail_posture_check_type(self):
        """Test case for detail_posture_check_type

        Retrieves a single posture check type  # noqa: E501
        """
        pass

    def test_list_posture_check_types(self):
        """Test case for list_posture_check_types

        List a subset of posture check types  # noqa: E501
        """
        pass

    def test_list_posture_checks(self):
        """Test case for list_posture_checks

        List a subset of posture checks  # noqa: E501
        """
        pass

    def test_patch_posture_check(self):
        """Test case for patch_posture_check

        Update the supplied fields on a Posture Checks  # noqa: E501
        """
        pass

    def test_update_posture_check(self):
        """Test case for update_posture_check

        Update all fields on a Posture Checks  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
