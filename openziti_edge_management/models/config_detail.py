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
from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictStr
from openziti_edge_management.models.entity_ref import EntityRef
from openziti_edge_management.models.link import Link
from openziti_edge_management.models.tags import Tags

class ConfigDetail(BaseModel):
    """
    A config resource
    """
    links: Dict[str, Link] = Field(..., alias="_links", description="A map of named links")
    created_at: datetime = Field(..., alias="createdAt")
    id: StrictStr = Field(...)
    tags: Optional[Tags] = None
    updated_at: datetime = Field(..., alias="updatedAt")
    config_type: EntityRef = Field(..., alias="configType")
    config_type_id: StrictStr = Field(..., alias="configTypeId")
    data: Dict[str, Any] = Field(..., description="The data section of a config is based on the schema of its type")
    name: StrictStr = Field(...)
    __properties = ["_links", "createdAt", "id", "tags", "updatedAt", "configType", "configTypeId", "data", "name"]

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
    def from_json(cls, json_str: str) -> ConfigDetail:
        """Create an instance of ConfigDetail from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each value in links (dict)
        _field_dict = {}
        if self.links:
            for _key in self.links:
                if self.links[_key]:
                    _field_dict[_key] = self.links[_key].to_dict()
            _dict['_links'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of tags
        if self.tags:
            _dict['tags'] = self.tags.to_dict()
        # override the default output from pydantic by calling `to_dict()` of config_type
        if self.config_type:
            _dict['configType'] = self.config_type.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ConfigDetail:
        """Create an instance of ConfigDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ConfigDetail.parse_obj(obj)

        _obj = ConfigDetail.parse_obj({
            "links": dict(
                (_k, Link.from_dict(_v))
                for _k, _v in obj.get("_links").items()
            )
            if obj.get("_links") is not None
            else None,
            "created_at": obj.get("createdAt"),
            "id": obj.get("id"),
            "tags": Tags.from_dict(obj.get("tags")) if obj.get("tags") is not None else None,
            "updated_at": obj.get("updatedAt"),
            "config_type": EntityRef.from_dict(obj.get("configType")) if obj.get("configType") is not None else None,
            "config_type_id": obj.get("configTypeId"),
            "data": obj.get("data"),
            "name": obj.get("name")
        })
        return _obj

