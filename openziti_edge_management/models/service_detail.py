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
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist
from openziti_edge_management.models.dial_bind import DialBind
from openziti_edge_management.models.link import Link
from openziti_edge_management.models.posture_queries import PostureQueries
from openziti_edge_management.models.tags import Tags

class ServiceDetail(BaseModel):
    """
    ServiceDetail
    """
    links: Dict[str, Link] = Field(..., alias="_links", description="A map of named links")
    created_at: datetime = Field(..., alias="createdAt")
    id: StrictStr = Field(...)
    tags: Optional[Tags] = None
    updated_at: datetime = Field(..., alias="updatedAt")
    config: Dict[str, Dict[str, Dict[str, Any]]] = Field(..., description="map of config data for this service keyed by the config type name. Only configs of the types requested will be returned.")
    configs: conlist(StrictStr) = Field(...)
    encryption_required: StrictBool = Field(..., alias="encryptionRequired", description="Describes whether connections must support end-to-end encryption on both sides of the connection. Read-only property, set at create.")
    name: StrictStr = Field(...)
    permissions: conlist(DialBind) = Field(...)
    posture_queries: conlist(PostureQueries) = Field(..., alias="postureQueries")
    role_attributes: Optional[conlist(StrictStr)] = Field(..., alias="roleAttributes", description="A set of strings used to loosly couple this resource to policies")
    terminator_strategy: StrictStr = Field(..., alias="terminatorStrategy")
    __properties = ["_links", "createdAt", "id", "tags", "updatedAt", "config", "configs", "encryptionRequired", "name", "permissions", "postureQueries", "roleAttributes", "terminatorStrategy"]

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
    def from_json(cls, json_str: str) -> ServiceDetail:
        """Create an instance of ServiceDetail from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in posture_queries (list)
        _items = []
        if self.posture_queries:
            for _item in self.posture_queries:
                if _item:
                    _items.append(_item.to_dict())
            _dict['postureQueries'] = _items
        # set to None if role_attributes (nullable) is None
        # and __fields_set__ contains the field
        if self.role_attributes is None and "role_attributes" in self.__fields_set__:
            _dict['roleAttributes'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ServiceDetail:
        """Create an instance of ServiceDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ServiceDetail.parse_obj(obj)

        _obj = ServiceDetail.parse_obj({
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
            "config": obj.get("config"),
            "configs": obj.get("configs"),
            "encryption_required": obj.get("encryptionRequired"),
            "name": obj.get("name"),
            "permissions": obj.get("permissions"),
            "posture_queries": [PostureQueries.from_dict(_item) for _item in obj.get("postureQueries")] if obj.get("postureQueries") is not None else None,
            "role_attributes": obj.get("roleAttributes"),
            "terminator_strategy": obj.get("terminatorStrategy")
        })
        return _obj

