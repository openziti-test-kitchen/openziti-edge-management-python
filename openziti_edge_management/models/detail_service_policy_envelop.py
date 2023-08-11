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



from pydantic import BaseModel, Field
from openziti_edge_management.models.meta import Meta
from openziti_edge_management.models.service_policy_detail import ServicePolicyDetail

class DetailServicePolicyEnvelop(BaseModel):
    """
    DetailServicePolicyEnvelop
    """
    data: ServicePolicyDetail = Field(...)
    meta: Meta = Field(...)
    __properties = ["data", "meta"]

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
    def from_json(cls, json_str: str) -> DetailServicePolicyEnvelop:
        """Create an instance of DetailServicePolicyEnvelop from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of data
        if self.data:
            _dict['data'] = self.data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of meta
        if self.meta:
            _dict['meta'] = self.meta.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DetailServicePolicyEnvelop:
        """Create an instance of DetailServicePolicyEnvelop from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DetailServicePolicyEnvelop.parse_obj(obj)

        _obj = DetailServicePolicyEnvelop.parse_obj({
            "data": ServicePolicyDetail.from_dict(obj.get("data")) if obj.get("data") is not None else None,
            "meta": Meta.from_dict(obj.get("meta")) if obj.get("meta") is not None else None
        })
        return _obj


