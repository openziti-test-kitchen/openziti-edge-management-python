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
from pydantic import BaseModel
from openziti_edge_management.models.identity_enrollments_ott import IdentityEnrollmentsOtt
from openziti_edge_management.models.identity_enrollments_ottca import IdentityEnrollmentsOttca

class IdentityEnrollments(BaseModel):
    """
    IdentityEnrollments
    """
    ott: Optional[IdentityEnrollmentsOtt] = None
    ottca: Optional[IdentityEnrollmentsOttca] = None
    updb: Optional[IdentityEnrollmentsOtt] = None
    __properties = ["ott", "ottca", "updb"]

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
    def from_json(cls, json_str: str) -> IdentityEnrollments:
        """Create an instance of IdentityEnrollments from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of ott
        if self.ott:
            _dict['ott'] = self.ott.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ottca
        if self.ottca:
            _dict['ottca'] = self.ottca.to_dict()
        # override the default output from pydantic by calling `to_dict()` of updb
        if self.updb:
            _dict['updb'] = self.updb.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> IdentityEnrollments:
        """Create an instance of IdentityEnrollments from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return IdentityEnrollments.parse_obj(obj)

        _obj = IdentityEnrollments.parse_obj({
            "ott": IdentityEnrollmentsOtt.from_dict(obj.get("ott")) if obj.get("ott") is not None else None,
            "ottca": IdentityEnrollmentsOttca.from_dict(obj.get("ottca")) if obj.get("ottca") is not None else None,
            "updb": IdentityEnrollmentsOtt.from_dict(obj.get("updb")) if obj.get("updb") is not None else None
        })
        return _obj

