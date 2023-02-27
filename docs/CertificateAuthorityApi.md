# openziti_edge_management.CertificateAuthorityApi

All URIs are relative to *https://demo.ziti.dev/edge/management/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ca**](CertificateAuthorityApi.md#create_ca) | **POST** /cas | Creates a CA
[**delete_ca**](CertificateAuthorityApi.md#delete_ca) | **DELETE** /cas/{id} | Delete a CA
[**detail_ca**](CertificateAuthorityApi.md#detail_ca) | **GET** /cas/{id} | Retrieves a single CA
[**get_ca_jwt**](CertificateAuthorityApi.md#get_ca_jwt) | **GET** /cas/{id}/jwt | Retrieve the enrollment JWT for a CA
[**list_cas**](CertificateAuthorityApi.md#list_cas) | **GET** /cas | List CAs
[**patch_ca**](CertificateAuthorityApi.md#patch_ca) | **PATCH** /cas/{id} | Update the supplied fields on a CA
[**update_ca**](CertificateAuthorityApi.md#update_ca) | **PUT** /cas/{id} | Update all fields on a CA
[**verify_ca**](CertificateAuthorityApi.md#verify_ca) | **POST** /cas/{id}/verify | Verify a CA


# **create_ca**
> CreateEnvelope create_ca(ca)

Creates a CA

Creates a CA in an unverified state. Requires admin access.

### Example

* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_management
from openziti_edge_management.api import certificate_authority_api
from openziti_edge_management.model.create_envelope import CreateEnvelope
from openziti_edge_management.model.api_error_envelope import ApiErrorEnvelope
from openziti_edge_management.model.ca_create import CaCreate
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
    api_instance = certificate_authority_api.CertificateAuthorityApi(api_client)
    ca = CaCreate(
        cert_pem='''-----BEGIN CERTIFICATE-----
MIICUjCCAdmgAwIBAgIJANooo7NB+dZZMAoGCCqGSM49BAMCMF4xCzAJBgNVBAYT
AlVTMQswCQYDVQQIDAJOQzETMBEGA1UECgwKTmV0Rm91bmRyeTEtMCsGA1UEAwwk
TmV0Rm91bmRyeSBaaXRpIEV4dGVybmFsIEFQSSBSb290IENBMB4XDTE4MTExNTEy
NTcwOVoXDTM4MTExMDEyNTcwOVowXjELMAkGA1UEBhMCVVMxCzAJBgNVBAgMAk5D
MRMwEQYDVQQKDApOZXRGb3VuZHJ5MS0wKwYDVQQDDCROZXRGb3VuZHJ5IFppdGkg
RXh0ZXJuYWwgQVBJIFJvb3QgQ0EwdjAQBgcqhkjOPQIBBgUrgQQAIgNiAARwq61Z
Iaqbaw0PDt3frJZaHjkxfZhwYrykI1GlbRNd/jix03lVG9qvpN5Og9fQfFFcFmD/
3vCE9S6O0npm0mADQxcBcxbMRAH5dtBuCuiJW6qAAbPgiM32vqSxBiFt0KejYzBh
MB0GA1UdDgQWBBRx1OVGuc/jdltDc8YBtkw8Tbr4fjAfBgNVHSMEGDAWgBRx1OVG
uc/jdltDc8YBtkw8Tbr4fjAPBgNVHRMBAf8EBTADAQH/MA4GA1UdDwEB/wQEAwIB
hjAKBggqhkjOPQQDAgNnADBkAjBDRxNZUaIVpkQKnAgJukl3ysd3/i7Z6hDyIEms
kllz/+ZvmdBp9iedV5o5BvJUggACMCv+UBFlJH7pmsOCo/F45Kk178YsCC7gaMxE
1ZG1zveyMvsYsH04C9FndE6w2MLvlA==
-----END CERTIFICATE-----
''',
        external_id_claim=ExternalIdClaim(
            index=1,
            location="COMMON_NAME",
            matcher="ALL",
            matcher_criteria="matcher_criteria_example",
            parser="NONE",
            parser_criteria="parser_criteria_example",
        ),
        identity_name_format="identity_name_format_example",
        identity_roles=Roles([
            "identity_roles_example",
        ]),
        is_auth_enabled=True,
        is_auto_ca_enrollment_enabled=True,
        is_ott_ca_enrollment_enabled=True,
        name="Test 3rd Party External CA",
        tags=Tags(None),
    ) # CaCreate | A CA to create

    # example passing only required values which don't have defaults set
    try:
        # Creates a CA
        api_response = api_instance.create_ca(ca)
        pprint(api_response)
    except openziti_edge_management.ApiException as e:
        print("Exception when calling CertificateAuthorityApi->create_ca: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ca** | [**CaCreate**](CaCreate.md)| A CA to create |

### Return type

[**CreateEnvelope**](CreateEnvelope.md)

### Authorization

[ztSession](../README.md#ztSession)

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

# **delete_ca**
> Empty delete_ca(id)

Delete a CA

Delete a CA by id. Deleting a CA will delete its associated certificate authenticators. This can make it impossible for identities to authenticate if they no longer have any valid authenticators. Requires admin access. 

### Example

* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_management
from openziti_edge_management.api import certificate_authority_api
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
    api_instance = certificate_authority_api.CertificateAuthorityApi(api_client)
    id = "id_example" # str | The id of the requested resource

    # example passing only required values which don't have defaults set
    try:
        # Delete a CA
        api_response = api_instance.delete_ca(id)
        pprint(api_response)
    except openziti_edge_management.ApiException as e:
        print("Exception when calling CertificateAuthorityApi->delete_ca: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource |

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
**200** | The delete request was successful and the resource has been removed |  -  |
**400** | The supplied request contains invalid fields or could not be parsed (json and non-json bodies). The error&#39;s code, message, and cause fields can be inspected for further information |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detail_ca**
> DetailCaEnvelope detail_ca(id)

Retrieves a single CA

Retrieves a single CA by id. Requires admin access.

### Example

* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_management
from openziti_edge_management.api import certificate_authority_api
from openziti_edge_management.model.detail_ca_envelope import DetailCaEnvelope
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
    api_instance = certificate_authority_api.CertificateAuthorityApi(api_client)
    id = "id_example" # str | The id of the requested resource

    # example passing only required values which don't have defaults set
    try:
        # Retrieves a single CA
        api_response = api_instance.detail_ca(id)
        pprint(api_response)
    except openziti_edge_management.ApiException as e:
        print("Exception when calling CertificateAuthorityApi->detail_ca: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource |

### Return type

[**DetailCaEnvelope**](DetailCaEnvelope.md)

### Authorization

[ztSession](../README.md#ztSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A singular Certificate Authority (CA) resource |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |
**404** | The requested resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ca_jwt**
> str get_ca_jwt(id)

Retrieve the enrollment JWT for a CA

For CA auto enrollment, the enrollment JWT is static and provided on each CA resource. This endpoint provides the jwt as a text response. 

### Example

* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_management
from openziti_edge_management.api import certificate_authority_api
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
    api_instance = certificate_authority_api.CertificateAuthorityApi(api_client)
    id = "id_example" # str | The id of the requested resource

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the enrollment JWT for a CA
        api_response = api_instance.get_ca_jwt(id)
        pprint(api_response)
    except openziti_edge_management.ApiException as e:
        print("Exception when calling CertificateAuthorityApi->get_ca_jwt: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource |

### Return type

**str**

### Authorization

[ztSession](../README.md#ztSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/jwt, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The result is the JWT text to validate the CA |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |
**404** | The requested resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cas**
> ListCasEnvelope list_cas()

List CAs

Retrieves a list of CA resources; supports filtering, sorting, and pagination. Requires admin access.

### Example

* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_management
from openziti_edge_management.api import certificate_authority_api
from openziti_edge_management.model.list_cas_envelope import ListCasEnvelope
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
    api_instance = certificate_authority_api.CertificateAuthorityApi(api_client)
    limit = 1 # int |  (optional)
    offset = 1 # int |  (optional)
    filter = "filter_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List CAs
        api_response = api_instance.list_cas(limit=limit, offset=offset, filter=filter)
        pprint(api_response)
    except openziti_edge_management.ApiException as e:
        print("Exception when calling CertificateAuthorityApi->list_cas: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional]
 **offset** | **int**|  | [optional]
 **filter** | **str**|  | [optional]

### Return type

[**ListCasEnvelope**](ListCasEnvelope.md)

### Authorization

[ztSession](../README.md#ztSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of Certificate Authorities (CAs) |  -  |
**400** | The supplied request contains invalid fields or could not be parsed (json and non-json bodies). The error&#39;s code, message, and cause fields can be inspected for further information |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_ca**
> Empty patch_ca(id, ca)

Update the supplied fields on a CA

Update only the supplied fields on a CA by id. Requires admin access.

### Example

* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_management
from openziti_edge_management.api import certificate_authority_api
from openziti_edge_management.model.ca_patch import CaPatch
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
    api_instance = certificate_authority_api.CertificateAuthorityApi(api_client)
    id = "id_example" # str | The id of the requested resource
    ca = CaPatch(
        external_id_claim=ExternalIdClaimPatch(
            index=1,
            location="COMMON_NAME",
            matcher="ALL",
            matcher_criteria="matcher_criteria_example",
            parser="NONE",
            parser_criteria="parser_criteria_example",
        ),
        identity_name_format="identity_name_format_example",
        identity_roles=Roles([
            "identity_roles_example",
        ]),
        is_auth_enabled=True,
        is_auto_ca_enrollment_enabled=True,
        is_ott_ca_enrollment_enabled=True,
        name="My CA",
        tags=Tags(None),
    ) # CaPatch | A CA patch object

    # example passing only required values which don't have defaults set
    try:
        # Update the supplied fields on a CA
        api_response = api_instance.patch_ca(id, ca)
        pprint(api_response)
    except openziti_edge_management.ApiException as e:
        print("Exception when calling CertificateAuthorityApi->patch_ca: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource |
 **ca** | [**CaPatch**](CaPatch.md)| A CA patch object |

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
**200** | The patch request was successful and the resource has been altered |  -  |
**400** | The supplied request contains invalid fields or could not be parsed (json and non-json bodies). The error&#39;s code, message, and cause fields can be inspected for further information |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |
**404** | The requested resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ca**
> Empty update_ca(id, ca)

Update all fields on a CA

Update all fields on a CA by id. Requires admin access.

### Example

* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_management
from openziti_edge_management.api import certificate_authority_api
from openziti_edge_management.model.ca_update import CaUpdate
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
    api_instance = certificate_authority_api.CertificateAuthorityApi(api_client)
    id = "id_example" # str | The id of the requested resource
    ca = CaUpdate(
        external_id_claim=ExternalIdClaim(
            index=1,
            location="COMMON_NAME",
            matcher="ALL",
            matcher_criteria="matcher_criteria_example",
            parser="NONE",
            parser_criteria="parser_criteria_example",
        ),
        identity_name_format="identity_name_format_example",
        identity_roles=Roles([
            "identity_roles_example",
        ]),
        is_auth_enabled=True,
        is_auto_ca_enrollment_enabled=True,
        is_ott_ca_enrollment_enabled=True,
        name="My CA",
        tags=Tags(None),
    ) # CaUpdate | A CA update object

    # example passing only required values which don't have defaults set
    try:
        # Update all fields on a CA
        api_response = api_instance.update_ca(id, ca)
        pprint(api_response)
    except openziti_edge_management.ApiException as e:
        print("Exception when calling CertificateAuthorityApi->update_ca: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource |
 **ca** | [**CaUpdate**](CaUpdate.md)| A CA update object |

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
**200** | The update request was successful and the resource has been altered |  -  |
**400** | The supplied request contains invalid fields or could not be parsed (json and non-json bodies). The error&#39;s code, message, and cause fields can be inspected for further information |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |
**404** | The requested resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_ca**
> Empty verify_ca(id, certificate)

Verify a CA

Allows a CA to become verified by submitting a certificate in PEM format that has been signed by the target CA. The common name on the certificate must match the verificationToken property of the CA. Unverfieid CAs can not be used for enrollment/authentication. Requires admin access. 

### Example

* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_management
from openziti_edge_management.api import certificate_authority_api
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
    api_instance = certificate_authority_api.CertificateAuthorityApi(api_client)
    id = "id_example" # str | The id of the requested resource
    certificate = "certificate_example" # str | A PEM formatted certificate signed by the target CA with the common name matching the CA's validationToken

    # example passing only required values which don't have defaults set
    try:
        # Verify a CA
        api_response = api_instance.verify_ca(id, certificate)
        pprint(api_response)
    except openziti_edge_management.ApiException as e:
        print("Exception when calling CertificateAuthorityApi->verify_ca: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource |
 **certificate** | **str**| A PEM formatted certificate signed by the target CA with the common name matching the CA&#39;s validationToken |

### Return type

[**Empty**](Empty.md)

### Authorization

[ztSession](../README.md#ztSession)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Base empty response |  -  |
**400** | The supplied request contains invalid fields or could not be parsed (json and non-json bodies). The error&#39;s code, message, and cause fields can be inspected for further information |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |
**404** | The requested resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

