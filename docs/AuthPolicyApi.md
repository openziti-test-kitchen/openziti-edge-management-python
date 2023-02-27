# openziti_edge_management.AuthPolicyApi

All URIs are relative to *https://demo.ziti.dev/edge/management/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_auth_policy**](AuthPolicyApi.md#create_auth_policy) | **POST** /auth-policies | Creates an Auth Policy
[**delete_auth_policy**](AuthPolicyApi.md#delete_auth_policy) | **DELETE** /auth-policies/{id} | Delete an Auth Policy
[**detail_auth_policy**](AuthPolicyApi.md#detail_auth_policy) | **GET** /auth-policies/{id} | Retrieves a single Auth Policy
[**list_auth_policies**](AuthPolicyApi.md#list_auth_policies) | **GET** /auth-policies | List Auth Policies
[**patch_auth_policy**](AuthPolicyApi.md#patch_auth_policy) | **PATCH** /auth-policies/{id} | Update the supplied fields on an Auth Policy
[**update_auth_policy**](AuthPolicyApi.md#update_auth_policy) | **PUT** /auth-policies/{id} | Update all fields on an Auth Policy


# **create_auth_policy**
> CreateEnvelope create_auth_policy(auth_policy)

Creates an Auth Policy

Creates an Auth Policy. Requires admin access.

### Example

* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_management
from openziti_edge_management.api import auth_policy_api
from openziti_edge_management.model.create_envelope import CreateEnvelope
from openziti_edge_management.model.api_error_envelope import ApiErrorEnvelope
from openziti_edge_management.model.auth_policy_create import AuthPolicyCreate
from pprint import pprint
# Defining the host is optional and defaults to https://demo.ziti.dev/edge/management/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openziti_edge_management.Configuration(
    host = "https://demo.ziti.dev/edge/management/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ztSession
configuration.api_key['ztSession'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ztSession'] = 'Bearer'

# Enter a context with an instance of the API client
with openziti_edge_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_policy_api.AuthPolicyApi(api_client)
    auth_policy = AuthPolicyCreate(
        name="name_example",
        primary=AuthPolicyPrimary(
            cert=AuthPolicyPrimaryCert(
                allow_expired_certs=True,
                allowed=True,
            ),
            ext_jwt=AuthPolicyPrimaryExtJwt(
                allowed=True,
                allowed_signers=[
                    "allowed_signers_example",
                ],
            ),
            updb=AuthPolicyPrimaryUpdb(
                allowed=True,
                lockout_duration_minutes=1,
                max_attempts=1,
                min_password_length=1,
                require_mixed_case=True,
                require_number_char=True,
                require_special_char=True,
            ),
        ),
        secondary=AuthPolicySecondary(
            require_ext_jwt_signer="require_ext_jwt_signer_example",
            require_totp=True,
        ),
        tags=Tags(None),
    ) # AuthPolicyCreate | An Auth Policy to create

    # example passing only required values which don't have defaults set
    try:
        # Creates an Auth Policy
        api_response = api_instance.create_auth_policy(auth_policy)
        pprint(api_response)
    except openziti_edge_management.ApiException as e:
        print("Exception when calling AuthPolicyApi->create_auth_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_policy** | [**AuthPolicyCreate**](AuthPolicyCreate.md)| An Auth Policy to create |

### Return type

[**CreateEnvelope**](CreateEnvelope.md)

### Authorization

[ztSession](../README.md#ztSession)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The create request was successful and the resource has been added at the following location |  -  |
**400** | The supplied request contains invalid fields or could not be parsed (json and non-json bodies). The error&#39;s code, message, and cause fields can be inspected for further information |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_auth_policy**
> Empty delete_auth_policy(id)

Delete an Auth Policy

Delete an Auth Policy by id. Requires admin access. 

### Example

* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_management
from openziti_edge_management.api import auth_policy_api
from openziti_edge_management.model.api_error_envelope import ApiErrorEnvelope
from openziti_edge_management.model.empty import Empty
from pprint import pprint
# Defining the host is optional and defaults to https://demo.ziti.dev/edge/management/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openziti_edge_management.Configuration(
    host = "https://demo.ziti.dev/edge/management/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ztSession
configuration.api_key['ztSession'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ztSession'] = 'Bearer'

# Enter a context with an instance of the API client
with openziti_edge_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_policy_api.AuthPolicyApi(api_client)
    id = "id_example" # str | The id of the requested resource

    # example passing only required values which don't have defaults set
    try:
        # Delete an Auth Policy
        api_response = api_instance.delete_auth_policy(id)
        pprint(api_response)
    except openziti_edge_management.ApiException as e:
        print("Exception when calling AuthPolicyApi->delete_auth_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource |

### Return type

[**Empty**](Empty.md)

### Authorization

[ztSession](../README.md#ztSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The delete request was successful and the resource has been removed |  -  |
**400** | The supplied request contains invalid fields or could not be parsed (json and non-json bodies). The error&#39;s code, message, and cause fields can be inspected for further information |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detail_auth_policy**
> DetailAuthPolicyEnvelope detail_auth_policy(id)

Retrieves a single Auth Policy

Retrieves a single Auth Policy by id. Requires admin access.

### Example

* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_management
from openziti_edge_management.api import auth_policy_api
from openziti_edge_management.model.detail_auth_policy_envelope import DetailAuthPolicyEnvelope
from openziti_edge_management.model.api_error_envelope import ApiErrorEnvelope
from pprint import pprint
# Defining the host is optional and defaults to https://demo.ziti.dev/edge/management/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openziti_edge_management.Configuration(
    host = "https://demo.ziti.dev/edge/management/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ztSession
configuration.api_key['ztSession'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ztSession'] = 'Bearer'

# Enter a context with an instance of the API client
with openziti_edge_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_policy_api.AuthPolicyApi(api_client)
    id = "id_example" # str | The id of the requested resource

    # example passing only required values which don't have defaults set
    try:
        # Retrieves a single Auth Policy
        api_response = api_instance.detail_auth_policy(id)
        pprint(api_response)
    except openziti_edge_management.ApiException as e:
        print("Exception when calling AuthPolicyApi->detail_auth_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource |

### Return type

[**DetailAuthPolicyEnvelope**](DetailAuthPolicyEnvelope.md)

### Authorization

[ztSession](../README.md#ztSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A singular Auth Policy resource |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |
**404** | The requested resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_auth_policies**
> ListAuthPoliciesEnvelope list_auth_policies()

List Auth Policies

Retrieves a list of Auth Policies

### Example

* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_management
from openziti_edge_management.api import auth_policy_api
from openziti_edge_management.model.list_auth_policies_envelope import ListAuthPoliciesEnvelope
from openziti_edge_management.model.api_error_envelope import ApiErrorEnvelope
from pprint import pprint
# Defining the host is optional and defaults to https://demo.ziti.dev/edge/management/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openziti_edge_management.Configuration(
    host = "https://demo.ziti.dev/edge/management/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ztSession
configuration.api_key['ztSession'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ztSession'] = 'Bearer'

# Enter a context with an instance of the API client
with openziti_edge_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_policy_api.AuthPolicyApi(api_client)
    limit = 1 # int |  (optional)
    offset = 1 # int |  (optional)
    filter = "filter_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Auth Policies
        api_response = api_instance.list_auth_policies(limit=limit, offset=offset, filter=filter)
        pprint(api_response)
    except openziti_edge_management.ApiException as e:
        print("Exception when calling AuthPolicyApi->list_auth_policies: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional]
 **offset** | **int**|  | [optional]
 **filter** | **str**|  | [optional]

### Return type

[**ListAuthPoliciesEnvelope**](ListAuthPoliciesEnvelope.md)

### Authorization

[ztSession](../README.md#ztSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of Auth Policies |  -  |
**400** | The supplied request contains invalid fields or could not be parsed (json and non-json bodies). The error&#39;s code, message, and cause fields can be inspected for further information |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_auth_policy**
> Empty patch_auth_policy(id, auth_policy)

Update the supplied fields on an Auth Policy

Update only the supplied fields on an Auth Policy by id. Requires admin access.

### Example

* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_management
from openziti_edge_management.api import auth_policy_api
from openziti_edge_management.model.auth_policy_patch import AuthPolicyPatch
from openziti_edge_management.model.api_error_envelope import ApiErrorEnvelope
from openziti_edge_management.model.empty import Empty
from pprint import pprint
# Defining the host is optional and defaults to https://demo.ziti.dev/edge/management/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openziti_edge_management.Configuration(
    host = "https://demo.ziti.dev/edge/management/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ztSession
configuration.api_key['ztSession'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ztSession'] = 'Bearer'

# Enter a context with an instance of the API client
with openziti_edge_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_policy_api.AuthPolicyApi(api_client)
    id = "id_example" # str | The id of the requested resource
    auth_policy = AuthPolicyPatch(
        name="name_example",
        primary=AuthPolicyPrimaryPatch(
            cert=AuthPolicyPrimaryCertPatch(
                allow_expired_certs=True,
                allowed=True,
            ),
            ext_jwt=AuthPolicyPrimaryExtJwtPatch(
                allowed=True,
                allowed_signers=[
                    "allowed_signers_example",
                ],
            ),
            updb=AuthPolicyPrimaryUpdbPatch(
                allowed=True,
                lockout_duration_minutes=1,
                max_attempts=1,
                min_password_length=1,
                require_mixed_case=True,
                require_number_char=True,
                require_special_char=True,
            ),
        ),
        secondary=AuthPolicySecondaryPatch(
            require_ext_jwt_signer="require_ext_jwt_signer_example",
            require_totp=True,
        ),
        tags=Tags(None),
    ) # AuthPolicyPatch | An Auth Policy patch object

    # example passing only required values which don't have defaults set
    try:
        # Update the supplied fields on an Auth Policy
        api_response = api_instance.patch_auth_policy(id, auth_policy)
        pprint(api_response)
    except openziti_edge_management.ApiException as e:
        print("Exception when calling AuthPolicyApi->patch_auth_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource |
 **auth_policy** | [**AuthPolicyPatch**](AuthPolicyPatch.md)| An Auth Policy patch object |

### Return type

[**Empty**](Empty.md)

### Authorization

[ztSession](../README.md#ztSession)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The patch request was successful and the resource has been altered |  -  |
**400** | The supplied request contains invalid fields or could not be parsed (json and non-json bodies). The error&#39;s code, message, and cause fields can be inspected for further information |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |
**404** | The requested resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_auth_policy**
> Empty update_auth_policy(id, auth_policy)

Update all fields on an Auth Policy

Update all fields on an Auth Policy by id. Requires admin access.

### Example

* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_management
from openziti_edge_management.api import auth_policy_api
from openziti_edge_management.model.api_error_envelope import ApiErrorEnvelope
from openziti_edge_management.model.auth_policy_create import AuthPolicyCreate
from openziti_edge_management.model.empty import Empty
from pprint import pprint
# Defining the host is optional and defaults to https://demo.ziti.dev/edge/management/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openziti_edge_management.Configuration(
    host = "https://demo.ziti.dev/edge/management/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ztSession
configuration.api_key['ztSession'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ztSession'] = 'Bearer'

# Enter a context with an instance of the API client
with openziti_edge_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_policy_api.AuthPolicyApi(api_client)
    id = "id_example" # str | The id of the requested resource
    auth_policy = AuthPolicyCreate(
        name="name_example",
        primary=AuthPolicyPrimary(
            cert=AuthPolicyPrimaryCert(
                allow_expired_certs=True,
                allowed=True,
            ),
            ext_jwt=AuthPolicyPrimaryExtJwt(
                allowed=True,
                allowed_signers=[
                    "allowed_signers_example",
                ],
            ),
            updb=AuthPolicyPrimaryUpdb(
                allowed=True,
                lockout_duration_minutes=1,
                max_attempts=1,
                min_password_length=1,
                require_mixed_case=True,
                require_number_char=True,
                require_special_char=True,
            ),
        ),
        secondary=AuthPolicySecondary(
            require_ext_jwt_signer="require_ext_jwt_signer_example",
            require_totp=True,
        ),
        tags=Tags(None),
    ) # AuthPolicyCreate | An Auth Policy update object

    # example passing only required values which don't have defaults set
    try:
        # Update all fields on an Auth Policy
        api_response = api_instance.update_auth_policy(id, auth_policy)
        pprint(api_response)
    except openziti_edge_management.ApiException as e:
        print("Exception when calling AuthPolicyApi->update_auth_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource |
 **auth_policy** | [**AuthPolicyCreate**](AuthPolicyCreate.md)| An Auth Policy update object |

### Return type

[**Empty**](Empty.md)

### Authorization

[ztSession](../README.md#ztSession)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The update request was successful and the resource has been altered |  -  |
**400** | The supplied request contains invalid fields or could not be parsed (json and non-json bodies). The error&#39;s code, message, and cause fields can be inspected for further information |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |
**404** | The requested resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

