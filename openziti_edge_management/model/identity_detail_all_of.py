"""
    Ziti Edge Management

    OpenZiti Edge Management API  # noqa: E501

    The version of the OpenAPI document: 0.25.31
    Contact: help@openziti.org
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from openziti_edge_management.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from openziti_edge_management.exceptions import ApiAttributeError


def lazy_import():
    from openziti_edge_management.model.attributes import Attributes
    from openziti_edge_management.model.entity_ref import EntityRef
    from openziti_edge_management.model.env_info import EnvInfo
    from openziti_edge_management.model.identity_authenticators import IdentityAuthenticators
    from openziti_edge_management.model.identity_enrollments import IdentityEnrollments
    from openziti_edge_management.model.sdk_info import SdkInfo
    from openziti_edge_management.model.tags import Tags
    from openziti_edge_management.model.terminator_cost import TerminatorCost
    from openziti_edge_management.model.terminator_cost_map import TerminatorCostMap
    from openziti_edge_management.model.terminator_precedence import TerminatorPrecedence
    from openziti_edge_management.model.terminator_precedence_map import TerminatorPrecedenceMap
    globals()['Attributes'] = Attributes
    globals()['EntityRef'] = EntityRef
    globals()['EnvInfo'] = EnvInfo
    globals()['IdentityAuthenticators'] = IdentityAuthenticators
    globals()['IdentityEnrollments'] = IdentityEnrollments
    globals()['SdkInfo'] = SdkInfo
    globals()['Tags'] = Tags
    globals()['TerminatorCost'] = TerminatorCost
    globals()['TerminatorCostMap'] = TerminatorCostMap
    globals()['TerminatorPrecedence'] = TerminatorPrecedence
    globals()['TerminatorPrecedenceMap'] = TerminatorPrecedenceMap


class IdentityDetailAllOf(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'auth_policy': (EntityRef,),  # noqa: E501
            'auth_policy_id': (str,),  # noqa: E501
            'authenticators': (IdentityAuthenticators,),  # noqa: E501
            'default_hosting_cost': (TerminatorCost,),  # noqa: E501
            'disabled': (bool,),  # noqa: E501
            'enrollment': (IdentityEnrollments,),  # noqa: E501
            'env_info': (EnvInfo,),  # noqa: E501
            'external_id': (str, none_type,),  # noqa: E501
            'has_api_session': (bool,),  # noqa: E501
            'has_edge_router_connection': (bool,),  # noqa: E501
            'is_admin': (bool,),  # noqa: E501
            'is_default_admin': (bool,),  # noqa: E501
            'is_mfa_enabled': (bool,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'role_attributes': (Attributes,),  # noqa: E501
            'sdk_info': (SdkInfo,),  # noqa: E501
            'service_hosting_costs': (TerminatorCostMap,),  # noqa: E501
            'service_hosting_precedences': (TerminatorPrecedenceMap,),  # noqa: E501
            'type': (EntityRef,),  # noqa: E501
            'type_id': (str,),  # noqa: E501
            'app_data': (Tags,),  # noqa: E501
            'default_hosting_precedence': (TerminatorPrecedence,),  # noqa: E501
            'disabled_at': (datetime, none_type,),  # noqa: E501
            'disabled_until': (datetime, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'auth_policy': 'authPolicy',  # noqa: E501
        'auth_policy_id': 'authPolicyId',  # noqa: E501
        'authenticators': 'authenticators',  # noqa: E501
        'default_hosting_cost': 'defaultHostingCost',  # noqa: E501
        'disabled': 'disabled',  # noqa: E501
        'enrollment': 'enrollment',  # noqa: E501
        'env_info': 'envInfo',  # noqa: E501
        'external_id': 'externalId',  # noqa: E501
        'has_api_session': 'hasApiSession',  # noqa: E501
        'has_edge_router_connection': 'hasEdgeRouterConnection',  # noqa: E501
        'is_admin': 'isAdmin',  # noqa: E501
        'is_default_admin': 'isDefaultAdmin',  # noqa: E501
        'is_mfa_enabled': 'isMfaEnabled',  # noqa: E501
        'name': 'name',  # noqa: E501
        'role_attributes': 'roleAttributes',  # noqa: E501
        'sdk_info': 'sdkInfo',  # noqa: E501
        'service_hosting_costs': 'serviceHostingCosts',  # noqa: E501
        'service_hosting_precedences': 'serviceHostingPrecedences',  # noqa: E501
        'type': 'type',  # noqa: E501
        'type_id': 'typeId',  # noqa: E501
        'app_data': 'appData',  # noqa: E501
        'default_hosting_precedence': 'defaultHostingPrecedence',  # noqa: E501
        'disabled_at': 'disabledAt',  # noqa: E501
        'disabled_until': 'disabledUntil',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, auth_policy, auth_policy_id, authenticators, default_hosting_cost, disabled, enrollment, env_info, external_id, has_api_session, has_edge_router_connection, is_admin, is_default_admin, is_mfa_enabled, name, role_attributes, sdk_info, service_hosting_costs, service_hosting_precedences, type, type_id, *args, **kwargs):  # noqa: E501
        """IdentityDetailAllOf - a model defined in OpenAPI

        Args:
            auth_policy (EntityRef):
            auth_policy_id (str):
            authenticators (IdentityAuthenticators):
            default_hosting_cost (TerminatorCost):
            disabled (bool):
            enrollment (IdentityEnrollments):
            env_info (EnvInfo):
            external_id (str, none_type):
            has_api_session (bool):
            has_edge_router_connection (bool):
            is_admin (bool):
            is_default_admin (bool):
            is_mfa_enabled (bool):
            name (str):
            role_attributes (Attributes):
            sdk_info (SdkInfo):
            service_hosting_costs (TerminatorCostMap):
            service_hosting_precedences (TerminatorPrecedenceMap):
            type (EntityRef):
            type_id (str):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            app_data (Tags): [optional]  # noqa: E501
            default_hosting_precedence (TerminatorPrecedence): [optional]  # noqa: E501
            disabled_at (datetime, none_type): [optional]  # noqa: E501
            disabled_until (datetime, none_type): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', True)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.auth_policy = auth_policy
        self.auth_policy_id = auth_policy_id
        self.authenticators = authenticators
        self.default_hosting_cost = default_hosting_cost
        self.disabled = disabled
        self.enrollment = enrollment
        self.env_info = env_info
        self.external_id = external_id
        self.has_api_session = has_api_session
        self.has_edge_router_connection = has_edge_router_connection
        self.is_admin = is_admin
        self.is_default_admin = is_default_admin
        self.is_mfa_enabled = is_mfa_enabled
        self.name = name
        self.role_attributes = role_attributes
        self.sdk_info = sdk_info
        self.service_hosting_costs = service_hosting_costs
        self.service_hosting_precedences = service_hosting_precedences
        self.type = type
        self.type_id = type_id
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, auth_policy, auth_policy_id, authenticators, default_hosting_cost, disabled, enrollment, env_info, external_id, has_api_session, has_edge_router_connection, is_admin, is_default_admin, is_mfa_enabled, name, role_attributes, sdk_info, service_hosting_costs, service_hosting_precedences, type, type_id, *args, **kwargs):  # noqa: E501
        """IdentityDetailAllOf - a model defined in OpenAPI

        Args:
            auth_policy (EntityRef):
            auth_policy_id (str):
            authenticators (IdentityAuthenticators):
            default_hosting_cost (TerminatorCost):
            disabled (bool):
            enrollment (IdentityEnrollments):
            env_info (EnvInfo):
            external_id (str, none_type):
            has_api_session (bool):
            has_edge_router_connection (bool):
            is_admin (bool):
            is_default_admin (bool):
            is_mfa_enabled (bool):
            name (str):
            role_attributes (Attributes):
            sdk_info (SdkInfo):
            service_hosting_costs (TerminatorCostMap):
            service_hosting_precedences (TerminatorPrecedenceMap):
            type (EntityRef):
            type_id (str):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            app_data (Tags): [optional]  # noqa: E501
            default_hosting_precedence (TerminatorPrecedence): [optional]  # noqa: E501
            disabled_at (datetime, none_type): [optional]  # noqa: E501
            disabled_until (datetime, none_type): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.auth_policy = auth_policy
        self.auth_policy_id = auth_policy_id
        self.authenticators = authenticators
        self.default_hosting_cost = default_hosting_cost
        self.disabled = disabled
        self.enrollment = enrollment
        self.env_info = env_info
        self.external_id = external_id
        self.has_api_session = has_api_session
        self.has_edge_router_connection = has_edge_router_connection
        self.is_admin = is_admin
        self.is_default_admin = is_default_admin
        self.is_mfa_enabled = is_mfa_enabled
        self.name = name
        self.role_attributes = role_attributes
        self.sdk_info = sdk_info
        self.service_hosting_costs = service_hosting_costs
        self.service_hosting_precedences = service_hosting_precedences
        self.type = type
        self.type_id = type_id
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
