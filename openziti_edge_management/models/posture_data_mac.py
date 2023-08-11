# coding: utf-8

"""
    Ziti Edge Management

    OpenZiti Edge Management API

    The version of the OpenAPI document: 0.25.31
    Contact: help@openziti.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import List
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist

class PostureDataMac(BaseModel):
    """
    PostureDataMac
    """
    last_updated_at: datetime = Field(..., alias="lastUpdatedAt")
    posture_check_id: StrictStr = Field(..., alias="postureCheckId")
    timed_out: StrictBool = Field(..., alias="timedOut")
    addresses: conlist(StrictStr) = Field(...)
    __properties = ["lastUpdatedAt", "postureCheckId", "timedOut", "addresses"]

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
    def from_json(cls, json_str: str) -> PostureDataMac:
        """Create an instance of PostureDataMac from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PostureDataMac:
        """Create an instance of PostureDataMac from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PostureDataMac.parse_obj(obj)

        _obj = PostureDataMac.parse_obj({
            "last_updated_at": obj.get("lastUpdatedAt"),
            "posture_check_id": obj.get("postureCheckId"),
            "timed_out": obj.get("timedOut"),
            "addresses": obj.get("addresses")
        })
        return _obj


