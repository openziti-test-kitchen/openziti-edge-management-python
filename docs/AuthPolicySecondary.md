# AuthPolicySecondary


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**require_ext_jwt_signer** | **str** |  | [optional] 
**require_totp** | **bool** |  | 

## Example

```python
from openziti_edge_management.models.auth_policy_secondary import AuthPolicySecondary

# TODO update the JSON string below
json = "{}"
# create an instance of AuthPolicySecondary from a JSON string
auth_policy_secondary_instance = AuthPolicySecondary.from_json(json)
# print the JSON string representation of the object
print AuthPolicySecondary.to_json()

# convert the object into a dict
auth_policy_secondary_dict = auth_policy_secondary_instance.to_dict()
# create an instance of AuthPolicySecondary from a dict
auth_policy_secondary_form_dict = auth_policy_secondary.from_dict(auth_policy_secondary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


