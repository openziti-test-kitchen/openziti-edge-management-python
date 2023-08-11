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
from pydantic import BaseModel, StrictStr
from openziti_edge_management.models.auth_policy_primary_patch import AuthPolicyPrimaryPatch
from openziti_edge_management.models.auth_policy_secondary_patch import AuthPolicySecondaryPatch
from openziti_edge_management.models.tags import Tags

class AuthPolicyPatch(BaseModel):
    """
    A Auth Policy resource
    """
    name: Optional[StrictStr] = None
    primary: Optional[AuthPolicyPrimaryPatch] = None
    secondary: Optional[AuthPolicySecondaryPatch] = None
    tags: Optional[Tags] = None
    __properties = ["name", "primary", "secondary", "tags"]

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
    def from_json(cls, json_str: str) -> AuthPolicyPatch:
        """Create an instance of AuthPolicyPatch from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of primary
        if self.primary:
            _dict['primary'] = self.primary.to_dict()
        # override the default output from pydantic by calling `to_dict()` of secondary
        if self.secondary:
            _dict['secondary'] = self.secondary.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tags
        if self.tags:
            _dict['tags'] = self.tags.to_dict()
        # set to None if name (nullable) is None
        # and __fields_set__ contains the field
        if self.name is None and "name" in self.__fields_set__:
            _dict['name'] = None

        # set to None if secondary (nullable) is None
        # and __fields_set__ contains the field
        if self.secondary is None and "secondary" in self.__fields_set__:
            _dict['secondary'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AuthPolicyPatch:
        """Create an instance of AuthPolicyPatch from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AuthPolicyPatch.parse_obj(obj)

        _obj = AuthPolicyPatch.parse_obj({
            "name": obj.get("name"),
            "primary": AuthPolicyPrimaryPatch.from_dict(obj.get("primary")) if obj.get("primary") is not None else None,
            "secondary": AuthPolicySecondaryPatch.from_dict(obj.get("secondary")) if obj.get("secondary") is not None else None,
            "tags": Tags.from_dict(obj.get("tags")) if obj.get("tags") is not None else None
        })
        return _obj
