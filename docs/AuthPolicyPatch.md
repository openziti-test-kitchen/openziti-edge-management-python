# AuthPolicyPatch

A Auth Policy resource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**primary** | [**AuthPolicyPrimaryPatch**](AuthPolicyPrimaryPatch.md) |  | [optional] 
**secondary** | [**AuthPolicySecondaryPatch**](AuthPolicySecondaryPatch.md) |  | [optional] 
**tags** | [**Tags**](Tags.md) |  | [optional] 

## Example

```python
from openziti_edge_management.models.auth_policy_patch import AuthPolicyPatch

# TODO update the JSON string below
json = "{}"
# create an instance of AuthPolicyPatch from a JSON string
auth_policy_patch_instance = AuthPolicyPatch.from_json(json)
# print the JSON string representation of the object
print AuthPolicyPatch.to_json()

# convert the object into a dict
auth_policy_patch_dict = auth_policy_patch_instance.to_dict()
# create an instance of AuthPolicyPatch from a dict
auth_policy_patch_form_dict = auth_policy_patch.from_dict(auth_policy_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


