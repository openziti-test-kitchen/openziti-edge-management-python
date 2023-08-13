# openziti_edge_management.EnrollmentApi

All URIs are relative to *https://demo.ziti.dev/edge/management/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_enrollment**](EnrollmentApi.md#create_enrollment) | **POST** /enrollments | Create an outstanding enrollment for an identity
[**delete_enrollment**](EnrollmentApi.md#delete_enrollment) | **DELETE** /enrollments/{id} | Delete an outstanding enrollment
[**detail_enrollment**](EnrollmentApi.md#detail_enrollment) | **GET** /enrollments/{id} | Retrieves an outstanding enrollment
[**list_enrollments**](EnrollmentApi.md#list_enrollments) | **GET** /enrollments | List outstanding enrollments
[**refresh_enrollment**](EnrollmentApi.md#refresh_enrollment) | **POST** /enrollments/{id}/refresh | Refreshes an enrollment record&#39;s expiration window


# **create_enrollment**
> CreateEnvelope create_enrollment(enrollment)

Create an outstanding enrollment for an identity

Creates a new OTT, OTTCA, or UPDB enrollment for a specific identity. If an enrollment of the same type is already outstanding the request will fail with a 409 conflict. If desired, an existing enrollment can be refreshed by `enrollments/:id/refresh` or deleted.

### Example

* Api Key Authentication (ztSession):
* OAuth Authentication (oauth2):

```python
import time
import openziti_edge_management
from openziti_edge_management.api import enrollment_api
from openziti_edge_management.model.create_envelope import CreateEnvelope
from openziti_edge_management.model.api_error_envelope import ApiErrorEnvelope
from openziti_edge_management.model.enrollment_create import EnrollmentCreate
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
    api_instance = enrollment_api.EnrollmentApi(api_client)
    enrollment = EnrollmentCreate(
        ca_id="ca_id_example",
        expires_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        identity_id="identity_id_example",
        method="ott",
        username="username_example",
    ) # EnrollmentCreate | An enrollment to create

    # example passing only required values which don't have defaults set
    try:
        # Create an outstanding enrollment for an identity
        api_response = api_instance.create_enrollment(enrollment)
        pprint(api_response)
    except openziti_edge_management.ApiException as e:
        print("Exception when calling EnrollmentApi->create_enrollment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enrollment** | [**EnrollmentCreate**](EnrollmentCreate.md)| An enrollment to create |

### Return type

[**CreateEnvelope**](CreateEnvelope.md)

### Authorization

[ztSession](../README.md#ztSession), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The create request was successful and the resource has been added at the following location |  -  |
**400** | The supplied request contains invalid fields or could not be parsed (json and non-json bodies). The error&#39;s code, message, and cause fields can be inspected for further information |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |
**409** | The request could not be completed due to a conflict of configuration or state |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_enrollment**
> Empty delete_enrollment(id)

Delete an outstanding enrollment

Delete an outstanding enrollment by id. Requires admin access.

### Example

* Api Key Authentication (ztSession):
* OAuth Authentication (oauth2):

```python
import time
import openziti_edge_management
from openziti_edge_management.api import enrollment_api
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

# Configure OAuth2 access token for authorization: oauth2
configuration = openziti_edge_management.Configuration(
    host = "https://demo.ziti.dev/edge/management/v1"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with openziti_edge_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = enrollment_api.EnrollmentApi(api_client)
    id = "id_example" # str | The id of the requested resource

    # example passing only required values which don't have defaults set
    try:
        # Delete an outstanding enrollment
        api_response = api_instance.delete_enrollment(id)
        pprint(api_response)
    except openziti_edge_management.ApiException as e:
        print("Exception when calling EnrollmentApi->delete_enrollment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource |

### Return type

[**Empty**](Empty.md)

### Authorization

[ztSession](../README.md#ztSession), [oauth2](../README.md#oauth2)

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

# **detail_enrollment**
> DetailEnrollmentEnvelope detail_enrollment(id)

Retrieves an outstanding enrollment

Retrieves a single outstanding enrollment by id. Requires admin access.

### Example

* Api Key Authentication (ztSession):
* OAuth Authentication (oauth2):

```python
import time
import openziti_edge_management
from openziti_edge_management.api import enrollment_api
from openziti_edge_management.model.detail_enrollment_envelope import DetailEnrollmentEnvelope
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
    api_instance = enrollment_api.EnrollmentApi(api_client)
    id = "id_example" # str | The id of the requested resource

    # example passing only required values which don't have defaults set
    try:
        # Retrieves an outstanding enrollment
        api_response = api_instance.detail_enrollment(id)
        pprint(api_response)
    except openziti_edge_management.ApiException as e:
        print("Exception when calling EnrollmentApi->detail_enrollment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource |

### Return type

[**DetailEnrollmentEnvelope**](DetailEnrollmentEnvelope.md)

### Authorization

[ztSession](../README.md#ztSession), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A singular enrollment resource |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |
**404** | The requested resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_enrollments**
> ListEnrollmentsEnvelope list_enrollments()

List outstanding enrollments

Retrieves a list of outstanding enrollments; supports filtering, sorting, and pagination. Requires admin access. 

### Example

* Api Key Authentication (ztSession):
* OAuth Authentication (oauth2):

```python
import time
import openziti_edge_management
from openziti_edge_management.api import enrollment_api
from openziti_edge_management.model.api_error_envelope import ApiErrorEnvelope
from openziti_edge_management.model.list_enrollments_envelope import ListEnrollmentsEnvelope
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
    api_instance = enrollment_api.EnrollmentApi(api_client)
    limit = 1 # int |  (optional)
    offset = 1 # int |  (optional)
    filter = "filter_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List outstanding enrollments
        api_response = api_instance.list_enrollments(limit=limit, offset=offset, filter=filter)
        pprint(api_response)
    except openziti_edge_management.ApiException as e:
        print("Exception when calling EnrollmentApi->list_enrollments: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional]
 **offset** | **int**|  | [optional]
 **filter** | **str**|  | [optional]

### Return type

[**ListEnrollmentsEnvelope**](ListEnrollmentsEnvelope.md)

### Authorization

[ztSession](../README.md#ztSession), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of enrollments |  -  |
**400** | The supplied request contains invalid fields or could not be parsed (json and non-json bodies). The error&#39;s code, message, and cause fields can be inspected for further information |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_enrollment**
> CreateEnvelope refresh_enrollment(id, refresh)

Refreshes an enrollment record's expiration window

For expired or unexpired enrollments, reset the expiration window. A new JWT will be generated and must be used for the enrollment.

### Example

* Api Key Authentication (ztSession):
* OAuth Authentication (oauth2):

```python
import time
import openziti_edge_management
from openziti_edge_management.api import enrollment_api
from openziti_edge_management.model.create_envelope import CreateEnvelope
from openziti_edge_management.model.enrollment_refresh import EnrollmentRefresh
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
    api_instance = enrollment_api.EnrollmentApi(api_client)
    id = "id_example" # str | The id of the requested resource
    refresh = EnrollmentRefresh(
        expires_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # EnrollmentRefresh | An enrollment refresh request

    # example passing only required values which don't have defaults set
    try:
        # Refreshes an enrollment record's expiration window
        api_response = api_instance.refresh_enrollment(id, refresh)
        pprint(api_response)
    except openziti_edge_management.ApiException as e:
        print("Exception when calling EnrollmentApi->refresh_enrollment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource |
 **refresh** | [**EnrollmentRefresh**](EnrollmentRefresh.md)| An enrollment refresh request |

### Return type

[**CreateEnvelope**](CreateEnvelope.md)

### Authorization

[ztSession](../README.md#ztSession), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The create request was successful and the resource has been added at the following location |  -  |
**400** | The supplied request contains invalid fields or could not be parsed (json and non-json bodies). The error&#39;s code, message, and cause fields can be inspected for further information |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

