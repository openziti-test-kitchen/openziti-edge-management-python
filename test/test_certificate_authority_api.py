"""
    Ziti Edge Management

    OpenZiti Edge Management API  # noqa: E501

    The version of the OpenAPI document: 0.25.6
    Contact: help@openziti.org
    Generated by: https://openapi-generator.tech
"""


import unittest

import openziti_edge_management
from openziti_edge_management.api.certificate_authority_api import CertificateAuthorityApi  # noqa: E501


class TestCertificateAuthorityApi(unittest.TestCase):
    """CertificateAuthorityApi unit test stubs"""

    def setUp(self):
        self.api = CertificateAuthorityApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_ca(self):
        """Test case for create_ca

        Creates a CA  # noqa: E501
        """
        pass

    def test_delete_ca(self):
        """Test case for delete_ca

        Delete a CA  # noqa: E501
        """
        pass

    def test_detail_ca(self):
        """Test case for detail_ca

        Retrieves a single CA  # noqa: E501
        """
        pass

    def test_get_ca_jwt(self):
        """Test case for get_ca_jwt

        Retrieve the enrollment JWT for a CA  # noqa: E501
        """
        pass

    def test_list_cas(self):
        """Test case for list_cas

        List CAs  # noqa: E501
        """
        pass

    def test_patch_ca(self):
        """Test case for patch_ca

        Update the supplied fields on a CA  # noqa: E501
        """
        pass

    def test_update_ca(self):
        """Test case for update_ca

        Update all fields on a CA  # noqa: E501
        """
        pass

    def test_verify_ca(self):
        """Test case for verify_ca

        Verify a CA  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()