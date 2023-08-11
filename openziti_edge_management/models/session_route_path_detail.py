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

class SessionRoutePathDetail(BaseModel):
    """
    SessionRoutePathDetail
    """
    route_path: Optional[conlist(StrictStr)] = Field(None, alias="routePath")
    __properties = ["routePath"]

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
    def from_json(cls, json_str: str) -> SessionRoutePathDetail:
        """Create an instance of SessionRoutePathDetail from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SessionRoutePathDetail:
        """Create an instance of SessionRoutePathDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SessionRoutePathDetail.parse_obj(obj)

        _obj = SessionRoutePathDetail.parse_obj({
            "route_path": obj.get("routePath")
        })
        return _obj

