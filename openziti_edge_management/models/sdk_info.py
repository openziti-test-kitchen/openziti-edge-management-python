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

class SdkInfo(BaseModel):
    """
    SDK information an authenticating client may provide
    """
    app_id: Optional[StrictStr] = Field(None, alias="appId")
    app_version: Optional[StrictStr] = Field(None, alias="appVersion")
    branch: Optional[StrictStr] = None
    revision: Optional[StrictStr] = None
    type: Optional[StrictStr] = None
    version: Optional[StrictStr] = None
    __properties = ["appId", "appVersion", "branch", "revision", "type", "version"]

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
    def from_json(cls, json_str: str) -> SdkInfo:
        """Create an instance of SdkInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SdkInfo:
        """Create an instance of SdkInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SdkInfo.parse_obj(obj)

        _obj = SdkInfo.parse_obj({
            "app_id": obj.get("appId"),
            "app_version": obj.get("appVersion"),
            "branch": obj.get("branch"),
            "revision": obj.get("revision"),
            "type": obj.get("type"),
            "version": obj.get("version")
        })
        return _obj
