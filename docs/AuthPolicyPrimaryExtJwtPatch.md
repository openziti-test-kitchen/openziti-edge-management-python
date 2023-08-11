# AuthPolicyPrimaryExtJwtPatch


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed** | **bool** |  | [optional] 
**allowed_signers** | **List[str]** |  | [optional] 

## Example

```python
from openziti_edge_management.models.auth_policy_primary_ext_jwt_patch import AuthPolicyPrimaryExtJwtPatch

# TODO update the JSON string below
json = "{}"
# create an instance of AuthPolicyPrimaryExtJwtPatch from a JSON string
auth_policy_primary_ext_jwt_patch_instance = AuthPolicyPrimaryExtJwtPatch.from_json(json)
# print the JSON string representation of the object
print AuthPolicyPrimaryExtJwtPatch.to_json()

# convert the object into a dict
auth_policy_primary_ext_jwt_patch_dict = auth_policy_primary_ext_jwt_patch_instance.to_dict()
# create an instance of AuthPolicyPrimaryExtJwtPatch from a dict
auth_policy_primary_ext_jwt_patch_form_dict = auth_policy_primary_ext_jwt_patch.from_dict(auth_policy_primary_ext_jwt_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


