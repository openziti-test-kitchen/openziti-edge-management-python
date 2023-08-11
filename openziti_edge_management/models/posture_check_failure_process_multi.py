# coding: utf-8

"""
    Ziti Edge Management

    OpenZiti Edge Management API  # noqa: E501

    The version of the OpenAPI document: 0.25.31
    Contact: help@openziti.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List
from pydantic import BaseModel, Field, conlist
from openziti_edge_management.models.posture_check_failure import PostureCheckFailure
from openziti_edge_management.models.posture_check_failure_process_actual import PostureCheckFailureProcessActual
from openziti_edge_management.models.process_multi import ProcessMulti
from openziti_edge_management.models.semantic import Semantic

class PostureCheckFailureProcessMulti(PostureCheckFailure):
    """
    PostureCheckFailureProcessMulti
    """
    actual_value: conlist(PostureCheckFailureProcessActual) = Field(..., alias="actualValue")
    expected_value: conlist(ProcessMulti) = Field(..., alias="expectedValue")
    semantic: Semantic = Field(...)
    __properties = ["postureCheckId", "postureCheckName", "postureCheckType", "actualValue", "expectedValue", "semantic"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> PostureCheckFailureProcessMulti:
        """Create an instance of PostureCheckFailureProcessMulti from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in actual_value (list)
        _items = []
        if self.actual_value:
            for _item in self.actual_value:
                if _item:
                    _items.append(_item.to_dict())
            _dict['actualValue'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in expected_value (list)
        _items = []
        if self.expected_value:
            for _item in self.expected_value:
                if _item:
                    _items.append(_item.to_dict())
            _dict['expectedValue'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PostureCheckFailureProcessMulti:
        """Create an instance of PostureCheckFailureProcessMulti from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PostureCheckFailureProcessMulti.parse_obj(obj)

        _obj = PostureCheckFailureProcessMulti.parse_obj({
            "posture_check_id": obj.get("postureCheckId"),
            "posture_check_name": obj.get("postureCheckName"),
            "posture_check_type": obj.get("postureCheckType"),
            "actual_value": [PostureCheckFailureProcessActual.from_dict(_item) for _item in obj.get("actualValue")] if obj.get("actualValue") is not None else None,
            "expected_value": [ProcessMulti.from_dict(_item) for _item in obj.get("expectedValue")] if obj.get("expectedValue") is not None else None,
            "semantic": obj.get("semantic")
        })
        return _obj
