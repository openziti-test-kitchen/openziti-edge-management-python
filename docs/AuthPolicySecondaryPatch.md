# AuthPolicySecondaryPatch


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**require_ext_jwt_signer** | **str** |  | [optional] 
**require_totp** | **bool** |  | [optional] 

## Example

```python
from openziti_edge_management.models.auth_policy_secondary_patch import AuthPolicySecondaryPatch

# TODO update the JSON string below
json = "{}"
# create an instance of AuthPolicySecondaryPatch from a JSON string
auth_policy_secondary_patch_instance = AuthPolicySecondaryPatch.from_json(json)
# print the JSON string representation of the object
print AuthPolicySecondaryPatch.to_json()

# convert the object into a dict
auth_policy_secondary_patch_dict = auth_policy_secondary_patch_instance.to_dict()
# create an instance of AuthPolicySecondaryPatch from a dict
auth_policy_secondary_patch_form_dict = auth_policy_secondary_patch.from_dict(auth_policy_secondary_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


