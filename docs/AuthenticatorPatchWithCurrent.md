# AuthenticatorPatchWithCurrent

All of the fields on an authenticator that may be updated

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** |  | [optional] 
**tags** | [**Tags**](Tags.md) |  | [optional] 
**username** | **str** |  | [optional] 
**current_password** | **str** |  | 

## Example

```python
from openziti_edge_management.models.authenticator_patch_with_current import AuthenticatorPatchWithCurrent

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorPatchWithCurrent from a JSON string
authenticator_patch_with_current_instance = AuthenticatorPatchWithCurrent.from_json(json)
# print the JSON string representation of the object
print AuthenticatorPatchWithCurrent.to_json()

# convert the object into a dict
authenticator_patch_with_current_dict = authenticator_patch_with_current_instance.to_dict()
# create an instance of AuthenticatorPatchWithCurrent from a dict
authenticator_patch_with_current_form_dict = authenticator_patch_with_current.from_dict(authenticator_patch_with_current_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


