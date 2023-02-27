"""
    Ziti Edge Management

    OpenZiti Edge Management API  # noqa: E501

    The version of the OpenAPI document: 0.25.6
    Contact: help@openziti.org
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from openziti_edge_management.api_client import ApiClient, Endpoint as _Endpoint
from openziti_edge_management.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from openziti_edge_management.model.api_error_envelope import ApiErrorEnvelope
from openziti_edge_management.model.authenticate import Authenticate
from openziti_edge_management.model.current_api_session_detail_envelope import CurrentApiSessionDetailEnvelope
from openziti_edge_management.model.empty import Empty
from openziti_edge_management.model.mfa_code import MfaCode


class AuthenticationApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.authenticate_endpoint = _Endpoint(
            settings={
                'response_type': (CurrentApiSessionDetailEnvelope,),
                'auth': [],
                'endpoint_path': '/authenticate',
                'operation_id': 'authenticate',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'method',
                    'auth',
                ],
                'required': [
                    'method',
                ],
                'nullable': [
                ],
                'enum': [
                    'method',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('method',): {

                        "PASSWORD": "password",
                        "CERT": "cert",
                        "EXT-JWT": "ext-jwt"
                    },
                },
                'openapi_types': {
                    'method':
                        (str,),
                    'auth':
                        (Authenticate,),
                },
                'attribute_map': {
                    'method': 'method',
                },
                'location_map': {
                    'method': 'query',
                    'auth': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'default'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.authenticate_mfa_endpoint = _Endpoint(
            settings={
                'response_type': (Empty,),
                'auth': [
                    'ztSession'
                ],
                'endpoint_path': '/authenticate/mfa',
                'operation_id': 'authenticate_mfa',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'mfa_auth',
                ],
                'required': [
                    'mfa_auth',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'mfa_auth':
                        (MfaCode,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'mfa_auth': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def authenticate(
        self,
        method,
        **kwargs
    ):
        """Authenticate via a method supplied via a query string parameter  # noqa: E501

        Allows authentication  Methods include \"password\" and \"cert\"   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.authenticate(method, async_req=True)
        >>> result = thread.get()

        Args:
            method (str):

        Keyword Args:
            auth (Authenticate): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            CurrentApiSessionDetailEnvelope
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['method'] = \
            method
        return self.authenticate_endpoint.call_with_http_info(**kwargs)

    def authenticate_mfa(
        self,
        mfa_auth,
        **kwargs
    ):
        """Complete MFA authentication  # noqa: E501

        Completes MFA authentication by submitting a MFA time based one time token or backup code.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.authenticate_mfa(mfa_auth, async_req=True)
        >>> result = thread.get()

        Args:
            mfa_auth (MfaCode): An MFA validation request

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            Empty
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['mfa_auth'] = \
            mfa_auth
        return self.authenticate_mfa_endpoint.call_with_http_info(**kwargs)

