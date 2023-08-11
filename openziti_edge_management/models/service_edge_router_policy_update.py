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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from openziti_edge_management.models.semantic import Semantic
from openziti_edge_management.models.tags import Tags

class ServiceEdgeRouterPolicyUpdate(BaseModel):
    """
    ServiceEdgeRouterPolicyUpdate
    """
    edge_router_roles: Optional[conlist(StrictStr)] = Field(None, alias="edgeRouterRoles")
    name: StrictStr = Field(...)
    semantic: Semantic = Field(...)
    service_roles: Optional[conlist(StrictStr)] = Field(None, alias="serviceRoles")
    tags: Optional[Tags] = None
    __properties = ["edgeRouterRoles", "name", "semantic", "serviceRoles", "tags"]

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
    def from_json(cls, json_str: str) -> ServiceEdgeRouterPolicyUpdate:
        """Create an instance of ServiceEdgeRouterPolicyUpdate from a JSON string"""
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
    def from_dict(cls, obj: dict) -> ServiceEdgeRouterPolicyUpdate:
        """Create an instance of ServiceEdgeRouterPolicyUpdate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ServiceEdgeRouterPolicyUpdate.parse_obj(obj)

        _obj = ServiceEdgeRouterPolicyUpdate.parse_obj({
            "edge_router_roles": obj.get("edgeRouterRoles"),
            "name": obj.get("name"),
            "semantic": obj.get("semantic"),
            "service_roles": obj.get("serviceRoles"),
            "tags": Tags.from_dict(obj.get("tags")) if obj.get("tags") is not None else None
        })
        return _obj


