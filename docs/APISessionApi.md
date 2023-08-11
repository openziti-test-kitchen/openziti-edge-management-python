# openziti_edge_management.APISessionApi

All URIs are relative to *https://demo.ziti.dev/edge/management/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_api_sessions**](APISessionApi.md#delete_api_sessions) | **DELETE** /api-sessions/{id} | Deletes an API Sessions
[**detail_api_sessions**](APISessionApi.md#detail_api_sessions) | **GET** /api-sessions/{id} | Retrieves a single API Session
[**list_api_sessions**](APISessionApi.md#list_api_sessions) | **GET** /api-sessions | List active API sessions


# **delete_api_sessions**
> Empty delete_api_sessions(id)

Deletes an API Sessions

Deletes and API sesion by id. Requires admin access.

### Example

* Api Key Authentication (ztSession):
```python
import time
import os
import openziti_edge_management
from openziti_edge_management.models.empty import Empty
from openziti_edge_management.rest import ApiException
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
configuration.api_key['ztSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ztSession'] = 'Bearer'

# Enter a context with an instance of the API client
with openziti_edge_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openziti_edge_management.APISessionApi(api_client)
    id = 'id_example' # str | The id of the requested resource

    try:
        # Deletes an API Sessions
        api_response = api_instance.delete_api_sessions(id)
        print("The response of APISessionApi->delete_api_sessions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APISessionApi->delete_api_sessions: %s\n" % e)
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
**403** | The currently supplied session does not have the correct access rights to request this resource |  -  |
**404** | The requested resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detail_api_sessions**
> DetailApiSessionEnvelope detail_api_sessions(id)

Retrieves a single API Session

Retrieves a single API Session by id. Requires admin access.

### Example

* Api Key Authentication (ztSession):
```python
import time
import os
import openziti_edge_management
from openziti_edge_management.models.detail_api_session_envelope import DetailApiSessionEnvelope
from openziti_edge_management.rest import ApiException
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
configuration.api_key['ztSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ztSession'] = 'Bearer'

# Enter a context with an instance of the API client
with openziti_edge_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openziti_edge_management.APISessionApi(api_client)
    id = 'id_example' # str | The id of the requested resource

    try:
        # Retrieves a single API Session
        api_response = api_instance.detail_api_sessions(id)
        print("The response of APISessionApi->detail_api_sessions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APISessionApi->detail_api_sessions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource | 

### Return type

[**DetailApiSessionEnvelope**](DetailApiSessionEnvelope.md)

### Authorization

[ztSession](../README.md#ztSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieves a singular API Session by id |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |
**404** | The requested resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_api_sessions**
> ListApiSessionsEnvelope list_api_sessions(limit=limit, offset=offset, filter=filter)

List active API sessions

Returns a list of active API sessions. The resources can be sorted, filtered, and paginated. This endpoint requires admin access. 

### Example

* Api Key Authentication (ztSession):
* OAuth Authentication (oauth2):
```python
import time
import os
import openziti_edge_management
from openziti_edge_management.models.list_api_sessions_envelope import ListApiSessionsEnvelope
from openziti_edge_management.rest import ApiException
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
configuration.api_key['ztSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ztSession'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openziti_edge_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openziti_edge_management.APISessionApi(api_client)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    filter = 'filter_example' # str |  (optional)

    try:
        # List active API sessions
        api_response = api_instance.list_api_sessions(limit=limit, offset=offset, filter=filter)
        print("The response of APISessionApi->list_api_sessions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APISessionApi->list_api_sessions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **filter** | **str**|  | [optional] 

### Return type

[**ListApiSessionsEnvelope**](ListApiSessionsEnvelope.md)

### Authorization

[ztSession](../README.md#ztSession), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of active API Sessions |  -  |
**400** | The supplied request contains invalid fields or could not be parsed (json and non-json bodies). The error&#39;s code, message, and cause fields can be inspected for further information |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

