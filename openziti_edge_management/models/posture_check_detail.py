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

from datetime import datetime
from typing import Dict, List, Optional, Union
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist
from openziti_edge_management.models.link import Link
from openziti_edge_management.models.tags import Tags

class PostureCheckDetail(BaseModel):
    """
    PostureCheckDetail
    """
    links: Dict[str, Link] = Field(..., alias="_links", description="A map of named links")
    created_at: datetime = Field(..., alias="createdAt")
    id: StrictStr = Field(...)
    name: StrictStr = Field(...)
    role_attributes: Optional[conlist(StrictStr)] = Field(..., alias="roleAttributes", description="A set of strings used to loosly couple this resource to policies")
    tags: Tags = Field(...)
    type_id: StrictStr = Field(..., alias="typeId")
    updated_at: datetime = Field(..., alias="updatedAt")
    version: StrictInt = Field(...)
    __properties = ["_links", "createdAt", "id", "name", "roleAttributes", "tags", "typeId", "updatedAt", "version"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    # JSON field name that stores the object type
    __discriminator_property_name = 'typeId'

    # discriminator mappings
    __discriminator_value_class_map = {
        'postureCheckDomainDetail': 'PostureCheckDomainDetail',
        'postureCheckMacAddressDetail': 'PostureCheckMacAddressDetail',
        'postureCheckMfaDetail': 'PostureCheckMfaDetail',
        'postureCheckOperatingSystemDetail': 'PostureCheckOperatingSystemDetail',
        'postureCheckProcessDetail': 'PostureCheckProcessDetail',
        'postureCheckProcessMultiDetail': 'PostureCheckProcessMultiDetail'
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
    def from_json(cls, json_str: str) -> Union(PostureCheckDomainDetail, PostureCheckMacAddressDetail, PostureCheckMfaDetail, PostureCheckOperatingSystemDetail, PostureCheckProcessDetail, PostureCheckProcessMultiDetail):
        """Create an instance of PostureCheckDetail from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each value in links (dict)
        _field_dict = {}
        if self.links:
            for _key in self.links:
                if self.links[_key]:
                    _field_dict[_key] = self.links[_key].to_dict()
            _dict['_links'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of tags
        if self.tags:
            _dict['tags'] = self.tags.to_dict()
        # set to None if role_attributes (nullable) is None
        # and __fields_set__ contains the field
        if self.role_attributes is None and "role_attributes" in self.__fields_set__:
            _dict['roleAttributes'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Union(PostureCheckDomainDetail, PostureCheckMacAddressDetail, PostureCheckMfaDetail, PostureCheckOperatingSystemDetail, PostureCheckProcessDetail, PostureCheckProcessMultiDetail):
        """Create an instance of PostureCheckDetail from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type:
            klass = globals()[object_type]
            return klass.from_dict(obj)
        else:
            raise ValueError("PostureCheckDetail failed to lookup discriminator value from " +
                             json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                             ", mapping: " + json.dumps(cls.__discriminator_value_class_map))

from openziti_edge_management.models.posture_check_domain_detail import postureCheckDomainDetail
from openziti_edge_management.models.posture_check_mac_address_detail import postureCheckMacAddressDetail
from openziti_edge_management.models.posture_check_mfa_detail import postureCheckMfaDetail
from openziti_edge_management.models.posture_check_operating_system_detail import postureCheckOperatingSystemDetail
from openziti_edge_management.models.posture_check_process_detail import postureCheckProcessDetail
from openziti_edge_management.models.posture_check_process_multi_detail import postureCheckProcessMultiDetail
PostureCheckDetail.update_forward_refs()

