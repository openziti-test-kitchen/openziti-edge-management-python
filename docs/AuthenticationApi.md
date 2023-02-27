# openziti_edge_management.AuthenticationApi

All URIs are relative to *https://demo.ziti.dev/edge/management/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authenticate**](AuthenticationApi.md#authenticate) | **POST** /authenticate | Authenticate via a method supplied via a query string parameter
[**authenticate_mfa**](AuthenticationApi.md#authenticate_mfa) | **POST** /authenticate/mfa | Complete MFA authentication


# **authenticate**
> CurrentApiSessionDetailEnvelope authenticate(method)

Authenticate via a method supplied via a query string parameter

Allows authentication  Methods include \"password\" and \"cert\" 

### Example


```python
import time
import openziti_edge_management
from openziti_edge_management.api import authentication_api
from openziti_edge_management.model.current_api_session_detail_envelope import CurrentApiSessionDetailEnvelope
from openziti_edge_management.model.authenticate import Authenticate
from openziti_edge_management.model.api_error_envelope import ApiErrorEnvelope
from pprint import pprint
# Defining the host is optional and defaults to https://demo.ziti.dev/edge/management/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openziti_edge_management.Configuration(
    host = "https://demo.ziti.dev/edge/management/v1"
)


# Enter a context with an instance of the API client
with openziti_edge_management.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = authentication_api.AuthenticationApi(api_client)
    method = "password" # str | 
    auth = Authenticate(
        config_types=ConfigTypes([
            "config_types_example",
        ]),
        env_info=EnvInfo(
            arch="arch_example",
            os="os_example",
            os_release="os_release_example",
            os_version="os_version_example",
        ),
        password=Password("password_example"),
        sdk_info=SdkInfo(
            app_id="app_id_example",
            app_version="app_version_example",
            branch="branch_example",
            revision="revision_example",
            type="type_example",
            version="version_example",
        ),
        username=Username("username_example"),
    ) # Authenticate |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Authenticate via a method supplied via a query string parameter
        api_response = api_instance.authenticate(method)
        pprint(api_response)
    except openziti_edge_management.ApiException as e:
        print("Exception when calling AuthenticationApi->authenticate: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Authenticate via a method supplied via a query string parameter
        api_response = api_instance.authenticate(method, auth=auth)
        pprint(api_response)
    except openziti_edge_management.ApiException as e:
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
**403** | The authentication request could not be processed as the credentials are invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authenticate_mfa**
> Empty authenticate_mfa(mfa_auth)

Complete MFA authentication

Completes MFA authentication by submitting a MFA time based one time token or backup code.

### Example

* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_management
from openziti_edge_management.api import authentication_api
from openziti_edge_management.model.mfa_code import MfaCode
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

# Enter a context with an instance of the API client
with openziti_edge_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentication_api.AuthenticationApi(api_client)
    mfa_auth = MfaCode(
        code="code_example",
    ) # MfaCode | An MFA validation request

    # example passing only required values which don't have defaults set
    try:
        # Complete MFA authentication
        api_response = api_instance.authenticate_mfa(mfa_auth)
        pprint(api_response)
    except openziti_edge_management.ApiException as e:
        print("Exception when calling AuthenticationApi->authenticate_mfa: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mfa_auth** | [**MfaCode**](MfaCode.md)| An MFA validation request |

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
**200** | Base empty response |  -  |
**401** | Base empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

