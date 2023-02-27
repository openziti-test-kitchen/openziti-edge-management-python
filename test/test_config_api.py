"""
    Ziti Edge Management

    OpenZiti Edge Management API  # noqa: E501

    The version of the OpenAPI document: 0.25.6
    Contact: help@openziti.org
    Generated by: https://openapi-generator.tech
"""


import unittest

import openziti_edge_management
from openziti_edge_management.api.config_api import ConfigApi  # noqa: E501


class TestConfigApi(unittest.TestCase):
    """ConfigApi unit test stubs"""

    def setUp(self):
        self.api = ConfigApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_config(self):
        """Test case for create_config

        Create a config resource  # noqa: E501
        """
        pass

    def test_create_config_type(self):
        """Test case for create_config_type

        Create a config-type. Requires admin access.  # noqa: E501
        """
        pass

    def test_delete_config(self):
        """Test case for delete_config

        Delete a config  # noqa: E501
        """
        pass

    def test_delete_config_type(self):
        """Test case for delete_config_type

        Delete a config-type  # noqa: E501
        """
        pass

    def test_detail_config(self):
        """Test case for detail_config

        Retrieves a single config  # noqa: E501
        """
        pass

    def test_detail_config_type(self):
        """Test case for detail_config_type

        Retrieves a single config-type  # noqa: E501
        """
        pass

    def test_list_config_types(self):
        """Test case for list_config_types

        List config-types  # noqa: E501
        """
        pass

    def test_list_configs(self):
        """Test case for list_configs

        List configs  # noqa: E501
        """
        pass

    def test_list_configs_for_config_type(self):
        """Test case for list_configs_for_config_type

        Lists the configs of a specific config-type  # noqa: E501
        """
        pass

    def test_patch_config(self):
        """Test case for patch_config

        Update the supplied fields on a config  # noqa: E501
        """
        pass

    def test_patch_config_type(self):
        """Test case for patch_config_type

        Update the supplied fields on a config-type  # noqa: E501
        """
        pass

    def test_update_config(self):
        """Test case for update_config

        Update all fields on a config  # noqa: E501
        """
        pass

    def test_update_config_type(self):
        """Test case for update_config_type

        Update all fields on a config-type  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()