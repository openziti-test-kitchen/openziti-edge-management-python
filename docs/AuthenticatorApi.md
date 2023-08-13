# openziti_edge_management.AuthenticatorApi

All URIs are relative to *https://demo.ziti.dev/edge/management/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_authenticator**](AuthenticatorApi.md#create_authenticator) | **POST** /authenticators | Creates an authenticator
[**delete_authenticator**](AuthenticatorApi.md#delete_authenticator) | **DELETE** /authenticators/{id} | Delete an Authenticator
[**detail_authenticator**](AuthenticatorApi.md#detail_authenticator) | **GET** /authenticators/{id} | Retrieves a single authenticator
[**list_authenticators**](AuthenticatorApi.md#list_authenticators) | **GET** /authenticators | List authenticators
[**patch_authenticator**](AuthenticatorApi.md#patch_authenticator) | **PATCH** /authenticators/{id} | Update the supplied fields on an authenticator
[**re_enroll_authenticator**](AuthenticatorApi.md#re_enroll_authenticator) | **POST** /authenticators/{id}/re-enroll | Reverts an authenticator to an enrollment
[**update_authenticator**](AuthenticatorApi.md#update_authenticator) | **PUT** /authenticators/{id} | Update all fields on an authenticator


# **create_authenticator**
> AuthenticatorCreate create_authenticator(authenticator)

Creates an authenticator

Creates an authenticator for a specific identity. Requires admin access. 

### Example

* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_management
from openziti_edge_management.api import authenticator_api
from openziti_edge_management.model.authenticator_create import AuthenticatorCreate
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
    api_instance = authenticator_api.AuthenticatorApi(api_client)
    authenticator = AuthenticatorCreate(
        cert_pem="cert_pem_example",
        identity_id="identity_id_example",
        method="method_example",
        password="password_example",
        tags=Tags(None),
        username="username_example",
    ) # AuthenticatorCreate | A Authenticator create object

    # example passing only required values which don't have defaults set
    try:
        # Creates an authenticator
        api_response = api_instance.create_authenticator(authenticator)
        pprint(api_response)
    except openziti_edge_management.ApiException as e:
        print("Exception when calling AuthenticatorApi->create_authenticator: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authenticator** | [**AuthenticatorCreate**](AuthenticatorCreate.md)| A Authenticator create object |

### Return type

[**AuthenticatorCreate**](AuthenticatorCreate.md)

### Authorization

[ztSession](../README.md#ztSession)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The create was successful |  -  |
**400** | The supplied request contains invalid fields or could not be parsed (json and non-json bodies). The error&#39;s code, message, and cause fields can be inspected for further information |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_authenticator**
> Empty delete_authenticator(id)

Delete an Authenticator

Delete an authenticator by id. Deleting all authenticators for an identity will make it impossible to log in. Requires admin access. 

### Example

* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_management
from openziti_edge_management.api import authenticator_api
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
    api_instance = authenticator_api.AuthenticatorApi(api_client)
    id = "id_example" # str | The id of the requested resource

    # example passing only required values which don't have defaults set
    try:
        # Delete an Authenticator
        api_response = api_instance.delete_authenticator(id)
        pprint(api_response)
    except openziti_edge_management.ApiException as e:
        print("Exception when calling AuthenticatorApi->delete_authenticator: %s\n" % e)
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

# **detail_authenticator**
> DetailAuthenticatorEnvelope detail_authenticator(id)

Retrieves a single authenticator

Retrieves a single authenticator by id. Requires admin access.

### Example

* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_management
from openziti_edge_management.api import authenticator_api
from openziti_edge_management.model.api_error_envelope import ApiErrorEnvelope
from openziti_edge_management.model.detail_authenticator_envelope import DetailAuthenticatorEnvelope
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
    api_instance = authenticator_api.AuthenticatorApi(api_client)
    id = "id_example" # str | The id of the requested resource

    # example passing only required values which don't have defaults set
    try:
        # Retrieves a single authenticator
        api_response = api_instance.detail_authenticator(id)
        pprint(api_response)
    except openziti_edge_management.ApiException as e:
        print("Exception when calling AuthenticatorApi->detail_authenticator: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource |

### Return type

[**DetailAuthenticatorEnvelope**](DetailAuthenticatorEnvelope.md)

### Authorization

[ztSession](../README.md#ztSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A singular authenticator resource |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |
**404** | The requested resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_authenticators**
> ListAuthenticatorsEnvelope list_authenticators()

List authenticators

Returns a list of authenticators associated to identities. The resources can be sorted, filtered, and paginated. This endpoint requires admin access. 

### Example

* Api Key Authentication (ztSession):
* OAuth Authentication (oauth2):

```python
import time
import openziti_edge_management
from openziti_edge_management.api import authenticator_api
from openziti_edge_management.model.list_authenticators_envelope import ListAuthenticatorsEnvelope
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

# Configure OAuth2 access token for authorization: oauth2
configuration = openziti_edge_management.Configuration(
    host = "https://demo.ziti.dev/edge/management/v1"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with openziti_edge_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authenticator_api.AuthenticatorApi(api_client)
    limit = 1 # int |  (optional)
    offset = 1 # int |  (optional)
    filter = "filter_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List authenticators
        api_response = api_instance.list_authenticators(limit=limit, offset=offset, filter=filter)
        pprint(api_response)
    except openziti_edge_management.ApiException as e:
        print("Exception when calling AuthenticatorApi->list_authenticators: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional]
 **offset** | **int**|  | [optional]
 **filter** | **str**|  | [optional]

### Return type

[**ListAuthenticatorsEnvelope**](ListAuthenticatorsEnvelope.md)

### Authorization

[ztSession](../README.md#ztSession), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of authenticators |  -  |
**400** | The supplied request contains invalid fields or could not be parsed (json and non-json bodies). The error&#39;s code, message, and cause fields can be inspected for further information |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_authenticator**
> Empty patch_authenticator(id, authenticator)

Update the supplied fields on an authenticator

Update the supplied fields on an authenticator by id. Requires admin access.

### Example

* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_management
from openziti_edge_management.api import authenticator_api
from openziti_edge_management.model.authenticator_patch import AuthenticatorPatch
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
    api_instance = authenticator_api.AuthenticatorApi(api_client)
    id = "id_example" # str | The id of the requested resource
    authenticator = AuthenticatorPatch(
        password=PasswordNullable("password_example"),
        tags=Tags(None),
        username=UsernameNullable("username_example"),
    ) # AuthenticatorPatch | An authenticator patch object

    # example passing only required values which don't have defaults set
    try:
        # Update the supplied fields on an authenticator
        api_response = api_instance.patch_authenticator(id, authenticator)
        pprint(api_response)
    except openziti_edge_management.ApiException as e:
        print("Exception when calling AuthenticatorApi->patch_authenticator: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource |
 **authenticator** | [**AuthenticatorPatch**](AuthenticatorPatch.md)| An authenticator patch object |

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

# **re_enroll_authenticator**
> CreateEnvelope re_enroll_authenticator(id, re_enroll)

Reverts an authenticator to an enrollment

Allows an authenticator to be reverted to an enrollment and allows re-enrollment to occur. On success the  created enrollment record response is provided and the source authenticator record will be deleted. The  enrollment created depends on the authenticator. UPDB authenticators result in UPDB enrollments, CERT authenticators result in OTT enrollments, CERT + CA authenticators result in OTTCA enrollments. 

### Example

* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_management
from openziti_edge_management.api import authenticator_api
from openziti_edge_management.model.create_envelope import CreateEnvelope
from openziti_edge_management.model.re_enroll import ReEnroll
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
    api_instance = authenticator_api.AuthenticatorApi(api_client)
    id = "id_example" # str | The id of the requested resource
    re_enroll = ReEnroll(
        expires_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # ReEnroll | A reEnrollment request

    # example passing only required values which don't have defaults set
    try:
        # Reverts an authenticator to an enrollment
        api_response = api_instance.re_enroll_authenticator(id, re_enroll)
        pprint(api_response)
    except openziti_edge_management.ApiException as e:
        print("Exception when calling AuthenticatorApi->re_enroll_authenticator: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource |
 **re_enroll** | [**ReEnroll**](ReEnroll.md)| A reEnrollment request |

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
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |
**404** | The requested resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_authenticator**
> Empty update_authenticator(id, authenticator)

Update all fields on an authenticator

Update all fields on an authenticator by id. Requires admin access.

### Example

* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_management
from openziti_edge_management.api import authenticator_api
from openziti_edge_management.model.authenticator_update import AuthenticatorUpdate
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
    api_instance = authenticator_api.AuthenticatorApi(api_client)
    id = "id_example" # str | The id of the requested resource
    authenticator = AuthenticatorUpdate(
        password=Password("password_example"),
        tags=Tags(None),
        username=Username("username_example"),
    ) # AuthenticatorUpdate | An authenticator put object

    # example passing only required values which don't have defaults set
    try:
        # Update all fields on an authenticator
        api_response = api_instance.update_authenticator(id, authenticator)
        pprint(api_response)
    except openziti_edge_management.ApiException as e:
        print("Exception when calling AuthenticatorApi->update_authenticator: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource |
 **authenticator** | [**AuthenticatorUpdate**](AuthenticatorUpdate.md)| An authenticator put object |

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

