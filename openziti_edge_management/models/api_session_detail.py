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

from datetime import datetime
from typing import Dict, List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist
from openziti_edge_management.models.auth_query_detail import AuthQueryDetail
from openziti_edge_management.models.dict[str,_link] import Dict[str, Link]
from openziti_edge_management.models.entity_ref import EntityRef
from openziti_edge_management.models.link import Link
from openziti_edge_management.models.tags import Tags

class ApiSessionDetail(BaseModel):
    """
    An API Session object
    """
    links: Dict[str, Link] = Field(..., alias="_links", description="A map of named links")
    created_at: datetime = Field(..., alias="createdAt")
    id: StrictStr = Field(...)
    tags: Optional[Tags] = None
    updated_at: datetime = Field(..., alias="updatedAt")
    auth_queries: conlist(AuthQueryDetail) = Field(..., alias="authQueries")
    authenticator_id: StrictStr = Field(..., alias="authenticatorId")
    cached_last_activity_at: Optional[datetime] = Field(None, alias="cachedLastActivityAt")
    config_types: conlist(StrictStr) = Field(..., alias="configTypes")
    identity: EntityRef = Field(...)
    identity_id: StrictStr = Field(..., alias="identityId")
    ip_address: StrictStr = Field(..., alias="ipAddress")
    is_mfa_complete: StrictBool = Field(..., alias="isMfaComplete")
    is_mfa_required: StrictBool = Field(..., alias="isMfaRequired")
    last_activity_at: Optional[datetime] = Field(None, alias="lastActivityAt")
    token: StrictStr = Field(...)
    __properties = ["_links", "createdAt", "id", "tags", "updatedAt", "authQueries", "authenticatorId", "cachedLastActivityAt", "configTypes", "identity", "identityId", "ipAddress", "isMfaComplete", "isMfaRequired", "lastActivityAt", "token"]

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
    def from_json(cls, json_str: str) -> ApiSessionDetail:
        """Create an instance of ApiSessionDetail from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in auth_queries (list)
        _items = []
        if self.auth_queries:
            for _item in self.auth_queries:
                if _item:
                    _items.append(_item.to_dict())
            _dict['authQueries'] = _items
        # override the default output from pydantic by calling `to_dict()` of identity
        if self.identity:
            _dict['identity'] = self.identity.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiSessionDetail:
        """Create an instance of ApiSessionDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiSessionDetail.parse_obj(obj)

        _obj = ApiSessionDetail.parse_obj({
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
            "auth_queries": [AuthQueryDetail.from_dict(_item) for _item in obj.get("authQueries")] if obj.get("authQueries") is not None else None,
            "authenticator_id": obj.get("authenticatorId"),
            "cached_last_activity_at": obj.get("cachedLastActivityAt"),
            "config_types": obj.get("configTypes"),
            "identity": EntityRef.from_dict(obj.get("identity")) if obj.get("identity") is not None else None,
            "identity_id": obj.get("identityId"),
            "ip_address": obj.get("ipAddress"),
            "is_mfa_complete": obj.get("isMfaComplete"),
            "is_mfa_required": obj.get("isMfaRequired"),
            "last_activity_at": obj.get("lastActivityAt"),
            "token": obj.get("token")
        })
        return _obj


