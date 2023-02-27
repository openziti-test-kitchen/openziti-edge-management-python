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
from openziti_edge_management.model.attributes import Attributes
from openziti_edge_management.model.identity_type import IdentityType
from openziti_edge_management.model.tags import Tags
from openziti_edge_management.model.terminator_cost import TerminatorCost
from openziti_edge_management.model.terminator_cost_map import TerminatorCostMap
from openziti_edge_management.model.terminator_precedence import TerminatorPrecedence
from openziti_edge_management.model.terminator_precedence_map import TerminatorPrecedenceMap
globals()['Attributes'] = Attributes
globals()['IdentityType'] = IdentityType
globals()['Tags'] = Tags
globals()['TerminatorCost'] = TerminatorCost
globals()['TerminatorCostMap'] = TerminatorCostMap
globals()['TerminatorPrecedence'] = TerminatorPrecedence
globals()['TerminatorPrecedenceMap'] = TerminatorPrecedenceMap
from openziti_edge_management.model.identity_patch import IdentityPatch


class TestIdentityPatch(unittest.TestCase):
    """IdentityPatch unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testIdentityPatch(self):
        """Test IdentityPatch"""
        # FIXME: construct object with mandatory attributes with example values
        # model = IdentityPatch()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
