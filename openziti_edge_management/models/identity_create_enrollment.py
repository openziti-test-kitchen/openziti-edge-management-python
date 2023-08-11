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


from typing import Optional
from pydantic import BaseModel, StrictBool, StrictStr

class IdentityCreateEnrollment(BaseModel):
    """
    IdentityCreateEnrollment
    """
    ott: Optional[StrictBool] = None
    ottca: Optional[StrictStr] = None
    updb: Optional[StrictStr] = None
    __properties = ["ott", "ottca", "updb"]

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
    def from_json(cls, json_str: str) -> IdentityCreateEnrollment:
        """Create an instance of IdentityCreateEnrollment from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> IdentityCreateEnrollment:
        """Create an instance of IdentityCreateEnrollment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return IdentityCreateEnrollment.parse_obj(obj)

        _obj = IdentityCreateEnrollment.parse_obj({
            "ott": obj.get("ott"),
            "ottca": obj.get("ottca"),
            "updb": obj.get("updb")
        })
        return _obj
