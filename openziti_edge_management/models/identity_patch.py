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


from typing import Dict, List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, conint, conlist
from openziti_edge_management.models.identity_type import IdentityType
from openziti_edge_management.models.tags import Tags
from openziti_edge_management.models.terminator_precedence import TerminatorPrecedence

class IdentityPatch(BaseModel):
    """
    IdentityPatch
    """
    app_data: Optional[Tags] = Field(None, alias="appData")
    auth_policy_id: Optional[StrictStr] = Field(None, alias="authPolicyId")
    default_hosting_cost: Optional[conint(strict=True, le=65535, ge=0)] = Field(None, alias="defaultHostingCost")
    default_hosting_precedence: Optional[TerminatorPrecedence] = Field(None, alias="defaultHostingPrecedence")
    external_id: Optional[StrictStr] = Field(None, alias="externalId")
    is_admin: Optional[StrictBool] = Field(None, alias="isAdmin")
    name: Optional[StrictStr] = None
    role_attributes: Optional[conlist(StrictStr)] = Field(None, alias="roleAttributes", description="A set of strings used to loosly couple this resource to policies")
    service_hosting_costs: Optional[Dict[str, conint(strict=True, le=65535, ge=0)]] = Field(None, alias="serviceHostingCosts")
    service_hosting_precedences: Optional[Dict[str, TerminatorPrecedence]] = Field(None, alias="serviceHostingPrecedences")
    tags: Optional[Tags] = None
    type: Optional[IdentityType] = None
    __properties = ["appData", "authPolicyId", "defaultHostingCost", "defaultHostingPrecedence", "externalId", "isAdmin", "name", "roleAttributes", "serviceHostingCosts", "serviceHostingPrecedences", "tags", "type"]

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
    def from_json(cls, json_str: str) -> IdentityPatch:
        """Create an instance of IdentityPatch from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of app_data
        if self.app_data:
            _dict['appData'] = self.app_data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tags
        if self.tags:
            _dict['tags'] = self.tags.to_dict()
        # set to None if auth_policy_id (nullable) is None
        # and __fields_set__ contains the field
        if self.auth_policy_id is None and "auth_policy_id" in self.__fields_set__:
            _dict['authPolicyId'] = None

        # set to None if external_id (nullable) is None
        # and __fields_set__ contains the field
        if self.external_id is None and "external_id" in self.__fields_set__:
            _dict['externalId'] = None

        # set to None if is_admin (nullable) is None
        # and __fields_set__ contains the field
        if self.is_admin is None and "is_admin" in self.__fields_set__:
            _dict['isAdmin'] = None

        # set to None if name (nullable) is None
        # and __fields_set__ contains the field
        if self.name is None and "name" in self.__fields_set__:
            _dict['name'] = None

        # set to None if role_attributes (nullable) is None
        # and __fields_set__ contains the field
        if self.role_attributes is None and "role_attributes" in self.__fields_set__:
            _dict['roleAttributes'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> IdentityPatch:
        """Create an instance of IdentityPatch from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return IdentityPatch.parse_obj(obj)

        _obj = IdentityPatch.parse_obj({
            "app_data": Tags.from_dict(obj.get("appData")) if obj.get("appData") is not None else None,
            "auth_policy_id": obj.get("authPolicyId"),
            "default_hosting_cost": obj.get("defaultHostingCost"),
            "default_hosting_precedence": obj.get("defaultHostingPrecedence"),
            "external_id": obj.get("externalId"),
            "is_admin": obj.get("isAdmin"),
            "name": obj.get("name"),
            "role_attributes": obj.get("roleAttributes"),
            "service_hosting_costs": obj.get("serviceHostingCosts"),
            "service_hosting_precedences": dict((_k, _v) for _k, _v in obj.get("serviceHostingPrecedences").items()),
            "tags": Tags.from_dict(obj.get("tags")) if obj.get("tags") is not None else None,
            "type": obj.get("type")
        })
        return _obj


