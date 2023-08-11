# openziti_edge_management.DatabaseApi

All URIs are relative to *https://demo.ziti.dev/edge/management/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_data_integrity**](DatabaseApi.md#check_data_integrity) | **POST** /database/check-data-integrity | Starts a data integrity scan on the datastore
[**create_database_snapshot**](DatabaseApi.md#create_database_snapshot) | **POST** /database/snapshot | Create a new database snapshot
[**data_integrity_results**](DatabaseApi.md#data_integrity_results) | **GET** /database/data-integrity-results | Returns any results found from in-progress integrity checks
[**fix_data_integrity**](DatabaseApi.md#fix_data_integrity) | **POST** /database/fix-data-integrity | Runs a data integrity scan on the datastore, attempts to fix any issues it can and returns any found issues


# **check_data_integrity**
> Empty check_data_integrity()

Starts a data integrity scan on the datastore

Starts a data integrity scan on the datastore. Requires admin access. Only once instance may run at a time, including runs of fixDataIntegrity.

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
    api_instance = openziti_edge_management.DatabaseApi(api_client)

    try:
        # Starts a data integrity scan on the datastore
        api_response = api_instance.check_data_integrity()
        print("The response of DatabaseApi->check_data_integrity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabaseApi->check_data_integrity: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

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
**202** | Base empty response |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |
**429** | The resource requested is rate limited and the rate limit has been exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_database_snapshot**
> Empty create_database_snapshot()

Create a new database snapshot

Create a new database snapshot. Requires admin access.

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
    api_instance = openziti_edge_management.DatabaseApi(api_client)

    try:
        # Create a new database snapshot
        api_response = api_instance.create_database_snapshot()
        print("The response of DatabaseApi->create_database_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabaseApi->create_database_snapshot: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

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
**200** | Base empty response |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |
**429** | The resource requested is rate limited and the rate limit has been exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_integrity_results**
> DataIntegrityCheckResultEnvelope data_integrity_results()

Returns any results found from in-progress integrity checks

Returns any results found from in-progress integrity checks. Requires admin access.

### Example

* Api Key Authentication (ztSession):
```python
import time
import os
import openziti_edge_management
from openziti_edge_management.models.data_integrity_check_result_envelope import DataIntegrityCheckResultEnvelope
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
    api_instance = openziti_edge_management.DatabaseApi(api_client)

    try:
        # Returns any results found from in-progress integrity checks
        api_response = api_instance.data_integrity_results()
        print("The response of DatabaseApi->data_integrity_results:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabaseApi->data_integrity_results: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**DataIntegrityCheckResultEnvelope**](DataIntegrityCheckResultEnvelope.md)

### Authorization

[ztSession](../README.md#ztSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of data integrity issues found |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fix_data_integrity**
> Empty fix_data_integrity()

Runs a data integrity scan on the datastore, attempts to fix any issues it can and returns any found issues

Runs a data integrity scan on the datastore, attempts to fix any issues it can, and returns any found issues. Requires admin access. Only once instance may run at a time, including runs of checkDataIntegrity.

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
    api_instance = openziti_edge_management.DatabaseApi(api_client)

    try:
        # Runs a data integrity scan on the datastore, attempts to fix any issues it can and returns any found issues
        api_response = api_instance.fix_data_integrity()
        print("The response of DatabaseApi->fix_data_integrity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabaseApi->fix_data_integrity: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

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
**202** | Base empty response |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |
**429** | The resource requested is rate limited and the rate limit has been exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

