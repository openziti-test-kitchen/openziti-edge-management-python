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
from openziti_edge_management.model.posture_check_failure_domain import PostureCheckFailureDomain
from openziti_edge_management.model.posture_check_failure_mac_address import PostureCheckFailureMacAddress
from openziti_edge_management.model.posture_check_failure_mfa import PostureCheckFailureMfa
from openziti_edge_management.model.posture_check_failure_operating_system import PostureCheckFailureOperatingSystem
from openziti_edge_management.model.posture_check_failure_process import PostureCheckFailureProcess
from openziti_edge_management.model.posture_check_failure_process_multi import PostureCheckFailureProcessMulti
globals()['PostureCheckFailureDomain'] = PostureCheckFailureDomain
globals()['PostureCheckFailureMacAddress'] = PostureCheckFailureMacAddress
globals()['PostureCheckFailureMfa'] = PostureCheckFailureMfa
globals()['PostureCheckFailureOperatingSystem'] = PostureCheckFailureOperatingSystem
globals()['PostureCheckFailureProcess'] = PostureCheckFailureProcess
globals()['PostureCheckFailureProcessMulti'] = PostureCheckFailureProcessMulti
from openziti_edge_management.model.posture_check_failure import PostureCheckFailure


class TestPostureCheckFailure(unittest.TestCase):
    """PostureCheckFailure unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPostureCheckFailure(self):
        """Test PostureCheckFailure"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PostureCheckFailure()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
