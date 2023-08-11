# AuthenticatorPatch

All of the fields on an authenticator that may be updated

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** |  | [optional] 
**tags** | [**Tags**](Tags.md) |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from openziti_edge_management.models.authenticator_patch import AuthenticatorPatch

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorPatch from a JSON string
authenticator_patch_instance = AuthenticatorPatch.from_json(json)
# print the JSON string representation of the object
print AuthenticatorPatch.to_json()

# convert the object into a dict
authenticator_patch_dict = authenticator_patch_instance.to_dict()
# create an instance of AuthenticatorPatch from a dict
authenticator_patch_form_dict = authenticator_patch.from_dict(authenticator_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


