# openziti_edge_management.CurrentIdentityApi

All URIs are relative to *https://demo.ziti.dev/edge/management/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_mfa_recovery_codes**](CurrentIdentityApi.md#create_mfa_recovery_codes) | **POST** /current-identity/mfa/recovery-codes | For a completed MFA enrollment regenerate the recovery codes
[**delete_mfa**](CurrentIdentityApi.md#delete_mfa) | **DELETE** /current-identity/mfa | Disable MFA for the current identity
[**detail_mfa**](CurrentIdentityApi.md#detail_mfa) | **GET** /current-identity/mfa | Returns the current status of MFA enrollment
[**detail_mfa_qr_code**](CurrentIdentityApi.md#detail_mfa_qr_code) | **GET** /current-identity/mfa/qr-code | Show a QR code for unverified MFA enrollments
[**detail_mfa_recovery_codes**](CurrentIdentityApi.md#detail_mfa_recovery_codes) | **GET** /current-identity/mfa/recovery-codes | For a completed MFA enrollment view the current recovery codes
[**enroll_mfa**](CurrentIdentityApi.md#enroll_mfa) | **POST** /current-identity/mfa | Initiate MFA enrollment
[**get_current_identity**](CurrentIdentityApi.md#get_current_identity) | **GET** /current-identity | Return the current identity
[**verify_mfa**](CurrentIdentityApi.md#verify_mfa) | **POST** /current-identity/mfa/verify | Complete MFA enrollment by verifying a time based one time token


# **create_mfa_recovery_codes**
> DetailMfaRecoveryCodesEnvelope create_mfa_recovery_codes(mfa_validation)

For a completed MFA enrollment regenerate the recovery codes

Allows regeneration of recovery codes of an MFA enrollment. Requires a current valid time based one time password to interact with. Available after a completed MFA enrollment. This replaces all existing recovery codes. 

### Example

* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_management
from openziti_edge_management.api import current_identity_api
from openziti_edge_management.model.mfa_code import MfaCode
from openziti_edge_management.model.detail_mfa_recovery_codes_envelope import DetailMfaRecoveryCodesEnvelope
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

# Enter a context with an instance of the API client
with openziti_edge_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = current_identity_api.CurrentIdentityApi(api_client)
    mfa_validation = MfaCode(
        code="code_example",
    ) # MfaCode | An MFA validation request

    # example passing only required values which don't have defaults set
    try:
        # For a completed MFA enrollment regenerate the recovery codes
        api_response = api_instance.create_mfa_recovery_codes(mfa_validation)
        pprint(api_response)
    except openziti_edge_management.ApiException as e:
        print("Exception when calling CurrentIdentityApi->create_mfa_recovery_codes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mfa_validation** | [**MfaCode**](MfaCode.md)| An MFA validation request |

### Return type

[**DetailMfaRecoveryCodesEnvelope**](DetailMfaRecoveryCodesEnvelope.md)

### Authorization

[ztSession](../README.md#ztSession)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The recovery codes of an MFA enrollment |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |
**404** | The requested resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_mfa**
> Empty delete_mfa()

Disable MFA for the current identity

Disable MFA for the current identity. Requires a current valid time based one time password if MFA enrollment has been completed. If not, code should be an empty string. If one time passwords are not available and admin account can be used to remove MFA from the identity via `DELETE /identities/<id>/mfa`. 

### Example

* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_management
from openziti_edge_management.api import current_identity_api
from openziti_edge_management.model.mfa_code import MfaCode
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

# Enter a context with an instance of the API client
with openziti_edge_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = current_identity_api.CurrentIdentityApi(api_client)
    mfa_validation_code = "mfa-validation-code_example" # str |  (optional)
    mfa_validation = MfaCode(
        code="code_example",
    ) # MfaCode | An MFA validation request (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Disable MFA for the current identity
        api_response = api_instance.delete_mfa(mfa_validation_code=mfa_validation_code, mfa_validation=mfa_validation)
        pprint(api_response)
    except openziti_edge_management.ApiException as e:
        print("Exception when calling CurrentIdentityApi->delete_mfa: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mfa_validation_code** | **str**|  | [optional]
 **mfa_validation** | [**MfaCode**](MfaCode.md)| An MFA validation request | [optional]

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
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |
**404** | The requested resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detail_mfa**
> DetailMfaEnvelope detail_mfa()

Returns the current status of MFA enrollment

Returns details about the current MFA enrollment. If enrollment has not been completed it will return the current MFA configuration details necessary to complete a `POST /current-identity/mfa/verify`. 

### Example

* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_management
from openziti_edge_management.api import current_identity_api
from openziti_edge_management.model.detail_mfa_envelope import DetailMfaEnvelope
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

# Enter a context with an instance of the API client
with openziti_edge_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = current_identity_api.CurrentIdentityApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Returns the current status of MFA enrollment
        api_response = api_instance.detail_mfa()
        pprint(api_response)
    except openziti_edge_management.ApiException as e:
        print("Exception when calling CurrentIdentityApi->detail_mfa: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**DetailMfaEnvelope**](DetailMfaEnvelope.md)

### Authorization

[ztSession](../README.md#ztSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The details of an MFA enrollment |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |
**404** | The requested resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detail_mfa_qr_code**
> detail_mfa_qr_code()

Show a QR code for unverified MFA enrollments

Shows an QR code image for unverified MFA enrollments. 404s if the MFA enrollment has been completed or not started. 

### Example

* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_management
from openziti_edge_management.api import current_identity_api
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
    api_instance = current_identity_api.CurrentIdentityApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Show a QR code for unverified MFA enrollments
        api_instance.detail_mfa_qr_code()
    except openziti_edge_management.ApiException as e:
        print("Exception when calling CurrentIdentityApi->detail_mfa_qr_code: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[ztSession](../README.md#ztSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | No MFA enrollment or MFA enrollment is completed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detail_mfa_recovery_codes**
> Empty detail_mfa_recovery_codes()

For a completed MFA enrollment view the current recovery codes

Allows the viewing of recovery codes of an MFA enrollment. Requires a current valid time based one time password to interact with. Available after a completed MFA enrollment. 

### Example

* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_management
from openziti_edge_management.api import current_identity_api
from openziti_edge_management.model.mfa_code import MfaCode
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

# Enter a context with an instance of the API client
with openziti_edge_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = current_identity_api.CurrentIdentityApi(api_client)
    mfa_validation_code = "mfa-validation-code_example" # str |  (optional)
    mfa_validation = MfaCode(
        code="code_example",
    ) # MfaCode | An MFA validation request (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # For a completed MFA enrollment view the current recovery codes
        api_response = api_instance.detail_mfa_recovery_codes(mfa_validation_code=mfa_validation_code, mfa_validation=mfa_validation)
        pprint(api_response)
    except openziti_edge_management.ApiException as e:
        print("Exception when calling CurrentIdentityApi->detail_mfa_recovery_codes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mfa_validation_code** | **str**|  | [optional]
 **mfa_validation** | [**MfaCode**](MfaCode.md)| An MFA validation request | [optional]

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
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |
**404** | The requested resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enroll_mfa**
> CreateEnvelope enroll_mfa()

Initiate MFA enrollment

Allows authenticator based MFA enrollment. If enrollment has already been completed, it must be disabled before attempting to re-enroll. Subsequent enrollment request is completed via `POST /current-identity/mfa/verify` 

### Example

* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_management
from openziti_edge_management.api import current_identity_api
from openziti_edge_management.model.create_envelope import CreateEnvelope
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

# Enter a context with an instance of the API client
with openziti_edge_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = current_identity_api.CurrentIdentityApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Initiate MFA enrollment
        api_response = api_instance.enroll_mfa()
        pprint(api_response)
    except openziti_edge_management.ApiException as e:
        print("Exception when calling CurrentIdentityApi->enroll_mfa: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CreateEnvelope**](CreateEnvelope.md)

### Authorization

[ztSession](../README.md#ztSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The create request was successful and the resource has been added at the following location |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |
**409** | The identity is already enrolled in MFA |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_identity**
> CurrentIdentityDetailEnvelope get_current_identity()

Return the current identity

Returns the identity associated with the API sessions used to issue the current request

### Example

* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_management
from openziti_edge_management.api import current_identity_api
from openziti_edge_management.model.api_error_envelope import ApiErrorEnvelope
from openziti_edge_management.model.current_identity_detail_envelope import CurrentIdentityDetailEnvelope
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
    api_instance = current_identity_api.CurrentIdentityApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Return the current identity
        api_response = api_instance.get_current_identity()
        pprint(api_response)
    except openziti_edge_management.ApiException as e:
        print("Exception when calling CurrentIdentityApi->get_current_identity: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CurrentIdentityDetailEnvelope**](CurrentIdentityDetailEnvelope.md)

### Authorization

[ztSession](../README.md#ztSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, default


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The identity associated with the API Session used to issue the request |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_mfa**
> Empty verify_mfa(mfa_validation)

Complete MFA enrollment by verifying a time based one time token

Completes MFA enrollment by accepting a time based one time password as verification. Called after MFA enrollment has been initiated via `POST /current-identity/mfa`. 

### Example

* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_management
from openziti_edge_management.api import current_identity_api
from openziti_edge_management.model.mfa_code import MfaCode
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

# Enter a context with an instance of the API client
with openziti_edge_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = current_identity_api.CurrentIdentityApi(api_client)
    mfa_validation = MfaCode(
        code="code_example",
    ) # MfaCode | An MFA validation request

    # example passing only required values which don't have defaults set
    try:
        # Complete MFA enrollment by verifying a time based one time token
        api_response = api_instance.verify_mfa(mfa_validation)
        pprint(api_response)
    except openziti_edge_management.ApiException as e:
        print("Exception when calling CurrentIdentityApi->verify_mfa: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mfa_validation** | [**MfaCode**](MfaCode.md)| An MFA validation request |

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
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |
**404** | The requested resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

