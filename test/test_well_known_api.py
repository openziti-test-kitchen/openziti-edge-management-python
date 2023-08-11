# coding: utf-8

"""
    Ziti Edge Management

    OpenZiti Edge Management API  # noqa: E501

    The version of the OpenAPI document: 0.25.31
    Contact: help@openziti.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest

import openziti_edge_management
from openziti_edge_management.api.well_known_api import WellKnownApi  # noqa: E501
from openziti_edge_management.rest import ApiException


class TestWellKnownApi(unittest.TestCase):
    """WellKnownApi unit test stubs"""

    def setUp(self):
        self.api = openziti_edge_management.api.well_known_api.WellKnownApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_list_well_known_cas(self):
        """Test case for list_well_known_cas

        Get CA Cert Store  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()