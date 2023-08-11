# AuthPolicyPrimaryPatch


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cert** | [**AuthPolicyPrimaryCertPatch**](AuthPolicyPrimaryCertPatch.md) |  | [optional] 
**ext_jwt** | [**AuthPolicyPrimaryExtJwtPatch**](AuthPolicyPrimaryExtJwtPatch.md) |  | [optional] 
**updb** | [**AuthPolicyPrimaryUpdbPatch**](AuthPolicyPrimaryUpdbPatch.md) |  | [optional] 

## Example

```python
from openziti_edge_management.models.auth_policy_primary_patch import AuthPolicyPrimaryPatch

# TODO update the JSON string below
json = "{}"
# create an instance of AuthPolicyPrimaryPatch from a JSON string
auth_policy_primary_patch_instance = AuthPolicyPrimaryPatch.from_json(json)
# print the JSON string representation of the object
print AuthPolicyPrimaryPatch.to_json()

# convert the object into a dict
auth_policy_primary_patch_dict = auth_policy_primary_patch_instance.to_dict()
# create an instance of AuthPolicyPrimaryPatch from a dict
auth_policy_primary_patch_form_dict = auth_policy_primary_patch.from_dict(auth_policy_primary_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


