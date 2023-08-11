# openziti_edge_management.ServiceApi

All URIs are relative to *https://demo.ziti.dev/edge/management/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_service**](ServiceApi.md#create_service) | **POST** /services | Create a services resource
[**delete_service**](ServiceApi.md#delete_service) | **DELETE** /services/{id} | Delete a service
[**detail_service**](ServiceApi.md#detail_service) | **GET** /services/{id} | Retrieves a single service
[**list_service_config**](ServiceApi.md#list_service_config) | **GET** /services/{id}/configs | List configs associated to a specific service
[**list_service_edge_routers**](ServiceApi.md#list_service_edge_routers) | **GET** /services/{id}/edge-routers | List accessible edge-routers
[**list_service_identities**](ServiceApi.md#list_service_identities) | **GET** /services/{id}/identities | List identities with access
[**list_service_service_edge_router_policies**](ServiceApi.md#list_service_service_edge_router_policies) | **GET** /services/{id}/service-edge-router-policies | List service edge router policies that affect a specific service
[**list_service_service_policies**](ServiceApi.md#list_service_service_policies) | **GET** /services/{id}/service-policies | List service policies that affect a specific service
[**list_service_terminators**](ServiceApi.md#list_service_terminators) | **GET** /services/{id}/terminators | List of terminators assigned to a service
[**list_services**](ServiceApi.md#list_services) | **GET** /services | List services
[**patch_service**](ServiceApi.md#patch_service) | **PATCH** /services/{id} | Update the supplied fields on a service
[**update_service**](ServiceApi.md#update_service) | **PUT** /services/{id} | Update all fields on a service


# **create_service**
> CreateEnvelope create_service(service)

Create a services resource

Create a services resource. Requires admin access.

### Example

* Api Key Authentication (ztSession):
* OAuth Authentication (oauth2):
```python
import time
import os
import openziti_edge_management
from openziti_edge_management.models.create_envelope import CreateEnvelope
from openziti_edge_management.models.service_create import ServiceCreate
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
    api_instance = openziti_edge_management.ServiceApi(api_client)
    service = openziti_edge_management.ServiceCreate() # ServiceCreate | A service to create

    try:
        # Create a services resource
        api_response = api_instance.create_service(service)
        print("The response of ServiceApi->create_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceApi->create_service: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | [**ServiceCreate**](ServiceCreate.md)| A service to create | 

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

# **delete_service**
> Empty delete_service(id)

Delete a service

Delete a service by id. Requires admin access.

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
    api_instance = openziti_edge_management.ServiceApi(api_client)
    id = 'id_example' # str | The id of the requested resource

    try:
        # Delete a service
        api_response = api_instance.delete_service(id)
        print("The response of ServiceApi->delete_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceApi->delete_service: %s\n" % e)
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

# **detail_service**
> DetailServiceEnvelope detail_service(id)

Retrieves a single service

Retrieves a single service by id. Requires admin access.

### Example

* Api Key Authentication (ztSession):
* OAuth Authentication (oauth2):
```python
import time
import os
import openziti_edge_management
from openziti_edge_management.models.detail_service_envelope import DetailServiceEnvelope
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
    api_instance = openziti_edge_management.ServiceApi(api_client)
    id = 'id_example' # str | The id of the requested resource

    try:
        # Retrieves a single service
        api_response = api_instance.detail_service(id)
        print("The response of ServiceApi->detail_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceApi->detail_service: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource | 

### Return type

[**DetailServiceEnvelope**](DetailServiceEnvelope.md)

### Authorization

[ztSession](../README.md#ztSession), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A single service |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |
**404** | The requested resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_service_config**
> ListConfigsEnvelope list_service_config(id, limit=limit, offset=offset, filter=filter)

List configs associated to a specific service

Retrieves a list of config resources associated to a specific service; supports filtering, sorting, and pagination. Requires admin access. 

### Example

* Api Key Authentication (ztSession):
* OAuth Authentication (oauth2):
```python
import time
import os
import openziti_edge_management
from openziti_edge_management.models.list_configs_envelope import ListConfigsEnvelope
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
    api_instance = openziti_edge_management.ServiceApi(api_client)
    id = 'id_example' # str | The id of the requested resource
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    filter = 'filter_example' # str |  (optional)

    try:
        # List configs associated to a specific service
        api_response = api_instance.list_service_config(id, limit=limit, offset=offset, filter=filter)
        print("The response of ServiceApi->list_service_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceApi->list_service_config: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **filter** | **str**|  | [optional] 

### Return type

[**ListConfigsEnvelope**](ListConfigsEnvelope.md)

### Authorization

[ztSession](../README.md#ztSession), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of configs |  -  |
**400** | The supplied request contains invalid fields or could not be parsed (json and non-json bodies). The error&#39;s code, message, and cause fields can be inspected for further information |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_service_edge_routers**
> ListEdgeRoutersEnvelope list_service_edge_routers(id, limit=limit, offset=offset, filter=filter)

List accessible edge-routers

Retrieves a list of edge-routers that may be used to access the given service. Supports filtering, sorting, and pagination. Requires admin access. 

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
    api_instance = openziti_edge_management.ServiceApi(api_client)
    id = 'id_example' # str | The id of the requested resource
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    filter = 'filter_example' # str |  (optional)

    try:
        # List accessible edge-routers
        api_response = api_instance.list_service_edge_routers(id, limit=limit, offset=offset, filter=filter)
        print("The response of ServiceApi->list_service_edge_routers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceApi->list_service_edge_routers: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **filter** | **str**|  | [optional] 

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

# **list_service_identities**
> ListIdentitiesEnvelope list_service_identities(id, limit=limit, offset=offset, filter=filter)

List identities with access

Retrieves a list of identities that have access to this service. Supports filtering, sorting, and pagination. Requires admin access. 

### Example

* Api Key Authentication (ztSession):
* OAuth Authentication (oauth2):
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openziti_edge_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openziti_edge_management.ServiceApi(api_client)
    id = 'id_example' # str | The id of the requested resource
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    filter = 'filter_example' # str |  (optional)

    try:
        # List identities with access
        api_response = api_instance.list_service_identities(id, limit=limit, offset=offset, filter=filter)
        print("The response of ServiceApi->list_service_identities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceApi->list_service_identities: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **filter** | **str**|  | [optional] 

### Return type

[**ListIdentitiesEnvelope**](ListIdentitiesEnvelope.md)

### Authorization

[ztSession](../README.md#ztSession), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of identities |  -  |
**400** | The supplied request contains invalid fields or could not be parsed (json and non-json bodies). The error&#39;s code, message, and cause fields can be inspected for further information |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_service_service_edge_router_policies**
> ListServiceEdgeRouterPoliciesEnvelope list_service_service_edge_router_policies(id, limit=limit, offset=offset, filter=filter)

List service edge router policies that affect a specific service

Retrieves a list of service edge router policy resources that affect a specific service; supports filtering, sorting, and pagination. Requires admin access. 

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
    api_instance = openziti_edge_management.ServiceApi(api_client)
    id = 'id_example' # str | The id of the requested resource
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    filter = 'filter_example' # str |  (optional)

    try:
        # List service edge router policies that affect a specific service
        api_response = api_instance.list_service_service_edge_router_policies(id, limit=limit, offset=offset, filter=filter)
        print("The response of ServiceApi->list_service_service_edge_router_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceApi->list_service_service_edge_router_policies: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource | 
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

# **list_service_service_policies**
> ListServicePoliciesEnvelope list_service_service_policies(id, limit=limit, offset=offset, filter=filter)

List service policies that affect a specific service

Retrieves a list of service policy resources that affect specific service; supports filtering, sorting, and pagination. Requires admin access. 

### Example

* Api Key Authentication (ztSession):
* OAuth Authentication (oauth2):
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openziti_edge_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openziti_edge_management.ServiceApi(api_client)
    id = 'id_example' # str | The id of the requested resource
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    filter = 'filter_example' # str |  (optional)

    try:
        # List service policies that affect a specific service
        api_response = api_instance.list_service_service_policies(id, limit=limit, offset=offset, filter=filter)
        print("The response of ServiceApi->list_service_service_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceApi->list_service_service_policies: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **filter** | **str**|  | [optional] 

### Return type

[**ListServicePoliciesEnvelope**](ListServicePoliciesEnvelope.md)

### Authorization

[ztSession](../README.md#ztSession), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of service policies |  -  |
**400** | The supplied request contains invalid fields or could not be parsed (json and non-json bodies). The error&#39;s code, message, and cause fields can be inspected for further information |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_service_terminators**
> ListTerminatorsEnvelope list_service_terminators(id, limit=limit, offset=offset, filter=filter)

List of terminators assigned to a service

Retrieves a list of terminator resources that are assigned specific service; supports filtering, sorting, and pagination. 

### Example

* Api Key Authentication (ztSession):
* OAuth Authentication (oauth2):
```python
import time
import os
import openziti_edge_management
from openziti_edge_management.models.list_terminators_envelope import ListTerminatorsEnvelope
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
    api_instance = openziti_edge_management.ServiceApi(api_client)
    id = 'id_example' # str | The id of the requested resource
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    filter = 'filter_example' # str |  (optional)

    try:
        # List of terminators assigned to a service
        api_response = api_instance.list_service_terminators(id, limit=limit, offset=offset, filter=filter)
        print("The response of ServiceApi->list_service_terminators:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceApi->list_service_terminators: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **filter** | **str**|  | [optional] 

### Return type

[**ListTerminatorsEnvelope**](ListTerminatorsEnvelope.md)

### Authorization

[ztSession](../README.md#ztSession), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of terminators |  -  |
**400** | The supplied request contains invalid fields or could not be parsed (json and non-json bodies). The error&#39;s code, message, and cause fields can be inspected for further information |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_services**
> ListServicesEnvelope list_services(limit=limit, offset=offset, filter=filter, role_filter=role_filter, role_semantic=role_semantic)

List services

Retrieves a list of config resources; supports filtering, sorting, and pagination. Requires admin access. 

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
    api_instance = openziti_edge_management.ServiceApi(api_client)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    filter = 'filter_example' # str |  (optional)
    role_filter = ['role_filter_example'] # List[str] |  (optional)
    role_semantic = 'role_semantic_example' # str |  (optional)

    try:
        # List services
        api_response = api_instance.list_services(limit=limit, offset=offset, filter=filter, role_filter=role_filter, role_semantic=role_semantic)
        print("The response of ServiceApi->list_services:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceApi->list_services: %s\n" % e)
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
**400** | The supplied request contains invalid fields or could not be parsed (json and non-json bodies). The error&#39;s code, message, and cause fields can be inspected for further information |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_service**
> Empty patch_service(id, service)

Update the supplied fields on a service

Update the supplied fields on a service. Requires admin access.

### Example

* Api Key Authentication (ztSession):
* OAuth Authentication (oauth2):
```python
import time
import os
import openziti_edge_management
from openziti_edge_management.models.empty import Empty
from openziti_edge_management.models.service_patch import ServicePatch
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
    api_instance = openziti_edge_management.ServiceApi(api_client)
    id = 'id_example' # str | The id of the requested resource
    service = openziti_edge_management.ServicePatch() # ServicePatch | A service patch object

    try:
        # Update the supplied fields on a service
        api_response = api_instance.patch_service(id, service)
        print("The response of ServiceApi->patch_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceApi->patch_service: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource | 
 **service** | [**ServicePatch**](ServicePatch.md)| A service patch object | 

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

# **update_service**
> Empty update_service(id, service)

Update all fields on a service

Update all fields on a service by id. Requires admin access.

### Example

* Api Key Authentication (ztSession):
* OAuth Authentication (oauth2):
```python
import time
import os
import openziti_edge_management
from openziti_edge_management.models.empty import Empty
from openziti_edge_management.models.service_update import ServiceUpdate
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
    api_instance = openziti_edge_management.ServiceApi(api_client)
    id = 'id_example' # str | The id of the requested resource
    service = openziti_edge_management.ServiceUpdate() # ServiceUpdate | A service update object

    try:
        # Update all fields on a service
        api_response = api_instance.update_service(id, service)
        print("The response of ServiceApi->update_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceApi->update_service: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource | 
 **service** | [**ServiceUpdate**](ServiceUpdate.md)| A service update object | 

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

