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



from pydantic import BaseModel, Field, StrictBool

class AuthPolicyPrimaryCert(BaseModel):
    """
    AuthPolicyPrimaryCert
    """
    allow_expired_certs: StrictBool = Field(..., alias="allowExpiredCerts")
    allowed: StrictBool = Field(...)
    __properties = ["allowExpiredCerts", "allowed"]

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
    def from_json(cls, json_str: str) -> AuthPolicyPrimaryCert:
        """Create an instance of AuthPolicyPrimaryCert from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AuthPolicyPrimaryCert:
        """Create an instance of AuthPolicyPrimaryCert from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AuthPolicyPrimaryCert.parse_obj(obj)

        _obj = AuthPolicyPrimaryCert.parse_obj({
            "allow_expired_certs": obj.get("allowExpiredCerts"),
            "allowed": obj.get("allowed")
        })
        return _obj

