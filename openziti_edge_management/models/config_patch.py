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


from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictStr
from openziti_edge_management.models.tags import Tags

class ConfigPatch(BaseModel):
    """
    A config patch object
    """
    data: Optional[Dict[str, Any]] = Field(None, description="Data payload is defined by the schema of the config-type defined in the type parameter")
    name: Optional[StrictStr] = None
    tags: Optional[Tags] = None
    __properties = ["data", "name", "tags"]

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
    def from_json(cls, json_str: str) -> ConfigPatch:
        """Create an instance of ConfigPatch from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ConfigPatch:
        """Create an instance of ConfigPatch from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ConfigPatch.parse_obj(obj)

        _obj = ConfigPatch.parse_obj({
            "data": obj.get("data"),
            "name": obj.get("name"),
            "tags": Tags.from_dict(obj.get("tags")) if obj.get("tags") is not None else None
        })
        return _obj

