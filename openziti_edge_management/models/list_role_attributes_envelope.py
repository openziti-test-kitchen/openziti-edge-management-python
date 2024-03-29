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
from pydantic import BaseModel, Field, StrictStr, conlist
from openziti_edge_management.models.meta import Meta

class ListRoleAttributesEnvelope(BaseModel):
    """
    ListRoleAttributesEnvelope
    """
    data: conlist(StrictStr) = Field(..., description="An array of role attributes")
    meta: Meta = Field(...)
    __properties = ["data", "meta"]

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
    def from_json(cls, json_str: str) -> ListRoleAttributesEnvelope:
        """Create an instance of ListRoleAttributesEnvelope from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of meta
        if self.meta:
            _dict['meta'] = self.meta.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ListRoleAttributesEnvelope:
        """Create an instance of ListRoleAttributesEnvelope from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ListRoleAttributesEnvelope.parse_obj(obj)

        _obj = ListRoleAttributesEnvelope.parse_obj({
            "data": obj.get("data"),
            "meta": Meta.from_dict(obj.get("meta")) if obj.get("meta") is not None else None
        })
        return _obj

