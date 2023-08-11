# openziti_edge_management.TracingApi

All URIs are relative to *https://demo.ziti.dev/edge/management/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**update_identity_tracing**](TracingApi.md#update_identity_tracing) | **PUT** /identities/{id}/trace | Enable/disable data flow tracing for an identity


# **update_identity_tracing**
> TraceDetailEnvelope update_identity_tracing(id, trace_spec)

Enable/disable data flow tracing for an identity

Allows an admin to enable/disable data flow tracing for an identity 

### Example

* Api Key Authentication (ztSession):
```python
import time
import os
import openziti_edge_management
from openziti_edge_management.models.trace_detail_envelope import TraceDetailEnvelope
from openziti_edge_management.models.trace_spec import TraceSpec
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
    api_instance = openziti_edge_management.TracingApi(api_client)
    id = 'id_example' # str | The id of the requested resource
    trace_spec = openziti_edge_management.TraceSpec() # TraceSpec | A traceSpec object

    try:
        # Enable/disable data flow tracing for an identity
        api_response = api_instance.update_identity_tracing(id, trace_spec)
        print("The response of TracingApi->update_identity_tracing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TracingApi->update_identity_tracing: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource | 
 **trace_spec** | [**TraceSpec**](TraceSpec.md)| A traceSpec object | 

### Return type

[**TraceDetailEnvelope**](TraceDetailEnvelope.md)

### Authorization

[ztSession](../README.md#ztSession)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the document that represents the trace state |  -  |
**400** | The supplied request contains invalid fields or could not be parsed (json and non-json bodies). The error&#39;s code, message, and cause fields can be inspected for further information |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |
**404** | The requested resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

