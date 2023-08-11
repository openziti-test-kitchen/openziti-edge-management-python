# coding: utf-8

"""
    Ziti Edge Management

    OpenZiti Edge Management API  # noqa: E501

    The version of the OpenAPI document: 0.25.31
    Contact: help@openziti.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError
from typing_extensions import Annotated

from pydantic import Field, StrictStr

from openziti_edge_management.models.trace_detail_envelope import TraceDetailEnvelope
from openziti_edge_management.models.trace_spec import TraceSpec

from openziti_edge_management.api_client import ApiClient
from openziti_edge_management.api_response import ApiResponse
from openziti_edge_management.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class TracingApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def update_identity_tracing(self, id : Annotated[StrictStr, Field(..., description="The id of the requested resource")], trace_spec : Annotated[TraceSpec, Field(..., description="A traceSpec object")], **kwargs) -> TraceDetailEnvelope:  # noqa: E501
        """Enable/disable data flow tracing for an identity  # noqa: E501

        Allows an admin to enable/disable data flow tracing for an identity   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_identity_tracing(id, trace_spec, async_req=True)
        >>> result = thread.get()

        :param id: The id of the requested resource (required)
        :type id: str
        :param trace_spec: A traceSpec object (required)
        :type trace_spec: TraceSpec
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: TraceDetailEnvelope
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the update_identity_tracing_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.update_identity_tracing_with_http_info(id, trace_spec, **kwargs)  # noqa: E501

    @validate_arguments
    def update_identity_tracing_with_http_info(self, id : Annotated[StrictStr, Field(..., description="The id of the requested resource")], trace_spec : Annotated[TraceSpec, Field(..., description="A traceSpec object")], **kwargs) -> ApiResponse:  # noqa: E501
        """Enable/disable data flow tracing for an identity  # noqa: E501

        Allows an admin to enable/disable data flow tracing for an identity   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_identity_tracing_with_http_info(id, trace_spec, async_req=True)
        >>> result = thread.get()

        :param id: The id of the requested resource (required)
        :type id: str
        :param trace_spec: A traceSpec object (required)
        :type trace_spec: TraceSpec
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(TraceDetailEnvelope, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'id',
            'trace_spec'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_identity_tracing" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['id']:
            _path_params['id'] = _params['id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['trace_spec'] is not None:
            _body_params = _params['trace_spec']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['ztSession']  # noqa: E501

        _response_types_map = {
            '200': "TraceDetailEnvelope",
            '400': "ApiErrorEnvelope",
            '401': "ApiErrorEnvelope",
            '404': "ApiErrorEnvelope",
        }

        return self.api_client.call_api(
            '/identities/{id}/trace', 'PUT',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
