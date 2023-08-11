# AuthPolicyPrimaryUpdbPatch


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed** | **bool** |  | [optional] 
**lockout_duration_minutes** | **int** |  | [optional] 
**max_attempts** | **int** |  | [optional] 
**min_password_length** | **int** |  | [optional] 
**require_mixed_case** | **bool** |  | [optional] 
**require_number_char** | **bool** |  | [optional] 
**require_special_char** | **bool** |  | [optional] 

## Example

```python
from openziti_edge_management.models.auth_policy_primary_updb_patch import AuthPolicyPrimaryUpdbPatch

# TODO update the JSON string below
json = "{}"
# create an instance of AuthPolicyPrimaryUpdbPatch from a JSON string
auth_policy_primary_updb_patch_instance = AuthPolicyPrimaryUpdbPatch.from_json(json)
# print the JSON string representation of the object
print AuthPolicyPrimaryUpdbPatch.to_json()

# convert the object into a dict
auth_policy_primary_updb_patch_dict = auth_policy_primary_updb_patch_instance.to_dict()
# create an instance of AuthPolicyPrimaryUpdbPatch from a dict
auth_policy_primary_updb_patch_form_dict = auth_policy_primary_updb_patch.from_dict(auth_policy_primary_updb_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


