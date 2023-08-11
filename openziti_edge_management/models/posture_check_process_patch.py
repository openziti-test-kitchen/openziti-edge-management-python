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


from typing import Optional

from openziti_edge_management.models.posture_check_patch import PostureCheckPatch
from openziti_edge_management.models.posture_check_type import PostureCheckType
from openziti_edge_management.models.process import Process
from openziti_edge_management.models.tags import Tags

class PostureCheckProcessPatch(PostureCheckPatch):
    """
    PostureCheckProcessPatch
    """
    process: Optional[Process] = None
    __properties = ["name", "roleAttributes", "tags", "typeId", "process"]

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
    def from_json(cls, json_str: str) -> PostureCheckProcessPatch:
        """Create an instance of PostureCheckProcessPatch from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of process
        if self.process:
            _dict['process'] = self.process.to_dict()
        # set to None if role_attributes (nullable) is None
        # and __fields_set__ contains the field
        if self.role_attributes is None and "role_attributes" in self.__fields_set__:
            _dict['roleAttributes'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PostureCheckProcessPatch:
        """Create an instance of PostureCheckProcessPatch from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PostureCheckProcessPatch.parse_obj(obj)

        _obj = PostureCheckProcessPatch.parse_obj({
            "name": obj.get("name"),
            "role_attributes": obj.get("roleAttributes"),
            "tags": Tags.from_dict(obj.get("tags")) if obj.get("tags") is not None else None,
            "type_id": obj.get("typeId"),
            "process": Process.from_dict(obj.get("process")) if obj.get("process") is not None else None
        })
        return _obj


