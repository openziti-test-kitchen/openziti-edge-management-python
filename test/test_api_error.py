"""
    Ziti Edge Management

    OpenZiti Edge Management API  # noqa: E501

    The version of the OpenAPI document: 0.25.6
    Contact: help@openziti.org
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import openziti_edge_management
from openziti_edge_management.model.api_error_args import ApiErrorArgs
from openziti_edge_management.model.api_error_cause import ApiErrorCause
globals()['ApiErrorArgs'] = ApiErrorArgs
globals()['ApiErrorCause'] = ApiErrorCause
from openziti_edge_management.model.api_error import ApiError


class TestApiError(unittest.TestCase):
    """ApiError unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testApiError(self):
        """Test ApiError"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ApiError()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
