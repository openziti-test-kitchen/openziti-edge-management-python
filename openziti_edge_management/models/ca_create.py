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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist
from openziti_edge_management.models.external_id_claim import ExternalIdClaim
from openziti_edge_management.models.tags import Tags

class CaCreate(BaseModel):
    """
    A create Certificate Authority (CA) object
    """
    cert_pem: StrictStr = Field(..., alias="certPem")
    external_id_claim: Optional[ExternalIdClaim] = Field(None, alias="externalIdClaim")
    identity_name_format: Optional[StrictStr] = Field(None, alias="identityNameFormat")
    identity_roles: conlist(StrictStr) = Field(..., alias="identityRoles")
    is_auth_enabled: StrictBool = Field(..., alias="isAuthEnabled")
    is_auto_ca_enrollment_enabled: StrictBool = Field(..., alias="isAutoCaEnrollmentEnabled")
    is_ott_ca_enrollment_enabled: StrictBool = Field(..., alias="isOttCaEnrollmentEnabled")
    name: StrictStr = Field(...)
    tags: Optional[Tags] = None
    __properties = ["certPem", "externalIdClaim", "identityNameFormat", "identityRoles", "isAuthEnabled", "isAutoCaEnrollmentEnabled", "isOttCaEnrollmentEnabled", "name", "tags"]

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
    def from_json(cls, json_str: str) -> CaCreate:
        """Create an instance of CaCreate from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of external_id_claim
        if self.external_id_claim:
            _dict['externalIdClaim'] = self.external_id_claim.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tags
        if self.tags:
            _dict['tags'] = self.tags.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CaCreate:
        """Create an instance of CaCreate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CaCreate.parse_obj(obj)

        _obj = CaCreate.parse_obj({
            "cert_pem": obj.get("certPem"),
            "external_id_claim": ExternalIdClaim.from_dict(obj.get("externalIdClaim")) if obj.get("externalIdClaim") is not None else None,
            "identity_name_format": obj.get("identityNameFormat"),
            "identity_roles": obj.get("identityRoles"),
            "is_auth_enabled": obj.get("isAuthEnabled"),
            "is_auto_ca_enrollment_enabled": obj.get("isAutoCaEnrollmentEnabled"),
            "is_ott_ca_enrollment_enabled": obj.get("isOttCaEnrollmentEnabled"),
            "name": obj.get("name"),
            "tags": Tags.from_dict(obj.get("tags")) if obj.get("tags") is not None else None
        })
        return _obj

