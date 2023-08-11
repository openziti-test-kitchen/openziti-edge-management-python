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
from pydantic import BaseModel, Field, StrictInt, StrictStr
from openziti_edge_management.models.mfa_formats import MfaFormats
from openziti_edge_management.models.mfa_providers import MfaProviders

class AuthQueryDetail(BaseModel):
    """
    AuthQueryDetail
    """
    format: Optional[MfaFormats] = None
    http_method: Optional[StrictStr] = Field(None, alias="httpMethod")
    http_url: Optional[StrictStr] = Field(None, alias="httpUrl")
    max_length: Optional[StrictInt] = Field(None, alias="maxLength")
    min_length: Optional[StrictInt] = Field(None, alias="minLength")
    provider: MfaProviders = Field(...)
    type_id: Optional[StrictStr] = Field(None, alias="typeId")
    __properties = ["format", "httpMethod", "httpUrl", "maxLength", "minLength", "provider", "typeId"]

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
    def from_json(cls, json_str: str) -> AuthQueryDetail:
        """Create an instance of AuthQueryDetail from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AuthQueryDetail:
        """Create an instance of AuthQueryDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AuthQueryDetail.parse_obj(obj)

        _obj = AuthQueryDetail.parse_obj({
            "format": obj.get("format"),
            "http_method": obj.get("httpMethod"),
            "http_url": obj.get("httpUrl"),
            "max_length": obj.get("maxLength"),
            "min_length": obj.get("minLength"),
            "provider": obj.get("provider"),
            "type_id": obj.get("typeId")
        })
        return _obj
