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
from pydantic import BaseModel, Field, StrictBool, StrictStr, conint, conlist
from openziti_edge_management.models.entity_ref import EntityRef
from openziti_edge_management.models.env_info import EnvInfo
from openziti_edge_management.models.identity_authenticators import IdentityAuthenticators
from openziti_edge_management.models.identity_enrollments import IdentityEnrollments
from openziti_edge_management.models.link import Link
from openziti_edge_management.models.sdk_info import SdkInfo
from openziti_edge_management.models.tags import Tags
from openziti_edge_management.models.terminator_precedence import TerminatorPrecedence

class IdentityDetail(BaseModel):
    """
    Detail of a specific identity
    """
    links: Dict[str, Link] = Field(..., alias="_links", description="A map of named links")
    created_at: datetime = Field(..., alias="createdAt")
    id: StrictStr = Field(...)
    tags: Optional[Tags] = None
    updated_at: datetime = Field(..., alias="updatedAt")
    app_data: Optional[Tags] = Field(None, alias="appData")
    auth_policy: EntityRef = Field(..., alias="authPolicy")
    auth_policy_id: StrictStr = Field(..., alias="authPolicyId")
    authenticators: IdentityAuthenticators = Field(...)
    default_hosting_cost: conint(strict=True, le=65535, ge=0) = Field(..., alias="defaultHostingCost")
    default_hosting_precedence: Optional[TerminatorPrecedence] = Field(None, alias="defaultHostingPrecedence")
    disabled: StrictBool = Field(...)
    disabled_at: Optional[datetime] = Field(None, alias="disabledAt")
    disabled_until: Optional[datetime] = Field(None, alias="disabledUntil")
    enrollment: IdentityEnrollments = Field(...)
    env_info: EnvInfo = Field(..., alias="envInfo")
    external_id: Optional[StrictStr] = Field(..., alias="externalId")
    has_api_session: StrictBool = Field(..., alias="hasApiSession")
    has_edge_router_connection: StrictBool = Field(..., alias="hasEdgeRouterConnection")
    is_admin: StrictBool = Field(..., alias="isAdmin")
    is_default_admin: StrictBool = Field(..., alias="isDefaultAdmin")
    is_mfa_enabled: StrictBool = Field(..., alias="isMfaEnabled")
    name: StrictStr = Field(...)
    role_attributes: Optional[conlist(StrictStr)] = Field(..., alias="roleAttributes", description="A set of strings used to loosly couple this resource to policies")
    sdk_info: SdkInfo = Field(..., alias="sdkInfo")
    service_hosting_costs: Dict[str, conint(strict=True, le=65535, ge=0)] = Field(..., alias="serviceHostingCosts")
    service_hosting_precedences: Dict[str, TerminatorPrecedence] = Field(..., alias="serviceHostingPrecedences")
    type: EntityRef = Field(...)
    type_id: StrictStr = Field(..., alias="typeId")
    __properties = ["_links", "createdAt", "id", "tags", "updatedAt", "appData", "authPolicy", "authPolicyId", "authenticators", "defaultHostingCost", "defaultHostingPrecedence", "disabled", "disabledAt", "disabledUntil", "enrollment", "envInfo", "externalId", "hasApiSession", "hasEdgeRouterConnection", "isAdmin", "isDefaultAdmin", "isMfaEnabled", "name", "roleAttributes", "sdkInfo", "serviceHostingCosts", "serviceHostingPrecedences", "type", "typeId"]

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
    def from_json(cls, json_str: str) -> IdentityDetail:
        """Create an instance of IdentityDetail from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of auth_policy
        if self.auth_policy:
            _dict['authPolicy'] = self.auth_policy.to_dict()
        # override the default output from pydantic by calling `to_dict()` of authenticators
        if self.authenticators:
            _dict['authenticators'] = self.authenticators.to_dict()
        # override the default output from pydantic by calling `to_dict()` of enrollment
        if self.enrollment:
            _dict['enrollment'] = self.enrollment.to_dict()
        # override the default output from pydantic by calling `to_dict()` of env_info
        if self.env_info:
            _dict['envInfo'] = self.env_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sdk_info
        if self.sdk_info:
            _dict['sdkInfo'] = self.sdk_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of type
        if self.type:
            _dict['type'] = self.type.to_dict()
        # set to None if disabled_at (nullable) is None
        # and __fields_set__ contains the field
        if self.disabled_at is None and "disabled_at" in self.__fields_set__:
            _dict['disabledAt'] = None

        # set to None if disabled_until (nullable) is None
        # and __fields_set__ contains the field
        if self.disabled_until is None and "disabled_until" in self.__fields_set__:
            _dict['disabledUntil'] = None

        # set to None if external_id (nullable) is None
        # and __fields_set__ contains the field
        if self.external_id is None and "external_id" in self.__fields_set__:
            _dict['externalId'] = None

        # set to None if role_attributes (nullable) is None
        # and __fields_set__ contains the field
        if self.role_attributes is None and "role_attributes" in self.__fields_set__:
            _dict['roleAttributes'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> IdentityDetail:
        """Create an instance of IdentityDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return IdentityDetail.parse_obj(obj)

        _obj = IdentityDetail.parse_obj({
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
            "auth_policy": EntityRef.from_dict(obj.get("authPolicy")) if obj.get("authPolicy") is not None else None,
            "auth_policy_id": obj.get("authPolicyId"),
            "authenticators": IdentityAuthenticators.from_dict(obj.get("authenticators")) if obj.get("authenticators") is not None else None,
            "default_hosting_cost": obj.get("defaultHostingCost"),
            "default_hosting_precedence": obj.get("defaultHostingPrecedence"),
            "disabled": obj.get("disabled"),
            "disabled_at": obj.get("disabledAt"),
            "disabled_until": obj.get("disabledUntil"),
            "enrollment": IdentityEnrollments.from_dict(obj.get("enrollment")) if obj.get("enrollment") is not None else None,
            "env_info": EnvInfo.from_dict(obj.get("envInfo")) if obj.get("envInfo") is not None else None,
            "external_id": obj.get("externalId"),
            "has_api_session": obj.get("hasApiSession"),
            "has_edge_router_connection": obj.get("hasEdgeRouterConnection"),
            "is_admin": obj.get("isAdmin"),
            "is_default_admin": obj.get("isDefaultAdmin"),
            "is_mfa_enabled": obj.get("isMfaEnabled"),
            "name": obj.get("name"),
            "role_attributes": obj.get("roleAttributes"),
            "sdk_info": SdkInfo.from_dict(obj.get("sdkInfo")) if obj.get("sdkInfo") is not None else None,
            "service_hosting_costs": obj.get("serviceHostingCosts"),
            "service_hosting_precedences": dict((_k, _v) for _k, _v in obj.get("serviceHostingPrecedences").items()),
            "type": EntityRef.from_dict(obj.get("type")) if obj.get("type") is not None else None,
            "type_id": obj.get("typeId")
        })
        return _obj

