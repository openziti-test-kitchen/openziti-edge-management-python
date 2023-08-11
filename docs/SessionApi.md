# openziti_edge_management.SessionApi

All URIs are relative to *https://demo.ziti.dev/edge/management/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_session**](SessionApi.md#delete_session) | **DELETE** /sessions/{id} | Delete a session
[**detail_session**](SessionApi.md#detail_session) | **GET** /sessions/{id} | Retrieves a single session
[**detail_session_route_path**](SessionApi.md#detail_session_route_path) | **GET** /sessions/{id}/route-path | Retrieves a single session&#39;s router path
[**list_sessions**](SessionApi.md#list_sessions) | **GET** /sessions | List sessions


# **delete_session**
> Empty delete_session(id)

Delete a session

Delete a session by id. Requires admin access.

### Example

* Api Key Authentication (ztSession):
* OAuth Authentication (oauth2):
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openziti_edge_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openziti_edge_management.SessionApi(api_client)
    id = 'id_example' # str | The id of the requested resource

    try:
        # Delete a session
        api_response = api_instance.delete_session(id)
        print("The response of SessionApi->delete_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionApi->delete_session: %s\n" % e)
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
**409** | The resource requested to be removed/altered cannot be as it is referenced by another object. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detail_session**
> DetailSessionManagementEnvelope detail_session(id)

Retrieves a single session

Retrieves a single session by id. Requires admin access.

### Example

* Api Key Authentication (ztSession):
* OAuth Authentication (oauth2):
```python
import time
import os
import openziti_edge_management
from openziti_edge_management.models.detail_session_management_envelope import DetailSessionManagementEnvelope
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
    api_instance = openziti_edge_management.SessionApi(api_client)
    id = 'id_example' # str | The id of the requested resource

    try:
        # Retrieves a single session
        api_response = api_instance.detail_session(id)
        print("The response of SessionApi->detail_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionApi->detail_session: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource | 

### Return type

[**DetailSessionManagementEnvelope**](DetailSessionManagementEnvelope.md)

### Authorization

[ztSession](../README.md#ztSession), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A single session |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |
**404** | The requested resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detail_session_route_path**
> DetailSessionRoutePathEnvelope detail_session_route_path(id)

Retrieves a single session's router path

Retrieves a single session's route path by id. Requires admin access.

### Example

* Api Key Authentication (ztSession):
* OAuth Authentication (oauth2):
```python
import time
import os
import openziti_edge_management
from openziti_edge_management.models.detail_session_route_path_envelope import DetailSessionRoutePathEnvelope
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
    api_instance = openziti_edge_management.SessionApi(api_client)
    id = 'id_example' # str | The id of the requested resource

    try:
        # Retrieves a single session's router path
        api_response = api_instance.detail_session_route_path(id)
        print("The response of SessionApi->detail_session_route_path:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionApi->detail_session_route_path: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource | 

### Return type

[**DetailSessionRoutePathEnvelope**](DetailSessionRoutePathEnvelope.md)

### Authorization

[ztSession](../README.md#ztSession), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A single session&#39;s route path |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |
**404** | The requested resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sessions**
> ListSessionsManagementEnvelope list_sessions(limit=limit, offset=offset, filter=filter)

List sessions

Retrieves a list of active sessions resources; supports filtering, sorting, and pagination. Requires admin access.  Sessions are tied to an API session and are moved when an API session times out or logs out. Active sessions (i.e. Ziti SDK connected to an edge router) will keep the session and API session marked as active. 

### Example

* Api Key Authentication (ztSession):
* OAuth Authentication (oauth2):
```python
import time
import os
import openziti_edge_management
from openziti_edge_management.models.list_sessions_management_envelope import ListSessionsManagementEnvelope
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
    api_instance = openziti_edge_management.SessionApi(api_client)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    filter = 'filter_example' # str |  (optional)

    try:
        # List sessions
        api_response = api_instance.list_sessions(limit=limit, offset=offset, filter=filter)
        print("The response of SessionApi->list_sessions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionApi->list_sessions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **filter** | **str**|  | [optional] 

### Return type

[**ListSessionsManagementEnvelope**](ListSessionsManagementEnvelope.md)

### Authorization

[ztSession](../README.md#ztSession), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of sessions |  -  |
**400** | The supplied request contains invalid fields or could not be parsed (json and non-json bodies). The error&#39;s code, message, and cause fields can be inspected for further information |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

