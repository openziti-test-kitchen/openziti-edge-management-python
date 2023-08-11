# PostureCheckMfaPropertiesPatch


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ignore_legacy_endpoints** | **bool** |  | [optional] 
**prompt_on_unlock** | **bool** |  | [optional] 
**prompt_on_wake** | **bool** |  | [optional] 
**timeout_seconds** | **int** |  | [optional] 

## Example

```python
from openziti_edge_management.models.posture_check_mfa_properties_patch import PostureCheckMfaPropertiesPatch

# TODO update the JSON string below
json = "{}"
# create an instance of PostureCheckMfaPropertiesPatch from a JSON string
posture_check_mfa_properties_patch_instance = PostureCheckMfaPropertiesPatch.from_json(json)
# print the JSON string representation of the object
print PostureCheckMfaPropertiesPatch.to_json()

# convert the object into a dict
posture_check_mfa_properties_patch_dict = posture_check_mfa_properties_patch_instance.to_dict()
# create an instance of PostureCheckMfaPropertiesPatch from a dict
posture_check_mfa_properties_patch_form_dict = posture_check_mfa_properties_patch.from_dict(posture_check_mfa_properties_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


