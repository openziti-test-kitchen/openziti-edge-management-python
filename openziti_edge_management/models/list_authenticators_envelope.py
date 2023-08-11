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


from typing import List, Optional
from pydantic import BaseModel, Field, conlist
from openziti_edge_management.models.authenticator_detail import AuthenticatorDetail
from openziti_edge_management.models.meta import Meta

class ListAuthenticatorsEnvelope(BaseModel):
    """
    ListAuthenticatorsEnvelope
    """
    data: Optional[conlist(AuthenticatorDetail)] = Field(None, description="An array of authenticator resources")
    meta: Optional[Meta] = None
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
    def from_json(cls, json_str: str) -> ListAuthenticatorsEnvelope:
        """Create an instance of ListAuthenticatorsEnvelope from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in data (list)
        _items = []
        if self.data:
            for _item in self.data:
                if _item:
                    _items.append(_item.to_dict())
            _dict['data'] = _items
        # override the default output from pydantic by calling `to_dict()` of meta
        if self.meta:
            _dict['meta'] = self.meta.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ListAuthenticatorsEnvelope:
        """Create an instance of ListAuthenticatorsEnvelope from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ListAuthenticatorsEnvelope.parse_obj(obj)

        _obj = ListAuthenticatorsEnvelope.parse_obj({
            "data": [AuthenticatorDetail.from_dict(_item) for _item in obj.get("data")] if obj.get("data") is not None else None,
            "meta": Meta.from_dict(obj.get("meta")) if obj.get("meta") is not None else None
        })
        return _obj


