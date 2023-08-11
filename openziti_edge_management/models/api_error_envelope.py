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



from pydantic import BaseModel, Field
from openziti_edge_management.models.api_error import ApiError
from openziti_edge_management.models.meta import Meta

class ApiErrorEnvelope(BaseModel):
    """
    ApiErrorEnvelope
    """
    error: ApiError = Field(...)
    meta: Meta = Field(...)
    __properties = ["error", "meta"]

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
    def from_json(cls, json_str: str) -> ApiErrorEnvelope:
        """Create an instance of ApiErrorEnvelope from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of error
        if self.error:
            _dict['error'] = self.error.to_dict()
        # override the default output from pydantic by calling `to_dict()` of meta
        if self.meta:
            _dict['meta'] = self.meta.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiErrorEnvelope:
        """Create an instance of ApiErrorEnvelope from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiErrorEnvelope.parse_obj(obj)

        _obj = ApiErrorEnvelope.parse_obj({
            "error": ApiError.from_dict(obj.get("error")) if obj.get("error") is not None else None,
            "meta": Meta.from_dict(obj.get("meta")) if obj.get("meta") is not None else None
        })
        return _obj

