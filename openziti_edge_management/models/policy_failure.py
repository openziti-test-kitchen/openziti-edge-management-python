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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from openziti_edge_management.models.posture_check_failure import PostureCheckFailure

class PolicyFailure(BaseModel):
    """
    PolicyFailure
    """
    checks: Optional[conlist(PostureCheckFailure)] = None
    policy_id: Optional[StrictStr] = Field(None, alias="policyId")
    policy_name: Optional[StrictStr] = Field(None, alias="policyName")
    __properties = ["checks", "policyId", "policyName"]

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
    def from_json(cls, json_str: str) -> PolicyFailure:
        """Create an instance of PolicyFailure from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in checks (list)
        _items = []
        if self.checks:
            for _item in self.checks:
                if _item:
                    _items.append(_item.to_dict())
            _dict['checks'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PolicyFailure:
        """Create an instance of PolicyFailure from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PolicyFailure.parse_obj(obj)

        _obj = PolicyFailure.parse_obj({
            "checks": [PostureCheckFailure.from_dict(_item) for _item in obj.get("checks")] if obj.get("checks") is not None else None,
            "policy_id": obj.get("policyId"),
            "policy_name": obj.get("policyName")
        })
        return _obj

