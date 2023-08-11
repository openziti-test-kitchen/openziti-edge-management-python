# AuthPolicyPrimaryExtJwt


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed** | **bool** |  | 
**allowed_signers** | **List[str]** |  | 

## Example

```python
from openziti_edge_management.models.auth_policy_primary_ext_jwt import AuthPolicyPrimaryExtJwt

# TODO update the JSON string below
json = "{}"
# create an instance of AuthPolicyPrimaryExtJwt from a JSON string
auth_policy_primary_ext_jwt_instance = AuthPolicyPrimaryExtJwt.from_json(json)
# print the JSON string representation of the object
print AuthPolicyPrimaryExtJwt.to_json()

# convert the object into a dict
auth_policy_primary_ext_jwt_dict = auth_policy_primary_ext_jwt_instance.to_dict()
# create an instance of AuthPolicyPrimaryExtJwt from a dict
auth_policy_primary_ext_jwt_form_dict = auth_policy_primary_ext_jwt.from_dict(auth_policy_primary_ext_jwt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


