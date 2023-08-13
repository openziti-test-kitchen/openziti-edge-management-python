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
from typing import Dict, Optional
from pydantic import BaseModel, Field, StrictStr
from openziti_edge_management.models.entity_ref import EntityRef
from openziti_edge_management.models.link import Link
from openziti_edge_management.models.tags import Tags

class EnrollmentDetail(BaseModel):
    """
    An enrollment object. Enrollments are tied to identities and potentially a CA. Depending on the method, different fields are utilized. For example ottca enrollments use the `ca` field and updb enrollments use the username field, but not vice versa. 
    """
    links: Dict[str, Link] = Field(..., alias="_links", description="A map of named links")
    created_at: datetime = Field(..., alias="createdAt")
    id: StrictStr = Field(...)
    tags: Optional[Tags] = None
    updated_at: datetime = Field(..., alias="updatedAt")
    ca_id: Optional[StrictStr] = Field(None, alias="caId")
    edge_router: Optional[EntityRef] = Field(None, alias="edgeRouter")
    edge_router_id: Optional[StrictStr] = Field(None, alias="edgeRouterId")
    expires_at: datetime = Field(..., alias="expiresAt")
    identity: Optional[EntityRef] = None
    identity_id: Optional[StrictStr] = Field(None, alias="identityId")
    jwt: Optional[StrictStr] = None
    method: StrictStr = Field(...)
    token: StrictStr = Field(...)
    transit_router: Optional[EntityRef] = Field(None, alias="transitRouter")
    transit_router_id: Optional[StrictStr] = Field(None, alias="transitRouterId")
    username: Optional[StrictStr] = None
    __properties = ["_links", "createdAt", "id", "tags", "updatedAt", "caId", "edgeRouter", "edgeRouterId", "expiresAt", "identity", "identityId", "jwt", "method", "token", "transitRouter", "transitRouterId", "username"]

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
    def from_json(cls, json_str: str) -> EnrollmentDetail:
        """Create an instance of EnrollmentDetail from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of edge_router
        if self.edge_router:
            _dict['edgeRouter'] = self.edge_router.to_dict()
        # override the default output from pydantic by calling `to_dict()` of identity
        if self.identity:
            _dict['identity'] = self.identity.to_dict()
        # override the default output from pydantic by calling `to_dict()` of transit_router
        if self.transit_router:
            _dict['transitRouter'] = self.transit_router.to_dict()
        # set to None if ca_id (nullable) is None
        # and __fields_set__ contains the field
        if self.ca_id is None and "ca_id" in self.__fields_set__:
            _dict['caId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EnrollmentDetail:
        """Create an instance of EnrollmentDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EnrollmentDetail.parse_obj(obj)

        _obj = EnrollmentDetail.parse_obj({
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
            "ca_id": obj.get("caId"),
            "edge_router": EntityRef.from_dict(obj.get("edgeRouter")) if obj.get("edgeRouter") is not None else None,
            "edge_router_id": obj.get("edgeRouterId"),
            "expires_at": obj.get("expiresAt"),
            "identity": EntityRef.from_dict(obj.get("identity")) if obj.get("identity") is not None else None,
            "identity_id": obj.get("identityId"),
            "jwt": obj.get("jwt"),
            "method": obj.get("method"),
            "token": obj.get("token"),
            "transit_router": EntityRef.from_dict(obj.get("transitRouter")) if obj.get("transitRouter") is not None else None,
            "transit_router_id": obj.get("transitRouterId"),
            "username": obj.get("username")
        })
        return _obj

