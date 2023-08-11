# AuthenticatorCreate

Creates an authenticator for a specific identity which can be used for API authentication

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cert_pem** | **str** | The client certificate the identity will login with. Used only for method&#x3D;&#39;cert&#39; | [optional] 
**identity_id** | **str** | The id of an existing identity that will be assigned this authenticator | 
**method** | **str** | The type of authenticator to create; which will dictate which properties on this object are required. | 
**password** | **str** | The password the identity will login with. Used only for method&#x3D;&#39;updb&#39; | [optional] 
**tags** | [**Tags**](Tags.md) |  | [optional] 
**username** | **str** | The username that the identity will login with. Used only for method&#x3D;&#39;updb&#39; | [optional] 

## Example

```python
from openziti_edge_management.models.authenticator_create import AuthenticatorCreate

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorCreate from a JSON string
authenticator_create_instance = AuthenticatorCreate.from_json(json)
# print the JSON string representation of the object
print AuthenticatorCreate.to_json()

# convert the object into a dict
authenticator_create_dict = authenticator_create_instance.to_dict()
# create an instance of AuthenticatorCreate from a dict
authenticator_create_form_dict = authenticator_create.from_dict(authenticator_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


