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


from typing import List
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist

class AuthPolicyPrimaryExtJwt(BaseModel):
    """
    AuthPolicyPrimaryExtJwt
    """
    allowed: StrictBool = Field(...)
    allowed_signers: conlist(StrictStr) = Field(..., alias="allowedSigners")
    __properties = ["allowed", "allowedSigners"]

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
    def from_json(cls, json_str: str) -> AuthPolicyPrimaryExtJwt:
        """Create an instance of AuthPolicyPrimaryExtJwt from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AuthPolicyPrimaryExtJwt:
        """Create an instance of AuthPolicyPrimaryExtJwt from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AuthPolicyPrimaryExtJwt.parse_obj(obj)

        _obj = AuthPolicyPrimaryExtJwt.parse_obj({
            "allowed": obj.get("allowed"),
            "allowed_signers": obj.get("allowedSigners")
        })
        return _obj


