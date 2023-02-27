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
from openziti_edge_management.model.base_entity import BaseEntity
from openziti_edge_management.model.links import Links
from openziti_edge_management.model.posture_check_type import PostureCheckType
from openziti_edge_management.model.posture_query_all_of import PostureQueryAllOf
from openziti_edge_management.model.posture_query_process import PostureQueryProcess
from openziti_edge_management.model.tags import Tags
globals()['BaseEntity'] = BaseEntity
globals()['Links'] = Links
globals()['PostureCheckType'] = PostureCheckType
globals()['PostureQueryAllOf'] = PostureQueryAllOf
globals()['PostureQueryProcess'] = PostureQueryProcess
globals()['Tags'] = Tags
from openziti_edge_management.model.posture_query import PostureQuery


class TestPostureQuery(unittest.TestCase):
    """PostureQuery unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPostureQuery(self):
        """Test PostureQuery"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PostureQuery()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()