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
from pydantic import BaseModel, Field, StrictStr, conlist
from openziti_edge_management.models.os_type import OsType

class ProcessMulti(BaseModel):
    """
    ProcessMulti
    """
    hashes: Optional[conlist(StrictStr)] = None
    os_type: OsType = Field(..., alias="osType")
    path: StrictStr = Field(...)
    signer_fingerprints: Optional[conlist(StrictStr)] = Field(None, alias="signerFingerprints")
    __properties = ["hashes", "osType", "path", "signerFingerprints"]

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
    def from_json(cls, json_str: str) -> ProcessMulti:
        """Create an instance of ProcessMulti from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ProcessMulti:
        """Create an instance of ProcessMulti from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ProcessMulti.parse_obj(obj)

        _obj = ProcessMulti.parse_obj({
            "hashes": obj.get("hashes"),
            "os_type": obj.get("osType"),
            "path": obj.get("path"),
            "signer_fingerprints": obj.get("signerFingerprints")
        })
        return _obj


