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
from pydantic import BaseModel, Field, StrictBool, StrictInt
from openziti_edge_management.models.posture_check_create import PostureCheckCreate

class PostureCheckMfaCreate(PostureCheckCreate):
    """
    PostureCheckMfaCreate
    """
    ignore_legacy_endpoints: Optional[StrictBool] = Field(None, alias="ignoreLegacyEndpoints")
    prompt_on_unlock: Optional[StrictBool] = Field(None, alias="promptOnUnlock")
    prompt_on_wake: Optional[StrictBool] = Field(None, alias="promptOnWake")
    timeout_seconds: Optional[StrictInt] = Field(None, alias="timeoutSeconds")
    __properties = ["name", "roleAttributes", "tags", "typeId", "ignoreLegacyEndpoints", "promptOnUnlock", "promptOnWake", "timeoutSeconds"]

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
    def from_json(cls, json_str: str) -> PostureCheckMfaCreate:
        """Create an instance of PostureCheckMfaCreate from a JSON string"""
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
        # set to None if role_attributes (nullable) is None
        # and __fields_set__ contains the field
        if self.role_attributes is None and "role_attributes" in self.__fields_set__:
            _dict['roleAttributes'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PostureCheckMfaCreate:
        """Create an instance of PostureCheckMfaCreate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PostureCheckMfaCreate.parse_obj(obj)

        _obj = PostureCheckMfaCreate.parse_obj({
            "name": obj.get("name"),
            "role_attributes": obj.get("roleAttributes"),
            "tags": Tags.from_dict(obj.get("tags")) if obj.get("tags") is not None else None,
            "type_id": obj.get("typeId"),
            "ignore_legacy_endpoints": obj.get("ignoreLegacyEndpoints"),
            "prompt_on_unlock": obj.get("promptOnUnlock"),
            "prompt_on_wake": obj.get("promptOnWake"),
            "timeout_seconds": obj.get("timeoutSeconds")
        })
        return _obj

