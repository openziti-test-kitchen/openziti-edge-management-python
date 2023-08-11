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
from pydantic import BaseModel, Field, StrictBool, StrictStr, conint, conlist
from openziti_edge_management.models.dict[str,_link] import Dict[str, Link]
from openziti_edge_management.models.link import Link
from openziti_edge_management.models.tags import Tags
from openziti_edge_management.models.version_info import VersionInfo

class EdgeRouterDetail(BaseModel):
    """
    A detail edge router resource
    """
    links: Dict[str, Link] = Field(..., alias="_links", description="A map of named links")
    created_at: datetime = Field(..., alias="createdAt")
    id: StrictStr = Field(...)
    tags: Optional[Tags] = None
    updated_at: datetime = Field(..., alias="updatedAt")
    app_data: Optional[Tags] = Field(None, alias="appData")
    cost: Optional[conint(strict=True, le=65535, ge=0)] = Field(...)
    disabled: StrictBool = Field(...)
    hostname: StrictStr = Field(...)
    is_online: StrictBool = Field(..., alias="isOnline")
    name: StrictStr = Field(...)
    no_traversal: Optional[StrictBool] = Field(..., alias="noTraversal")
    supported_protocols: Dict[str, StrictStr] = Field(..., alias="supportedProtocols")
    sync_status: StrictStr = Field(..., alias="syncStatus")
    cert_pem: Optional[StrictStr] = Field(None, alias="certPem")
    enrollment_created_at: Optional[datetime] = Field(None, alias="enrollmentCreatedAt")
    enrollment_expires_at: Optional[datetime] = Field(None, alias="enrollmentExpiresAt")
    enrollment_jwt: Optional[StrictStr] = Field(None, alias="enrollmentJwt")
    enrollment_token: Optional[StrictStr] = Field(None, alias="enrollmentToken")
    fingerprint: Optional[StrictStr] = None
    is_tunneler_enabled: StrictBool = Field(..., alias="isTunnelerEnabled")
    is_verified: StrictBool = Field(..., alias="isVerified")
    role_attributes: Optional[conlist(StrictStr)] = Field(..., alias="roleAttributes", description="A set of strings used to loosly couple this resource to policies")
    unverified_cert_pem: Optional[StrictStr] = Field(None, alias="unverifiedCertPem")
    unverified_fingerprint: Optional[StrictStr] = Field(None, alias="unverifiedFingerprint")
    version_info: Optional[VersionInfo] = Field(None, alias="versionInfo")
    __properties = ["_links", "createdAt", "id", "tags", "updatedAt", "appData", "cost", "disabled", "hostname", "isOnline", "name", "noTraversal", "supportedProtocols", "syncStatus", "certPem", "enrollmentCreatedAt", "enrollmentExpiresAt", "enrollmentJwt", "enrollmentToken", "fingerprint", "isTunnelerEnabled", "isVerified", "roleAttributes", "unverifiedCertPem", "unverifiedFingerprint", "versionInfo"]

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
    def from_json(cls, json_str: str) -> EdgeRouterDetail:
        """Create an instance of EdgeRouterDetail from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of app_data
        if self.app_data:
            _dict['appData'] = self.app_data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of version_info
        if self.version_info:
            _dict['versionInfo'] = self.version_info.to_dict()
        # set to None if cost (nullable) is None
        # and __fields_set__ contains the field
        if self.cost is None and "cost" in self.__fields_set__:
            _dict['cost'] = None

        # set to None if no_traversal (nullable) is None
        # and __fields_set__ contains the field
        if self.no_traversal is None and "no_traversal" in self.__fields_set__:
            _dict['noTraversal'] = None

        # set to None if cert_pem (nullable) is None
        # and __fields_set__ contains the field
        if self.cert_pem is None and "cert_pem" in self.__fields_set__:
            _dict['certPem'] = None

        # set to None if enrollment_created_at (nullable) is None
        # and __fields_set__ contains the field
        if self.enrollment_created_at is None and "enrollment_created_at" in self.__fields_set__:
            _dict['enrollmentCreatedAt'] = None

        # set to None if enrollment_expires_at (nullable) is None
        # and __fields_set__ contains the field
        if self.enrollment_expires_at is None and "enrollment_expires_at" in self.__fields_set__:
            _dict['enrollmentExpiresAt'] = None

        # set to None if enrollment_jwt (nullable) is None
        # and __fields_set__ contains the field
        if self.enrollment_jwt is None and "enrollment_jwt" in self.__fields_set__:
            _dict['enrollmentJwt'] = None

        # set to None if enrollment_token (nullable) is None
        # and __fields_set__ contains the field
        if self.enrollment_token is None and "enrollment_token" in self.__fields_set__:
            _dict['enrollmentToken'] = None

        # set to None if role_attributes (nullable) is None
        # and __fields_set__ contains the field
        if self.role_attributes is None and "role_attributes" in self.__fields_set__:
            _dict['roleAttributes'] = None

        # set to None if unverified_cert_pem (nullable) is None
        # and __fields_set__ contains the field
        if self.unverified_cert_pem is None and "unverified_cert_pem" in self.__fields_set__:
            _dict['unverifiedCertPem'] = None

        # set to None if unverified_fingerprint (nullable) is None
        # and __fields_set__ contains the field
        if self.unverified_fingerprint is None and "unverified_fingerprint" in self.__fields_set__:
            _dict['unverifiedFingerprint'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EdgeRouterDetail:
        """Create an instance of EdgeRouterDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EdgeRouterDetail.parse_obj(obj)

        _obj = EdgeRouterDetail.parse_obj({
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
            "app_data": Tags.from_dict(obj.get("appData")) if obj.get("appData") is not None else None,
            "cost": obj.get("cost"),
            "disabled": obj.get("disabled"),
            "hostname": obj.get("hostname"),
            "is_online": obj.get("isOnline"),
            "name": obj.get("name"),
            "no_traversal": obj.get("noTraversal"),
            "supported_protocols": obj.get("supportedProtocols"),
            "sync_status": obj.get("syncStatus"),
            "cert_pem": obj.get("certPem"),
            "enrollment_created_at": obj.get("enrollmentCreatedAt"),
            "enrollment_expires_at": obj.get("enrollmentExpiresAt"),
            "enrollment_jwt": obj.get("enrollmentJwt"),
            "enrollment_token": obj.get("enrollmentToken"),
            "fingerprint": obj.get("fingerprint"),
            "is_tunneler_enabled": obj.get("isTunnelerEnabled"),
            "is_verified": obj.get("isVerified"),
            "role_attributes": obj.get("roleAttributes"),
            "unverified_cert_pem": obj.get("unverifiedCertPem"),
            "unverified_fingerprint": obj.get("unverifiedFingerprint"),
            "version_info": VersionInfo.from_dict(obj.get("versionInfo")) if obj.get("versionInfo") is not None else None
        })
        return _obj


