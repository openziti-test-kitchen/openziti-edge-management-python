# ExternalJwtSignerPatch


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audience** | **str** |  | [optional] 
**cert_pem** | **str** |  | [optional] 
**claims_property** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**external_auth_url** | **str** |  | [optional] 
**issuer** | **str** |  | [optional] 
**jwks_endpoint** | **str** |  | [optional] 
**kid** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**tags** | [**Tags**](Tags.md) |  | [optional] 
**use_external_id** | **bool** |  | [optional] 

## Example

```python
from openziti_edge_management.models.external_jwt_signer_patch import ExternalJwtSignerPatch

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalJwtSignerPatch from a JSON string
external_jwt_signer_patch_instance = ExternalJwtSignerPatch.from_json(json)
# print the JSON string representation of the object
print ExternalJwtSignerPatch.to_json()

# convert the object into a dict
external_jwt_signer_patch_dict = external_jwt_signer_patch_instance.to_dict()
# create an instance of ExternalJwtSignerPatch from a dict
external_jwt_signer_patch_form_dict = external_jwt_signer_patch.from_dict(external_jwt_signer_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


