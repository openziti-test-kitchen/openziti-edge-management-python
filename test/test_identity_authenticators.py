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
from openziti_edge_management.model.identity_authenticators_cert import IdentityAuthenticatorsCert
from openziti_edge_management.model.identity_authenticators_updb import IdentityAuthenticatorsUpdb
globals()['IdentityAuthenticatorsCert'] = IdentityAuthenticatorsCert
globals()['IdentityAuthenticatorsUpdb'] = IdentityAuthenticatorsUpdb
from openziti_edge_management.model.identity_authenticators import IdentityAuthenticators


class TestIdentityAuthenticators(unittest.TestCase):
    """IdentityAuthenticators unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testIdentityAuthenticators(self):
        """Test IdentityAuthenticators"""
        # FIXME: construct object with mandatory attributes with example values
        # model = IdentityAuthenticators()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
