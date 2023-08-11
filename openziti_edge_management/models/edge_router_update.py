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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, conint, conlist
from openziti_edge_management.models.tags import Tags

class EdgeRouterUpdate(BaseModel):
    """
    An edge router update object
    """
    app_data: Optional[Tags] = Field(None, alias="appData")
    cost: Optional[conint(strict=True, le=65535, ge=0)] = None
    disabled: Optional[StrictBool] = None
    is_tunneler_enabled: Optional[StrictBool] = Field(None, alias="isTunnelerEnabled")
    name: StrictStr = Field(...)
    no_traversal: Optional[StrictBool] = Field(None, alias="noTraversal")
    role_attributes: Optional[conlist(StrictStr)] = Field(None, alias="roleAttributes", description="A set of strings used to loosly couple this resource to policies")
    tags: Optional[Tags] = None
    __properties = ["appData", "cost", "disabled", "isTunnelerEnabled", "name", "noTraversal", "roleAttributes", "tags"]

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
    def from_json(cls, json_str: str) -> EdgeRouterUpdate:
        """Create an instance of EdgeRouterUpdate from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of app_data
        if self.app_data:
            _dict['appData'] = self.app_data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tags
        if self.tags:
            _dict['tags'] = self.tags.to_dict()
        # set to None if cost (nullable) is None
        # and __fields_set__ contains the field
        if self.cost is None and "cost" in self.__fields_set__:
            _dict['cost'] = None

        # set to None if disabled (nullable) is None
        # and __fields_set__ contains the field
        if self.disabled is None and "disabled" in self.__fields_set__:
            _dict['disabled'] = None

        # set to None if no_traversal (nullable) is None
        # and __fields_set__ contains the field
        if self.no_traversal is None and "no_traversal" in self.__fields_set__:
            _dict['noTraversal'] = None

        # set to None if role_attributes (nullable) is None
        # and __fields_set__ contains the field
        if self.role_attributes is None and "role_attributes" in self.__fields_set__:
            _dict['roleAttributes'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EdgeRouterUpdate:
        """Create an instance of EdgeRouterUpdate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EdgeRouterUpdate.parse_obj(obj)

        _obj = EdgeRouterUpdate.parse_obj({
            "app_data": Tags.from_dict(obj.get("appData")) if obj.get("appData") is not None else None,
            "cost": obj.get("cost"),
            "disabled": obj.get("disabled"),
            "is_tunneler_enabled": obj.get("isTunnelerEnabled"),
            "name": obj.get("name"),
            "no_traversal": obj.get("noTraversal"),
            "role_attributes": obj.get("roleAttributes"),
            "tags": Tags.from_dict(obj.get("tags")) if obj.get("tags") is not None else None
        })
        return _obj

