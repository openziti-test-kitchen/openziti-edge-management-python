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
from openziti_edge_management.model.auth_policy_primary_cert import AuthPolicyPrimaryCert
from openziti_edge_management.model.auth_policy_primary_ext_jwt import AuthPolicyPrimaryExtJwt
from openziti_edge_management.model.auth_policy_primary_updb import AuthPolicyPrimaryUpdb
globals()['AuthPolicyPrimaryCert'] = AuthPolicyPrimaryCert
globals()['AuthPolicyPrimaryExtJwt'] = AuthPolicyPrimaryExtJwt
globals()['AuthPolicyPrimaryUpdb'] = AuthPolicyPrimaryUpdb
from openziti_edge_management.model.auth_policy_primary import AuthPolicyPrimary


class TestAuthPolicyPrimary(unittest.TestCase):
    """AuthPolicyPrimary unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAuthPolicyPrimary(self):
        """Test AuthPolicyPrimary"""
        # FIXME: construct object with mandatory attributes with example values
        # model = AuthPolicyPrimary()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
