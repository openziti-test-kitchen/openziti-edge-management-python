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
from openziti_edge_management.model.password import Password
from openziti_edge_management.model.tags import Tags
from openziti_edge_management.model.username import Username
globals()['Password'] = Password
globals()['Tags'] = Tags
globals()['Username'] = Username
from openziti_edge_management.model.authenticator_update import AuthenticatorUpdate


class TestAuthenticatorUpdate(unittest.TestCase):
    """AuthenticatorUpdate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAuthenticatorUpdate(self):
        """Test AuthenticatorUpdate"""
        # FIXME: construct object with mandatory attributes with example values
        # model = AuthenticatorUpdate()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
