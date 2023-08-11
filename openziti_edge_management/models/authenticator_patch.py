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
from pydantic import BaseModel, constr
from openziti_edge_management.models.tags import Tags

class AuthenticatorPatch(BaseModel):
    """
    All of the fields on an authenticator that may be updated
    """
    password: Optional[constr(strict=True, max_length=100, min_length=5)] = None
    tags: Optional[Tags] = None
    username: Optional[constr(strict=True, max_length=100, min_length=4)] = None
    __properties = ["password", "tags", "username"]

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
    def from_json(cls, json_str: str) -> AuthenticatorPatch:
        """Create an instance of AuthenticatorPatch from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of tags
        if self.tags:
            _dict['tags'] = self.tags.to_dict()
        # set to None if password (nullable) is None
        # and __fields_set__ contains the field
        if self.password is None and "password" in self.__fields_set__:
            _dict['password'] = None

        # set to None if username (nullable) is None
        # and __fields_set__ contains the field
        if self.username is None and "username" in self.__fields_set__:
            _dict['username'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AuthenticatorPatch:
        """Create an instance of AuthenticatorPatch from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AuthenticatorPatch.parse_obj(obj)

        _obj = AuthenticatorPatch.parse_obj({
            "password": obj.get("password"),
            "tags": Tags.from_dict(obj.get("tags")) if obj.get("tags") is not None else None,
            "username": obj.get("username")
        })
        return _obj
