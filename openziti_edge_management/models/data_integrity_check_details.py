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

from datetime import datetime
from typing import List
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist
from openziti_edge_management.models.data_integrity_check_detail import DataIntegrityCheckDetail

class DataIntegrityCheckDetails(BaseModel):
    """
    DataIntegrityCheckDetails
    """
    end_time: datetime = Field(..., alias="endTime")
    error: StrictStr = Field(...)
    fixing_errors: StrictBool = Field(..., alias="fixingErrors")
    in_progress: StrictBool = Field(..., alias="inProgress")
    results: conlist(DataIntegrityCheckDetail) = Field(...)
    start_time: datetime = Field(..., alias="startTime")
    too_many_errors: StrictBool = Field(..., alias="tooManyErrors")
    __properties = ["endTime", "error", "fixingErrors", "inProgress", "results", "startTime", "tooManyErrors"]

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
    def from_json(cls, json_str: str) -> DataIntegrityCheckDetails:
        """Create an instance of DataIntegrityCheckDetails from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in results (list)
        _items = []
        if self.results:
            for _item in self.results:
                if _item:
                    _items.append(_item.to_dict())
            _dict['results'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DataIntegrityCheckDetails:
        """Create an instance of DataIntegrityCheckDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DataIntegrityCheckDetails.parse_obj(obj)

        _obj = DataIntegrityCheckDetails.parse_obj({
            "end_time": obj.get("endTime"),
            "error": obj.get("error"),
            "fixing_errors": obj.get("fixingErrors"),
            "in_progress": obj.get("inProgress"),
            "results": [DataIntegrityCheckDetail.from_dict(_item) for _item in obj.get("results")] if obj.get("results") is not None else None,
            "start_time": obj.get("startTime"),
            "too_many_errors": obj.get("tooManyErrors")
        })
        return _obj
