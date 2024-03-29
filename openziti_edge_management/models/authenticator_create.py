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


from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from openziti_edge_management.models.tags import Tags

class AuthenticatorCreate(BaseModel):
    """
    Creates an authenticator for a specific identity which can be used for API authentication
    """
    cert_pem: Optional[StrictStr] = Field(None, alias="certPem", description="The client certificate the identity will login with. Used only for method='cert'")
    identity_id: StrictStr = Field(..., alias="identityId", description="The id of an existing identity that will be assigned this authenticator")
    method: StrictStr = Field(..., description="The type of authenticator to create; which will dictate which properties on this object are required.")
    password: Optional[StrictStr] = Field(None, description="The password the identity will login with. Used only for method='updb'")
    tags: Optional[Tags] = None
    username: Optional[StrictStr] = Field(None, description="The username that the identity will login with. Used only for method='updb'")
    __properties = ["certPem", "identityId", "method", "password", "tags", "username"]

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
    def from_json(cls, json_str: str) -> AuthenticatorCreate:
        """Create an instance of AuthenticatorCreate from a JSON string"""
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
    def from_dict(cls, obj: dict) -> AuthenticatorCreate:
        """Create an instance of AuthenticatorCreate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AuthenticatorCreate.parse_obj(obj)

        _obj = AuthenticatorCreate.parse_obj({
            "cert_pem": obj.get("certPem"),
            "identity_id": obj.get("identityId"),
            "method": obj.get("method"),
            "password": obj.get("password"),
            "tags": Tags.from_dict(obj.get("tags")) if obj.get("tags") is not None else None,
            "username": obj.get("username")
        })
        return _obj

