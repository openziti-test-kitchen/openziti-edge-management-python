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


from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictStr
from openziti_edge_management.models.api_error_args import ApiErrorArgs

class ApiErrorCause(BaseModel):
    """
    ApiErrorCause
    """
    field: Optional[StrictStr] = None
    reason: Optional[StrictStr] = None
    value: Optional[Dict[str, Any]] = Field(None, description="can be any value - string, number, boolean, array or object")
    args: Optional[ApiErrorArgs] = None
    cause: Optional[ApiErrorCause] = None
    cause_message: Optional[StrictStr] = Field(None, alias="causeMessage")
    code: Optional[StrictStr] = None
    data: Optional[Dict[str, Any]] = None
    message: Optional[StrictStr] = None
    request_id: Optional[StrictStr] = Field(None, alias="requestId")
    __properties = ["field", "reason", "value", "args", "cause", "causeMessage", "code", "data", "message", "requestId"]

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
    def from_json(cls, json_str: str) -> ApiErrorCause:
        """Create an instance of ApiErrorCause from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of args
        if self.args:
            _dict['args'] = self.args.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cause
        if self.cause:
            _dict['cause'] = self.cause.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiErrorCause:
        """Create an instance of ApiErrorCause from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiErrorCause.parse_obj(obj)

        _obj = ApiErrorCause.parse_obj({
            "field": obj.get("field"),
            "reason": obj.get("reason"),
            "value": obj.get("value"),
            "args": ApiErrorArgs.from_dict(obj.get("args")) if obj.get("args") is not None else None,
            "cause": ApiErrorCause.from_dict(obj.get("cause")) if obj.get("cause") is not None else None,
            "cause_message": obj.get("causeMessage"),
            "code": obj.get("code"),
            "data": obj.get("data"),
            "message": obj.get("message"),
            "request_id": obj.get("requestId")
        })
        return _obj

