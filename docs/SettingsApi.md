# openziti_edge_management.SettingsApi

All URIs are relative to *https://demo.ziti.dev/edge/management/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_controller_setting**](SettingsApi.md#create_controller_setting) | **POST** /controller-settings | Create a controller specific setting
[**delete_controller_setting**](SettingsApi.md#delete_controller_setting) | **DELETE** /controller-settings/{id}/effective | Delete a controller setting object
[**detail_controller_setting**](SettingsApi.md#detail_controller_setting) | **GET** /controller-settings/{id} | Retrieves a single controller setting object.
[**detail_controller_setting_effective**](SettingsApi.md#detail_controller_setting_effective) | **GET** /controller-settings/{id}/effective | Retrieves a single controller&#39;s effective calculated settings from the instance and global configuration.
[**list_controller_settings**](SettingsApi.md#list_controller_settings) | **GET** /controller-settings | List controller settings
[**patch_controller_setting**](SettingsApi.md#patch_controller_setting) | **PATCH** /controller-settings/{id}/effective | Update the supplied fields on a controller setting object
[**update_controller_setting**](SettingsApi.md#update_controller_setting) | **PUT** /controller-settings/{id}/effective | Update all fields on a controller setting object


# **create_controller_setting**
> CreateEnvelope create_controller_setting(controller_setting)

Create a controller specific setting

Create a new controller specific settings object. Requires admin access.

### Example

* Api Key Authentication (ztSession):
* OAuth Authentication (oauth2):

```python
import time
import openziti_edge_management
from openziti_edge_management.api import settings_api
from openziti_edge_management.model.create_envelope import CreateEnvelope
from openziti_edge_management.model.api_error_envelope import ApiErrorEnvelope
from openziti_edge_management.model.controller_setting_create import ControllerSettingCreate
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
    api_instance = settings_api.SettingsApi(api_client)
    controller_setting = ControllerSettingCreate(None) # ControllerSettingCreate | A controller settings object to create

    # example passing only required values which don't have defaults set
    try:
        # Create a controller specific setting
        api_response = api_instance.create_controller_setting(controller_setting)
        pprint(api_response)
    except openziti_edge_management.ApiException as e:
        print("Exception when calling SettingsApi->create_controller_setting: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **controller_setting** | [**ControllerSettingCreate**](ControllerSettingCreate.md)| A controller settings object to create |

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
**401** | The supplied session does not have the correct access rights to request this resource |  -  |
**429** | The resource requested is rate limited and the rate limit has been exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_controller_setting**
> Empty delete_controller_setting(id)

Delete a controller setting object

Delete a controller setting object by id. Requires admin access.

### Example

* Api Key Authentication (ztSession):
* OAuth Authentication (oauth2):

```python
import time
import openziti_edge_management
from openziti_edge_management.api import settings_api
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
    api_instance = settings_api.SettingsApi(api_client)
    id = "id_example" # str | The id of the requested resource

    # example passing only required values which don't have defaults set
    try:
        # Delete a controller setting object
        api_response = api_instance.delete_controller_setting(id)
        pprint(api_response)
    except openziti_edge_management.ApiException as e:
        print("Exception when calling SettingsApi->delete_controller_setting: %s\n" % e)
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
**401** | The supplied session does not have the correct access rights to request this resource |  -  |
**409** | The resource requested to be removed/altered cannot be as it is referenced by another object. |  -  |
**429** | The resource requested is rate limited and the rate limit has been exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detail_controller_setting**
> DetailControllerSettingEnvelope detail_controller_setting(id)

Retrieves a single controller setting object.

Retrieves a single controller setting object by id. Requires admin access.

### Example

* Api Key Authentication (ztSession):
* OAuth Authentication (oauth2):

```python
import time
import openziti_edge_management
from openziti_edge_management.api import settings_api
from openziti_edge_management.model.detail_controller_setting_envelope import DetailControllerSettingEnvelope
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
    api_instance = settings_api.SettingsApi(api_client)
    id = "id_example" # str | The id of the requested resource

    # example passing only required values which don't have defaults set
    try:
        # Retrieves a single controller setting object.
        api_response = api_instance.detail_controller_setting(id)
        pprint(api_response)
    except openziti_edge_management.ApiException as e:
        print("Exception when calling SettingsApi->detail_controller_setting: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource |

### Return type

[**DetailControllerSettingEnvelope**](DetailControllerSettingEnvelope.md)

### Authorization

[ztSession](../README.md#ztSession), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A singular controller setting object |  -  |
**401** | The supplied session does not have the correct access rights to request this resource |  -  |
**404** | The requested resource does not exist |  -  |
**429** | The resource requested is rate limited and the rate limit has been exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detail_controller_setting_effective**
> DetailControllerSettingEffectiveEnvelope detail_controller_setting_effective(id)

Retrieves a single controller's effective calculated settings from the instance and global configuration.

Retrieves a single controller's effective setting object by id. Requires admin access.

### Example

* Api Key Authentication (ztSession):
* OAuth Authentication (oauth2):

```python
import time
import openziti_edge_management
from openziti_edge_management.api import settings_api
from openziti_edge_management.model.api_error_envelope import ApiErrorEnvelope
from openziti_edge_management.model.detail_controller_setting_effective_envelope import DetailControllerSettingEffectiveEnvelope
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
    api_instance = settings_api.SettingsApi(api_client)
    id = "id_example" # str | The id of the requested resource

    # example passing only required values which don't have defaults set
    try:
        # Retrieves a single controller's effective calculated settings from the instance and global configuration.
        api_response = api_instance.detail_controller_setting_effective(id)
        pprint(api_response)
    except openziti_edge_management.ApiException as e:
        print("Exception when calling SettingsApi->detail_controller_setting_effective: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource |

### Return type

[**DetailControllerSettingEffectiveEnvelope**](DetailControllerSettingEffectiveEnvelope.md)

### Authorization

[ztSession](../README.md#ztSession), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A singular controller&#39;s effective setting object |  -  |
**401** | The supplied session does not have the correct access rights to request this resource |  -  |
**404** | The requested resource does not exist |  -  |
**429** | The resource requested is rate limited and the rate limit has been exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_controller_settings**
> ListControllerSettingEnvelope list_controller_settings()

List controller settings

Retrieves a list controller settings including the base `global` settings object and any overriding controller specific settings. 

### Example

* Api Key Authentication (ztSession):
* OAuth Authentication (oauth2):

```python
import time
import openziti_edge_management
from openziti_edge_management.api import settings_api
from openziti_edge_management.model.api_error_envelope import ApiErrorEnvelope
from openziti_edge_management.model.list_controller_setting_envelope import ListControllerSettingEnvelope
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
    api_instance = settings_api.SettingsApi(api_client)
    limit = 1 # int |  (optional)
    offset = 1 # int |  (optional)
    filter = "filter_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List controller settings
        api_response = api_instance.list_controller_settings(limit=limit, offset=offset, filter=filter)
        pprint(api_response)
    except openziti_edge_management.ApiException as e:
        print("Exception when calling SettingsApi->list_controller_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional]
 **offset** | **int**|  | [optional]
 **filter** | **str**|  | [optional]

### Return type

[**ListControllerSettingEnvelope**](ListControllerSettingEnvelope.md)

### Authorization

[ztSession](../README.md#ztSession), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of controller setting objects |  -  |
**400** | The supplied request contains invalid fields or could not be parsed (json and non-json bodies). The error&#39;s code, message, and cause fields can be inspected for further information |  -  |
**401** | The supplied session does not have the correct access rights to request this resource |  -  |
**429** | The resource requested is rate limited and the rate limit has been exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_controller_setting**
> Empty patch_controller_setting(id, controller_setting)

Update the supplied fields on a controller setting object

Update the supplied fields on a controller setting object. Requires admin access.

### Example

* Api Key Authentication (ztSession):
* OAuth Authentication (oauth2):

```python
import time
import openziti_edge_management
from openziti_edge_management.api import settings_api
from openziti_edge_management.model.api_error_envelope import ApiErrorEnvelope
from openziti_edge_management.model.empty import Empty
from openziti_edge_management.model.controller_setting_patch import ControllerSettingPatch
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
    api_instance = settings_api.SettingsApi(api_client)
    id = "id_example" # str | The id of the requested resource
    controller_setting = ControllerSettingPatch(None) # ControllerSettingPatch | A controller setting object patch object

    # example passing only required values which don't have defaults set
    try:
        # Update the supplied fields on a controller setting object
        api_response = api_instance.patch_controller_setting(id, controller_setting)
        pprint(api_response)
    except openziti_edge_management.ApiException as e:
        print("Exception when calling SettingsApi->patch_controller_setting: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource |
 **controller_setting** | [**ControllerSettingPatch**](ControllerSettingPatch.md)| A controller setting object patch object |

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
**401** | The supplied session does not have the correct access rights to request this resource |  -  |
**404** | The requested resource does not exist |  -  |
**429** | The resource requested is rate limited and the rate limit has been exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_controller_setting**
> Empty update_controller_setting(id, controller_setting)

Update all fields on a controller setting object

Update all fields on a controller setting object by id. Requires admin access.

### Example

* Api Key Authentication (ztSession):
* OAuth Authentication (oauth2):

```python
import time
import openziti_edge_management
from openziti_edge_management.api import settings_api
from openziti_edge_management.model.api_error_envelope import ApiErrorEnvelope
from openziti_edge_management.model.controller_setting_update import ControllerSettingUpdate
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
    api_instance = settings_api.SettingsApi(api_client)
    id = "id_example" # str | The id of the requested resource
    controller_setting = ControllerSettingUpdate(None) # ControllerSettingUpdate | A controller setting update object

    # example passing only required values which don't have defaults set
    try:
        # Update all fields on a controller setting object
        api_response = api_instance.update_controller_setting(id, controller_setting)
        pprint(api_response)
    except openziti_edge_management.ApiException as e:
        print("Exception when calling SettingsApi->update_controller_setting: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource |
 **controller_setting** | [**ControllerSettingUpdate**](ControllerSettingUpdate.md)| A controller setting update object |

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
**401** | The supplied session does not have the correct access rights to request this resource |  -  |
**404** | The requested resource does not exist |  -  |
**429** | The resource requested is rate limited and the rate limit has been exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

