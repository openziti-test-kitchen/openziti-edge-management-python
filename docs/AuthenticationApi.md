# openziti_edge_management.AuthenticationApi

All URIs are relative to *https://demo.ziti.dev/edge/management/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authenticate**](AuthenticationApi.md#authenticate) | **POST** /authenticate | Authenticate via a method supplied via a query string parameter
[**authenticate_mfa**](AuthenticationApi.md#authenticate_mfa) | **POST** /authenticate/mfa | Complete MFA authentication


# **authenticate**
> CurrentApiSessionDetailEnvelope authenticate(method, auth=auth)

Authenticate via a method supplied via a query string parameter

Allowed authentication methods include \"password\", \"cert\", and \"ext-jwt\" 

### Example

```python
import time
import os
import openziti_edge_management
from openziti_edge_management.models.authenticate import Authenticate
from openziti_edge_management.models.current_api_session_detail_envelope import CurrentApiSessionDetailEnvelope
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
    api_instance = openziti_edge_management.AuthenticationApi(api_client)
    method = 'method_example' # str | 
    auth = openziti_edge_management.Authenticate() # Authenticate |  (optional)

    try:
        # Authenticate via a method supplied via a query string parameter
        api_response = api_instance.authenticate(method, auth=auth)
        print("The response of AuthenticationApi->authenticate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->authenticate: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **method** | **str**|  | 
 **auth** | [**Authenticate**](Authenticate.md)|  | [optional] 

### Return type

[**CurrentApiSessionDetailEnvelope**](CurrentApiSessionDetailEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, default

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The API session associated with the session used to issue the request |  -  |
**400** | The supplied request contains invalid fields or could not be parsed (json and non-json bodies). The error&#39;s code, message, and cause fields can be inspected for further information |  -  |
**401** | The authentication request could not be processed as the credentials are invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authenticate_mfa**
> Empty authenticate_mfa(mfa_auth)

Complete MFA authentication

Completes MFA authentication by submitting a MFA time based one time token or backup code.

### Example

* Api Key Authentication (ztSession):
* OAuth Authentication (oauth2):
```python
import time
import os
import openziti_edge_management
from openziti_edge_management.models.empty import Empty
from openziti_edge_management.models.mfa_code import MfaCode
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
    api_instance = openziti_edge_management.AuthenticationApi(api_client)
    mfa_auth = openziti_edge_management.MfaCode() # MfaCode | An MFA validation request

    try:
        # Complete MFA authentication
        api_response = api_instance.authenticate_mfa(mfa_auth)
        print("The response of AuthenticationApi->authenticate_mfa:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->authenticate_mfa: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mfa_auth** | [**MfaCode**](MfaCode.md)| An MFA validation request | 

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
**200** | Base empty response |  -  |
**401** | Base empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

