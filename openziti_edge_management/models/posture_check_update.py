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
import openziti_edge_management.models


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from openziti_edge_management.models.posture_check_type import PostureCheckType
from openziti_edge_management.models.tags import Tags

class PostureCheckUpdate(BaseModel):
    """
    PostureCheckUpdate
    """
    name: StrictStr = Field(...)
    role_attributes: Optional[conlist(StrictStr)] = Field(None, alias="roleAttributes", description="A set of strings used to loosly couple this resource to policies")
    tags: Optional[Tags] = None
    type_id: Optional[PostureCheckType] = Field(None, alias="typeId")
    __properties = ["name", "roleAttributes", "tags", "typeId"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    # JSON field name that stores the object type
    __discriminator_property_name = 'typeId'

    # discriminator mappings
    __discriminator_value_class_map = {
        'postureCheckDomainUpdate': 'PostureCheckDomainUpdate',
        'postureCheckMacAddressUpdate': 'PostureCheckMacAddressUpdate',
        'postureCheckMfaUpdate': 'PostureCheckMfaUpdate',
        'postureCheckOperatingSystemUpdate': 'PostureCheckOperatingSystemUpdate',
        'postureCheckProcessMultiUpdate': 'PostureCheckProcessMultiUpdate',
        'postureCheckProcessUpdate': 'PostureCheckProcessUpdate'
    }

    @classmethod
    def get_discriminator_value(cls, obj: dict) -> str:
        """Returns the discriminator value (object type) of the data"""
        discriminator_value = obj[cls.__discriminator_property_name]
        if discriminator_value:
            return cls.__discriminator_value_class_map.get(discriminator_value)
        else:
            return None

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Union(PostureCheckDomainUpdate, PostureCheckMacAddressUpdate, PostureCheckMfaUpdate, PostureCheckOperatingSystemUpdate, PostureCheckProcessMultiUpdate, PostureCheckProcessUpdate):
        """Create an instance of PostureCheckUpdate from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of tags
        if self.tags:
            _dict['tags'] = self.tags.to_dict()
        # set to None if role_attributes (nullable) is None
        # and __fields_set__ contains the field
        if self.role_attributes is None and "role_attributes" in self.__fields_set__:
            _dict['roleAttributes'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Union(PostureCheckDomainUpdate, PostureCheckMacAddressUpdate, PostureCheckMfaUpdate, PostureCheckOperatingSystemUpdate, PostureCheckProcessMultiUpdate, PostureCheckProcessUpdate):
        """Create an instance of PostureCheckUpdate from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type:
            klass = getattr(openziti_edge_management.models, object_type)
            return klass.from_dict(obj)
        else:
            raise ValueError("PostureCheckUpdate failed to lookup discriminator value from " +
                             json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                             ", mapping: " + json.dumps(cls.__discriminator_value_class_map))

