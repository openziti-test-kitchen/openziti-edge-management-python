# ExternalJwtSignerCreate

A create Certificate Authority (CA) object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audience** | **str** |  | 
**cert_pem** | **str** |  | [optional] 
**claims_property** | **str** |  | [optional] 
**enabled** | **bool** |  | 
**external_auth_url** | **str** |  | [optional] 
**issuer** | **str** |  | 
**jwks_endpoint** | **str** |  | [optional] 
**kid** | **str** |  | [optional] 
**name** | **str** |  | 
**tags** | [**Tags**](Tags.md) |  | [optional] 
**use_external_id** | **bool** |  | [optional] 

## Example

```python
from openziti_edge_management.models.external_jwt_signer_create import ExternalJwtSignerCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalJwtSignerCreate from a JSON string
external_jwt_signer_create_instance = ExternalJwtSignerCreate.from_json(json)
# print the JSON string representation of the object
print ExternalJwtSignerCreate.to_json()

# convert the object into a dict
external_jwt_signer_create_dict = external_jwt_signer_create_instance.to_dict()
# create an instance of ExternalJwtSignerCreate from a dict
external_jwt_signer_create_form_dict = external_jwt_signer_create.from_dict(external_jwt_signer_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


