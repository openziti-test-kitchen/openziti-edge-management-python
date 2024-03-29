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
from pydantic import BaseModel, Field, StrictBool, StrictStr
from openziti_edge_management.models.link import Link
from openziti_edge_management.models.tags import Tags

class ExternalJwtSignerDetail(BaseModel):
    """
    A External JWT Signer resource
    """
    links: Dict[str, Link] = Field(..., alias="_links", description="A map of named links")
    created_at: datetime = Field(..., alias="createdAt")
    id: StrictStr = Field(...)
    tags: Optional[Tags] = None
    updated_at: datetime = Field(..., alias="updatedAt")
    audience: StrictStr = Field(...)
    cert_pem: Optional[StrictStr] = Field(..., alias="certPem")
    claims_property: StrictStr = Field(..., alias="claimsProperty")
    common_name: StrictStr = Field(..., alias="commonName")
    enabled: StrictBool = Field(...)
    external_auth_url: StrictStr = Field(..., alias="externalAuthUrl")
    fingerprint: StrictStr = Field(...)
    issuer: StrictStr = Field(...)
    jwks_endpoint: Optional[StrictStr] = Field(..., alias="jwksEndpoint")
    kid: StrictStr = Field(...)
    name: StrictStr = Field(...)
    not_after: datetime = Field(..., alias="notAfter")
    not_before: datetime = Field(..., alias="notBefore")
    use_external_id: StrictBool = Field(..., alias="useExternalId")
    __properties = ["_links", "createdAt", "id", "tags", "updatedAt", "audience", "certPem", "claimsProperty", "commonName", "enabled", "externalAuthUrl", "fingerprint", "issuer", "jwksEndpoint", "kid", "name", "notAfter", "notBefore", "useExternalId"]

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
    def from_json(cls, json_str: str) -> ExternalJwtSignerDetail:
        """Create an instance of ExternalJwtSignerDetail from a JSON string"""
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
        # set to None if cert_pem (nullable) is None
        # and __fields_set__ contains the field
        if self.cert_pem is None and "cert_pem" in self.__fields_set__:
            _dict['certPem'] = None

        # set to None if jwks_endpoint (nullable) is None
        # and __fields_set__ contains the field
        if self.jwks_endpoint is None and "jwks_endpoint" in self.__fields_set__:
            _dict['jwksEndpoint'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ExternalJwtSignerDetail:
        """Create an instance of ExternalJwtSignerDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ExternalJwtSignerDetail.parse_obj(obj)

        _obj = ExternalJwtSignerDetail.parse_obj({
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
            "audience": obj.get("audience"),
            "cert_pem": obj.get("certPem"),
            "claims_property": obj.get("claimsProperty"),
            "common_name": obj.get("commonName"),
            "enabled": obj.get("enabled"),
            "external_auth_url": obj.get("externalAuthUrl"),
            "fingerprint": obj.get("fingerprint"),
            "issuer": obj.get("issuer"),
            "jwks_endpoint": obj.get("jwksEndpoint"),
            "kid": obj.get("kid"),
            "name": obj.get("name"),
            "not_after": obj.get("notAfter"),
            "not_before": obj.get("notBefore"),
            "use_external_id": obj.get("useExternalId")
        })
        return _obj

