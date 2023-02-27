# AuthenticatorCreate

Creates an authenticator for a specific identity which can be used for API authentication

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity_id** | **str** | The id of an existing identity that will be assigned this authenticator | 
**method** | **str** | The type of authenticator to create; which will dictate which properties on this object are required. | 
**cert_pem** | **str** | The client certificate the identity will login with. Used only for method&#x3D;&#39;cert&#39; | [optional] 
**password** | **str** | The password the identity will login with. Used only for method&#x3D;&#39;updb&#39; | [optional] 
**tags** | [**Tags**](Tags.md) |  | [optional] 
**username** | **str** | The username that the identity will login with. Used only for method&#x3D;&#39;updb&#39; | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


