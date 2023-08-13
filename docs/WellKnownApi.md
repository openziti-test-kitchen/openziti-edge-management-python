# openziti_edge_management.WellKnownApi

All URIs are relative to *https://demo.ziti.dev/edge/management/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_well_known_cas**](WellKnownApi.md#list_well_known_cas) | **GET** /.well-known/est/cacerts | Get CA Cert Store


# **list_well_known_cas**
> str list_well_known_cas()

Get CA Cert Store

This endpoint is used during enrollments to bootstrap trust between enrolling clients and the Ziti Edge API. This endpoint returns a base64 encoded PKCS7 store. The content can be base64 decoded and parsed by any library that supports parsing PKCS7 stores. 

### Example

```python
import time
import os
import openziti_edge_management
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
    api_instance = openziti_edge_management.WellKnownApi(api_client)

    try:
        # Get CA Cert Store
        api_response = api_instance.list_well_known_cas()
        print("The response of WellKnownApi->list_well_known_cas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WellKnownApi->list_well_known_cas: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pkcs7-mime

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A base64 encoded PKCS7 store |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

