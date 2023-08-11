# ExternalJwtSignerUpdate


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
from openziti_edge_management.models.external_jwt_signer_update import ExternalJwtSignerUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalJwtSignerUpdate from a JSON string
external_jwt_signer_update_instance = ExternalJwtSignerUpdate.from_json(json)
# print the JSON string representation of the object
print ExternalJwtSignerUpdate.to_json()

# convert the object into a dict
external_jwt_signer_update_dict = external_jwt_signer_update_instance.to_dict()
# create an instance of ExternalJwtSignerUpdate from a dict
external_jwt_signer_update_form_dict = external_jwt_signer_update.from_dict(external_jwt_signer_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


