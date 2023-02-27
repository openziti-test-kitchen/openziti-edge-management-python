"""
    Ziti Edge Management

    OpenZiti Edge Management API  # noqa: E501

    The version of the OpenAPI document: 0.25.6
    Contact: help@openziti.org
    Generated by: https://openapi-generator.tech
"""


import unittest

import openziti_edge_management
from openziti_edge_management.api.role_attributes_api import RoleAttributesApi  # noqa: E501


class TestRoleAttributesApi(unittest.TestCase):
    """RoleAttributesApi unit test stubs"""

    def setUp(self):
        self.api = RoleAttributesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_list_edge_router_role_attributes(self):
        """Test case for list_edge_router_role_attributes

        List role attributes in use by edge routers  # noqa: E501
        """
        pass

    def test_list_identity_role_attributes(self):
        """Test case for list_identity_role_attributes

        List role attributes in use by identities  # noqa: E501
        """
        pass

    def test_list_service_role_attributes(self):
        """Test case for list_service_role_attributes

        List role attributes in use by services  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
