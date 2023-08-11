# openziti_edge_management.InformationalApi

All URIs are relative to *https://demo.ziti.dev/edge/management/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**detail_spec**](InformationalApi.md#detail_spec) | **GET** /specs/{id} | Return a single spec resource
[**detail_spec_body**](InformationalApi.md#detail_spec_body) | **GET** /specs/{id}/spec | Returns the spec&#39;s file
[**list_root**](InformationalApi.md#list_root) | **GET** / | Returns version information
[**list_specs**](InformationalApi.md#list_specs) | **GET** /specs | Returns a list of API specs
[**list_summary**](InformationalApi.md#list_summary) | **GET** /summary | Returns a list of accessible resource counts
[**list_version**](InformationalApi.md#list_version) | **GET** /version | Returns version information


# **detail_spec**
> DetailSpecEnvelope detail_spec(id)

Return a single spec resource

Returns single spec resource embedded within the controller for consumption/documentation/code geneartion

### Example

```python
import time
import os
import openziti_edge_management
from openziti_edge_management.models.detail_spec_envelope import DetailSpecEnvelope
from openziti_edge_management.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://demo.ziti.dev/edge/management/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openziti_edge_management.Configuration(
    host = "https://demo.ziti.dev/edge/management/v1"
)


# Enter a context with an instance of the API client
with openziti_edge_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openziti_edge_management.InformationalApi(api_client)
    id = 'id_example' # str | The id of the requested resource

    try:
        # Return a single spec resource
        api_response = api_instance.detail_spec(id)
        print("The response of InformationalApi->detail_spec:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InformationalApi->detail_spec: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource | 

### Return type

[**DetailSpecEnvelope**](DetailSpecEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A single specification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detail_spec_body**
> DetailSpecBodyEnvelope detail_spec_body(id)

Returns the spec's file

Return the body of the specification (i.e. Swagger, OpenAPI 2.0, 3.0, etc).

### Example

```python
import time
import os
import openziti_edge_management
from openziti_edge_management.models.detail_spec_body_envelope import DetailSpecBodyEnvelope
from openziti_edge_management.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://demo.ziti.dev/edge/management/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openziti_edge_management.Configuration(
    host = "https://demo.ziti.dev/edge/management/v1"
)


# Enter a context with an instance of the API client
with openziti_edge_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openziti_edge_management.InformationalApi(api_client)
    id = 'id_example' # str | The id of the requested resource

    try:
        # Returns the spec's file
        api_response = api_instance.detail_spec_body(id)
        print("The response of InformationalApi->detail_spec_body:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InformationalApi->detail_spec_body: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource | 

### Return type

[**DetailSpecBodyEnvelope**](DetailSpecBodyEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/yaml, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the document that represents the specification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_root**
> ListVersionEnvelope list_root()

Returns version information

### Example

```python
import time
import os
import openziti_edge_management
from openziti_edge_management.models.list_version_envelope import ListVersionEnvelope
from openziti_edge_management.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://demo.ziti.dev/edge/management/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openziti_edge_management.Configuration(
    host = "https://demo.ziti.dev/edge/management/v1"
)


# Enter a context with an instance of the API client
with openziti_edge_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openziti_edge_management.InformationalApi(api_client)

    try:
        # Returns version information
        api_response = api_instance.list_root()
        print("The response of InformationalApi->list_root:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InformationalApi->list_root: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ListVersionEnvelope**](ListVersionEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Version information for the controller |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_specs**
> ListSpecsEnvelope list_specs()

Returns a list of API specs

Returns a list of spec files embedded within the controller for consumption/documentation/code geneartion

### Example

```python
import time
import os
import openziti_edge_management
from openziti_edge_management.models.list_specs_envelope import ListSpecsEnvelope
from openziti_edge_management.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://demo.ziti.dev/edge/management/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openziti_edge_management.Configuration(
    host = "https://demo.ziti.dev/edge/management/v1"
)


# Enter a context with an instance of the API client
with openziti_edge_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openziti_edge_management.InformationalApi(api_client)

    try:
        # Returns a list of API specs
        api_response = api_instance.list_specs()
        print("The response of InformationalApi->list_specs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InformationalApi->list_specs: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ListSpecsEnvelope**](ListSpecsEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of specifications |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_summary**
> ListSummaryCountsEnvelope list_summary()

Returns a list of accessible resource counts

This endpoint is usefull for UIs that wish to display UI elements with counts.

### Example

* Api Key Authentication (ztSession):
```python
import time
import os
import openziti_edge_management
from openziti_edge_management.models.list_summary_counts_envelope import ListSummaryCountsEnvelope
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
    api_instance = openziti_edge_management.InformationalApi(api_client)

    try:
        # Returns a list of accessible resource counts
        api_response = api_instance.list_summary()
        print("The response of InformationalApi->list_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InformationalApi->list_summary: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ListSummaryCountsEnvelope**](ListSummaryCountsEnvelope.md)

### Authorization

[ztSession](../README.md#ztSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Entity counts scopped to the current identitie&#39;s access |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_version**
> ListVersionEnvelope list_version()

Returns version information

### Example

```python
import time
import os
import openziti_edge_management
from openziti_edge_management.models.list_version_envelope import ListVersionEnvelope
from openziti_edge_management.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://demo.ziti.dev/edge/management/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openziti_edge_management.Configuration(
    host = "https://demo.ziti.dev/edge/management/v1"
)


# Enter a context with an instance of the API client
with openziti_edge_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openziti_edge_management.InformationalApi(api_client)

    try:
        # Returns version information
        api_response = api_instance.list_version()
        print("The response of InformationalApi->list_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InformationalApi->list_version: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ListVersionEnvelope**](ListVersionEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Version information for the controller |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

