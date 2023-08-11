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

from datetime import datetime

from pydantic import BaseModel, Field, StrictBool, StrictStr

class PostureDataBase(BaseModel):
    """
    PostureDataBase
    """
    last_updated_at: datetime = Field(..., alias="lastUpdatedAt")
    posture_check_id: StrictStr = Field(..., alias="postureCheckId")
    timed_out: StrictBool = Field(..., alias="timedOut")
    __properties = ["lastUpdatedAt", "postureCheckId", "timedOut"]

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
    def from_json(cls, json_str: str) -> PostureDataBase:
        """Create an instance of PostureDataBase from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PostureDataBase:
        """Create an instance of PostureDataBase from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PostureDataBase.parse_obj(obj)

        _obj = PostureDataBase.parse_obj({
            "last_updated_at": obj.get("lastUpdatedAt"),
            "posture_check_id": obj.get("postureCheckId"),
            "timed_out": obj.get("timedOut")
        })
        return _obj

