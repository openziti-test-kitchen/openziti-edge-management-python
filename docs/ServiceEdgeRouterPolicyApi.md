# openziti_edge_management.ServiceEdgeRouterPolicyApi

All URIs are relative to *https://demo.ziti.dev/edge/management/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_service_edge_router_policy**](ServiceEdgeRouterPolicyApi.md#create_service_edge_router_policy) | **POST** /service-edge-router-policies | Create a service edge router policy resource
[**delete_service_edge_router_policy**](ServiceEdgeRouterPolicyApi.md#delete_service_edge_router_policy) | **DELETE** /service-edge-router-policies/{id} | Delete a service edge policy
[**detail_service_edge_router_policy**](ServiceEdgeRouterPolicyApi.md#detail_service_edge_router_policy) | **GET** /service-edge-router-policies/{id} | Retrieves a single service edge policy
[**list_service_edge_router_policies**](ServiceEdgeRouterPolicyApi.md#list_service_edge_router_policies) | **GET** /service-edge-router-policies | List service edge router policies
[**list_service_edge_router_policy_edge_routers**](ServiceEdgeRouterPolicyApi.md#list_service_edge_router_policy_edge_routers) | **GET** /service-edge-router-policies/{id}/edge-routers | List the edge routers that a service edge router policy applies to
[**list_service_edge_router_policy_services**](ServiceEdgeRouterPolicyApi.md#list_service_edge_router_policy_services) | **GET** /service-edge-router-policies/{id}/services | List the services that a service edge router policy applies to
[**patch_service_edge_router_policy**](ServiceEdgeRouterPolicyApi.md#patch_service_edge_router_policy) | **PATCH** /service-edge-router-policies/{id} | Update the supplied fields on a service edge policy
[**update_service_edge_router_policy**](ServiceEdgeRouterPolicyApi.md#update_service_edge_router_policy) | **PUT** /service-edge-router-policies/{id} | Update all fields on a service edge policy


# **create_service_edge_router_policy**
> CreateEnvelope create_service_edge_router_policy(policy)

Create a service edge router policy resource

Create a service edge router policy resource. Requires admin access.

### Example

* Api Key Authentication (ztSession):
* OAuth Authentication (oauth2):
```python
import time
import os
import openziti_edge_management
from openziti_edge_management.models.create_envelope import CreateEnvelope
from openziti_edge_management.models.service_edge_router_policy_create import ServiceEdgeRouterPolicyCreate
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
    api_instance = openziti_edge_management.ServiceEdgeRouterPolicyApi(api_client)
    policy = openziti_edge_management.ServiceEdgeRouterPolicyCreate() # ServiceEdgeRouterPolicyCreate | A service edge router policy to create

    try:
        # Create a service edge router policy resource
        api_response = api_instance.create_service_edge_router_policy(policy)
        print("The response of ServiceEdgeRouterPolicyApi->create_service_edge_router_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceEdgeRouterPolicyApi->create_service_edge_router_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy** | [**ServiceEdgeRouterPolicyCreate**](ServiceEdgeRouterPolicyCreate.md)| A service edge router policy to create | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_service_edge_router_policy**
> Empty delete_service_edge_router_policy(id)

Delete a service edge policy

Delete a service edge policy by id. Requires admin access.

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
    api_instance = openziti_edge_management.ServiceEdgeRouterPolicyApi(api_client)
    id = 'id_example' # str | The id of the requested resource

    try:
        # Delete a service edge policy
        api_response = api_instance.delete_service_edge_router_policy(id)
        print("The response of ServiceEdgeRouterPolicyApi->delete_service_edge_router_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceEdgeRouterPolicyApi->delete_service_edge_router_policy: %s\n" % e)
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

# **detail_service_edge_router_policy**
> DetailServiceEdgePolicyEnvelope detail_service_edge_router_policy(id)

Retrieves a single service edge policy

Retrieves a single service edge policy by id. Requires admin access.

### Example

* Api Key Authentication (ztSession):
* OAuth Authentication (oauth2):
```python
import time
import os
import openziti_edge_management
from openziti_edge_management.models.detail_service_edge_policy_envelope import DetailServiceEdgePolicyEnvelope
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
    api_instance = openziti_edge_management.ServiceEdgeRouterPolicyApi(api_client)
    id = 'id_example' # str | The id of the requested resource

    try:
        # Retrieves a single service edge policy
        api_response = api_instance.detail_service_edge_router_policy(id)
        print("The response of ServiceEdgeRouterPolicyApi->detail_service_edge_router_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceEdgeRouterPolicyApi->detail_service_edge_router_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource | 

### Return type

[**DetailServiceEdgePolicyEnvelope**](DetailServiceEdgePolicyEnvelope.md)

### Authorization

[ztSession](../README.md#ztSession), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A single service edge router policy |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |
**404** | The requested resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_service_edge_router_policies**
> ListServiceEdgeRouterPoliciesEnvelope list_service_edge_router_policies(limit=limit, offset=offset, filter=filter)

List service edge router policies

Retrieves a list of service edge router policy resources; supports filtering, sorting, and pagination. Requires admin access. 

### Example

* Api Key Authentication (ztSession):
* OAuth Authentication (oauth2):
```python
import time
import os
import openziti_edge_management
from openziti_edge_management.models.list_service_edge_router_policies_envelope import ListServiceEdgeRouterPoliciesEnvelope
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
    api_instance = openziti_edge_management.ServiceEdgeRouterPolicyApi(api_client)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    filter = 'filter_example' # str |  (optional)

    try:
        # List service edge router policies
        api_response = api_instance.list_service_edge_router_policies(limit=limit, offset=offset, filter=filter)
        print("The response of ServiceEdgeRouterPolicyApi->list_service_edge_router_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceEdgeRouterPolicyApi->list_service_edge_router_policies: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **filter** | **str**|  | [optional] 

### Return type

[**ListServiceEdgeRouterPoliciesEnvelope**](ListServiceEdgeRouterPoliciesEnvelope.md)

### Authorization

[ztSession](../README.md#ztSession), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of service edge router policies |  -  |
**400** | The supplied request contains invalid fields or could not be parsed (json and non-json bodies). The error&#39;s code, message, and cause fields can be inspected for further information |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_service_edge_router_policy_edge_routers**
> ListEdgeRoutersEnvelope list_service_edge_router_policy_edge_routers(id)

List the edge routers that a service edge router policy applies to

List the edge routers that a service edge router policy applies to

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
    api_instance = openziti_edge_management.ServiceEdgeRouterPolicyApi(api_client)
    id = 'id_example' # str | The id of the requested resource

    try:
        # List the edge routers that a service edge router policy applies to
        api_response = api_instance.list_service_edge_router_policy_edge_routers(id)
        print("The response of ServiceEdgeRouterPolicyApi->list_service_edge_router_policy_edge_routers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceEdgeRouterPolicyApi->list_service_edge_router_policy_edge_routers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource | 

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
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |
**404** | The requested resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_service_edge_router_policy_services**
> ListServicesEnvelope list_service_edge_router_policy_services(id)

List the services that a service edge router policy applies to

List the services that a service edge router policy applies to

### Example

* Api Key Authentication (ztSession):
* OAuth Authentication (oauth2):
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openziti_edge_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openziti_edge_management.ServiceEdgeRouterPolicyApi(api_client)
    id = 'id_example' # str | The id of the requested resource

    try:
        # List the services that a service edge router policy applies to
        api_response = api_instance.list_service_edge_router_policy_services(id)
        print("The response of ServiceEdgeRouterPolicyApi->list_service_edge_router_policy_services:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceEdgeRouterPolicyApi->list_service_edge_router_policy_services: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource | 

### Return type

[**ListServicesEnvelope**](ListServicesEnvelope.md)

### Authorization

[ztSession](../README.md#ztSession), [oauth2](../README.md#oauth2)

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

# **patch_service_edge_router_policy**
> Empty patch_service_edge_router_policy(id, policy)

Update the supplied fields on a service edge policy

Update the supplied fields on a service edge policy. Requires admin access.

### Example

* Api Key Authentication (ztSession):
* OAuth Authentication (oauth2):
```python
import time
import os
import openziti_edge_management
from openziti_edge_management.models.empty import Empty
from openziti_edge_management.models.service_edge_router_policy_patch import ServiceEdgeRouterPolicyPatch
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
    api_instance = openziti_edge_management.ServiceEdgeRouterPolicyApi(api_client)
    id = 'id_example' # str | The id of the requested resource
    policy = openziti_edge_management.ServiceEdgeRouterPolicyPatch() # ServiceEdgeRouterPolicyPatch | A service edge router policy patch object

    try:
        # Update the supplied fields on a service edge policy
        api_response = api_instance.patch_service_edge_router_policy(id, policy)
        print("The response of ServiceEdgeRouterPolicyApi->patch_service_edge_router_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceEdgeRouterPolicyApi->patch_service_edge_router_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource | 
 **policy** | [**ServiceEdgeRouterPolicyPatch**](ServiceEdgeRouterPolicyPatch.md)| A service edge router policy patch object | 

### Return type

[**Empty**](Empty.md)

### Authorization

[ztSession](../README.md#ztSession), [oauth2](../README.md#oauth2)

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

# **update_service_edge_router_policy**
> Empty update_service_edge_router_policy(id, policy)

Update all fields on a service edge policy

Update all fields on a service edge policy by id. Requires admin access.

### Example

* Api Key Authentication (ztSession):
* OAuth Authentication (oauth2):
```python
import time
import os
import openziti_edge_management
from openziti_edge_management.models.empty import Empty
from openziti_edge_management.models.service_edge_router_policy_update import ServiceEdgeRouterPolicyUpdate
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
    api_instance = openziti_edge_management.ServiceEdgeRouterPolicyApi(api_client)
    id = 'id_example' # str | The id of the requested resource
    policy = openziti_edge_management.ServiceEdgeRouterPolicyUpdate() # ServiceEdgeRouterPolicyUpdate | A service edge router policy update object

    try:
        # Update all fields on a service edge policy
        api_response = api_instance.update_service_edge_router_policy(id, policy)
        print("The response of ServiceEdgeRouterPolicyApi->update_service_edge_router_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceEdgeRouterPolicyApi->update_service_edge_router_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource | 
 **policy** | [**ServiceEdgeRouterPolicyUpdate**](ServiceEdgeRouterPolicyUpdate.md)| A service edge router policy update object | 

### Return type

[**Empty**](Empty.md)

### Authorization

[ztSession](../README.md#ztSession), [oauth2](../README.md#oauth2)

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

