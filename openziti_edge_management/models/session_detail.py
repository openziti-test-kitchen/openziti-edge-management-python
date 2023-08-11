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
from typing import Dict, List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from openziti_edge_management.models.dial_bind import DialBind
from openziti_edge_management.models.entity_ref import EntityRef
from openziti_edge_management.models.link import Link
from openziti_edge_management.models.session_edge_router import SessionEdgeRouter
from openziti_edge_management.models.tags import Tags

class SessionDetail(BaseModel):
    """
    SessionDetail
    """
    links: Dict[str, Link] = Field(..., alias="_links", description="A map of named links")
    created_at: datetime = Field(..., alias="createdAt")
    id: StrictStr = Field(...)
    tags: Optional[Tags] = None
    updated_at: datetime = Field(..., alias="updatedAt")
    api_session: EntityRef = Field(..., alias="apiSession")
    api_session_id: StrictStr = Field(..., alias="apiSessionId")
    edge_routers: conlist(SessionEdgeRouter) = Field(..., alias="edgeRouters")
    identity_id: StrictStr = Field(..., alias="identityId")
    service: EntityRef = Field(...)
    service_id: StrictStr = Field(..., alias="serviceId")
    token: StrictStr = Field(...)
    type: DialBind = Field(...)
    __properties = ["_links", "createdAt", "id", "tags", "updatedAt", "apiSession", "apiSessionId", "edgeRouters", "identityId", "service", "serviceId", "token", "type"]

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
    def from_json(cls, json_str: str) -> SessionDetail:
        """Create an instance of SessionDetail from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of api_session
        if self.api_session:
            _dict['apiSession'] = self.api_session.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in edge_routers (list)
        _items = []
        if self.edge_routers:
            for _item in self.edge_routers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['edgeRouters'] = _items
        # override the default output from pydantic by calling `to_dict()` of service
        if self.service:
            _dict['service'] = self.service.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SessionDetail:
        """Create an instance of SessionDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SessionDetail.parse_obj(obj)

        _obj = SessionDetail.parse_obj({
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
            "api_session": EntityRef.from_dict(obj.get("apiSession")) if obj.get("apiSession") is not None else None,
            "api_session_id": obj.get("apiSessionId"),
            "edge_routers": [SessionEdgeRouter.from_dict(_item) for _item in obj.get("edgeRouters")] if obj.get("edgeRouters") is not None else None,
            "identity_id": obj.get("identityId"),
            "service": EntityRef.from_dict(obj.get("service")) if obj.get("service") is not None else None,
            "service_id": obj.get("serviceId"),
            "token": obj.get("token"),
            "type": obj.get("type")
        })
        return _obj

