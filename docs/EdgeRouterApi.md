# openziti_edge_management.EdgeRouterApi

All URIs are relative to *https://demo.ziti.dev/edge/management/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_edge_router**](EdgeRouterApi.md#create_edge_router) | **POST** /edge-routers | Create an edge router
[**delete_edge_router**](EdgeRouterApi.md#delete_edge_router) | **DELETE** /edge-routers/{id} | Delete an edge router
[**detail_edge_router**](EdgeRouterApi.md#detail_edge_router) | **GET** /edge-routers/{id} | Retrieves a single edge router
[**list_edge_router_edge_router_policies**](EdgeRouterApi.md#list_edge_router_edge_router_policies) | **GET** /edge-routers/{id}/edge-router-policies | List the edge router policies that affect an edge router
[**list_edge_router_identities**](EdgeRouterApi.md#list_edge_router_identities) | **GET** /edge-routers/{id}/identities | List associated identities
[**list_edge_router_service_edge_router_policies**](EdgeRouterApi.md#list_edge_router_service_edge_router_policies) | **GET** /edge-routers/{id}/service-edge-router-policies | List the service policies that affect an edge router
[**list_edge_router_services**](EdgeRouterApi.md#list_edge_router_services) | **GET** /edge-routers/{id}/services | List associated services
[**list_edge_routers**](EdgeRouterApi.md#list_edge_routers) | **GET** /edge-routers | List edge routers
[**patch_edge_router**](EdgeRouterApi.md#patch_edge_router) | **PATCH** /edge-routers/{id} | Update the supplied fields on an edge router
[**re_enroll_edge_router**](EdgeRouterApi.md#re_enroll_edge_router) | **POST** /edge-routers/{id}/re-enroll | Re-enroll an edge router
[**update_edge_router**](EdgeRouterApi.md#update_edge_router) | **PUT** /edge-routers/{id} | Update all fields on an edge router


# **create_edge_router**
> CreateEnvelope create_edge_router(edge_router)

Create an edge router

Create a edge router resource. Requires admin access.

### Example

* Api Key Authentication (ztSession):
```python
import time
import os
import openziti_edge_management
from openziti_edge_management.models.create_envelope import CreateEnvelope
from openziti_edge_management.models.edge_router_create import EdgeRouterCreate
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
    api_instance = openziti_edge_management.EdgeRouterApi(api_client)
    edge_router = openziti_edge_management.EdgeRouterCreate() # EdgeRouterCreate | A edge router to create

    try:
        # Create an edge router
        api_response = api_instance.create_edge_router(edge_router)
        print("The response of EdgeRouterApi->create_edge_router:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeRouterApi->create_edge_router: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_router** | [**EdgeRouterCreate**](EdgeRouterCreate.md)| A edge router to create | 

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

# **delete_edge_router**
> Empty delete_edge_router(id)

Delete an edge router

Delete an edge router by id. Requires admin access.

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
    api_instance = openziti_edge_management.EdgeRouterApi(api_client)
    id = 'id_example' # str | The id of the requested resource

    try:
        # Delete an edge router
        api_response = api_instance.delete_edge_router(id)
        print("The response of EdgeRouterApi->delete_edge_router:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeRouterApi->delete_edge_router: %s\n" % e)
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
**409** | The resource requested to be removed/altered cannot be as it is referenced by another object. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detail_edge_router**
> DetailedEdgeRouterEnvelope detail_edge_router(id)

Retrieves a single edge router

Retrieves a single edge router by id. Requires admin access.

### Example

* Api Key Authentication (ztSession):
```python
import time
import os
import openziti_edge_management
from openziti_edge_management.models.detailed_edge_router_envelope import DetailedEdgeRouterEnvelope
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
    api_instance = openziti_edge_management.EdgeRouterApi(api_client)
    id = 'id_example' # str | The id of the requested resource

    try:
        # Retrieves a single edge router
        api_response = api_instance.detail_edge_router(id)
        print("The response of EdgeRouterApi->detail_edge_router:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeRouterApi->detail_edge_router: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource | 

### Return type

[**DetailedEdgeRouterEnvelope**](DetailedEdgeRouterEnvelope.md)

### Authorization

[ztSession](../README.md#ztSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A singular edge router resource |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |
**404** | The requested resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_edge_router_edge_router_policies**
> ListEdgeRouterPoliciesEnvelope list_edge_router_edge_router_policies(id)

List the edge router policies that affect an edge router

Retrieves a list of edge router policies that apply to the specified edge router.

### Example

* Api Key Authentication (ztSession):
```python
import time
import os
import openziti_edge_management
from openziti_edge_management.models.list_edge_router_policies_envelope import ListEdgeRouterPoliciesEnvelope
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
    api_instance = openziti_edge_management.EdgeRouterApi(api_client)
    id = 'id_example' # str | The id of the requested resource

    try:
        # List the edge router policies that affect an edge router
        api_response = api_instance.list_edge_router_edge_router_policies(id)
        print("The response of EdgeRouterApi->list_edge_router_edge_router_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeRouterApi->list_edge_router_edge_router_policies: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource | 

### Return type

[**ListEdgeRouterPoliciesEnvelope**](ListEdgeRouterPoliciesEnvelope.md)

### Authorization

[ztSession](../README.md#ztSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of edge router policies |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |
**404** | The requested resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_edge_router_identities**
> ListIdentitiesEnvelope list_edge_router_identities(id)

List associated identities

Retrieves a list of identities that may access services via the given edge router. Supports filtering, sorting, and pagination. Requires admin access. 

### Example

* Api Key Authentication (ztSession):
```python
import time
import os
import openziti_edge_management
from openziti_edge_management.models.list_identities_envelope import ListIdentitiesEnvelope
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
    api_instance = openziti_edge_management.EdgeRouterApi(api_client)
    id = 'id_example' # str | The id of the requested resource

    try:
        # List associated identities
        api_response = api_instance.list_edge_router_identities(id)
        print("The response of EdgeRouterApi->list_edge_router_identities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeRouterApi->list_edge_router_identities: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource | 

### Return type

[**ListIdentitiesEnvelope**](ListIdentitiesEnvelope.md)

### Authorization

[ztSession](../README.md#ztSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of identities |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |
**404** | The requested resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_edge_router_service_edge_router_policies**
> ListServicePoliciesEnvelope list_edge_router_service_edge_router_policies(id)

List the service policies that affect an edge router

Retrieves a list of service policies policies that apply to the specified edge router.

### Example

* Api Key Authentication (ztSession):
```python
import time
import os
import openziti_edge_management
from openziti_edge_management.models.list_service_policies_envelope import ListServicePoliciesEnvelope
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
    api_instance = openziti_edge_management.EdgeRouterApi(api_client)
    id = 'id_example' # str | The id of the requested resource

    try:
        # List the service policies that affect an edge router
        api_response = api_instance.list_edge_router_service_edge_router_policies(id)
        print("The response of EdgeRouterApi->list_edge_router_service_edge_router_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeRouterApi->list_edge_router_service_edge_router_policies: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource | 

### Return type

[**ListServicePoliciesEnvelope**](ListServicePoliciesEnvelope.md)

### Authorization

[ztSession](../README.md#ztSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of service policies |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |
**404** | The requested resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_edge_router_services**
> ListServicesEnvelope list_edge_router_services(id)

List associated services

Retrieves a list of services that may be accessed via the given edge router. Supports filtering, sorting, and pagination. Requires admin access. 

### Example

* Api Key Authentication (ztSession):
```python
import time
import os
import openziti_edge_management
from openziti_edge_management.models.list_services_envelope import ListServicesEnvelope
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
    api_instance = openziti_edge_management.EdgeRouterApi(api_client)
    id = 'id_example' # str | The id of the requested resource

    try:
        # List associated services
        api_response = api_instance.list_edge_router_services(id)
        print("The response of EdgeRouterApi->list_edge_router_services:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeRouterApi->list_edge_router_services: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource | 

### Return type

[**ListServicesEnvelope**](ListServicesEnvelope.md)

### Authorization

[ztSession](../README.md#ztSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of services |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |
**404** | The requested resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_edge_routers**
> ListEdgeRoutersEnvelope list_edge_routers(limit=limit, offset=offset, filter=filter, role_filter=role_filter, role_semantic=role_semantic)

List edge routers

Retrieves a list of edge router resources; supports filtering, sorting, and pagination. Requires admin access. 

### Example

* Api Key Authentication (ztSession):
* OAuth Authentication (oauth2):
```python
import time
import os
import openziti_edge_management
from openziti_edge_management.models.list_edge_routers_envelope import ListEdgeRoutersEnvelope
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
    api_instance = openziti_edge_management.EdgeRouterApi(api_client)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    filter = 'filter_example' # str |  (optional)
    role_filter = ['role_filter_example'] # List[str] |  (optional)
    role_semantic = 'role_semantic_example' # str |  (optional)

    try:
        # List edge routers
        api_response = api_instance.list_edge_routers(limit=limit, offset=offset, filter=filter, role_filter=role_filter, role_semantic=role_semantic)
        print("The response of EdgeRouterApi->list_edge_routers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeRouterApi->list_edge_routers: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **filter** | **str**|  | [optional] 
 **role_filter** | [**List[str]**](str.md)|  | [optional] 
 **role_semantic** | **str**|  | [optional] 

### Return type

[**ListEdgeRoutersEnvelope**](ListEdgeRoutersEnvelope.md)

### Authorization

[ztSession](../README.md#ztSession), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of edge routers |  -  |
**400** | The supplied request contains invalid fields or could not be parsed (json and non-json bodies). The error&#39;s code, message, and cause fields can be inspected for further information |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_edge_router**
> Empty patch_edge_router(id, edge_router)

Update the supplied fields on an edge router

Update the supplied fields on an edge router. Requires admin access.

### Example

* Api Key Authentication (ztSession):
```python
import time
import os
import openziti_edge_management
from openziti_edge_management.models.edge_router_patch import EdgeRouterPatch
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
    api_instance = openziti_edge_management.EdgeRouterApi(api_client)
    id = 'id_example' # str | The id of the requested resource
    edge_router = openziti_edge_management.EdgeRouterPatch() # EdgeRouterPatch | An edge router patch object

    try:
        # Update the supplied fields on an edge router
        api_response = api_instance.patch_edge_router(id, edge_router)
        print("The response of EdgeRouterApi->patch_edge_router:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeRouterApi->patch_edge_router: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource | 
 **edge_router** | [**EdgeRouterPatch**](EdgeRouterPatch.md)| An edge router patch object | 

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

# **re_enroll_edge_router**
> Empty re_enroll_edge_router(id)

Re-enroll an edge router

Removes current certificate based authentication mechanisms and reverts the edge router into a state where enrollment must be performed. The router retains all other properties and associations. If the router is currently connected, it will be disconnected and any attemps to reconnect will fail until the enrollment process is completed with the newly generated JWT.  If the edge router has an existing outstanding enrollment JWT it will be replaced. The previous JWT will no longer be usable to complete the enrollment process. 

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
    api_instance = openziti_edge_management.EdgeRouterApi(api_client)
    id = 'id_example' # str | The id of the requested resource

    try:
        # Re-enroll an edge router
        api_response = api_instance.re_enroll_edge_router(id)
        print("The response of EdgeRouterApi->re_enroll_edge_router:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeRouterApi->re_enroll_edge_router: %s\n" % e)
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
**200** | Base empty response |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |
**404** | The requested resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_edge_router**
> Empty update_edge_router(id, edge_router)

Update all fields on an edge router

Update all fields on an edge router by id. Requires admin access.

### Example

* Api Key Authentication (ztSession):
```python
import time
import os
import openziti_edge_management
from openziti_edge_management.models.edge_router_update import EdgeRouterUpdate
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
    api_instance = openziti_edge_management.EdgeRouterApi(api_client)
    id = 'id_example' # str | The id of the requested resource
    edge_router = openziti_edge_management.EdgeRouterUpdate() # EdgeRouterUpdate | An edge router update object

    try:
        # Update all fields on an edge router
        api_response = api_instance.update_edge_router(id, edge_router)
        print("The response of EdgeRouterApi->update_edge_router:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeRouterApi->update_edge_router: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource | 
 **edge_router** | [**EdgeRouterUpdate**](EdgeRouterUpdate.md)| An edge router update object | 

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

