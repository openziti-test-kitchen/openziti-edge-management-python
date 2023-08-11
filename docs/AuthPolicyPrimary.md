# AuthPolicyPrimary


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cert** | [**AuthPolicyPrimaryCert**](AuthPolicyPrimaryCert.md) |  | 
**ext_jwt** | [**AuthPolicyPrimaryExtJwt**](AuthPolicyPrimaryExtJwt.md) |  | 
**updb** | [**AuthPolicyPrimaryUpdb**](AuthPolicyPrimaryUpdb.md) |  | 

## Example

```python
from openziti_edge_management.models.auth_policy_primary import AuthPolicyPrimary

# TODO update the JSON string below
json = "{}"
# create an instance of AuthPolicyPrimary from a JSON string
auth_policy_primary_instance = AuthPolicyPrimary.from_json(json)
# print the JSON string representation of the object
print AuthPolicyPrimary.to_json()

# convert the object into a dict
auth_policy_primary_dict = auth_policy_primary_instance.to_dict()
# create an instance of AuthPolicyPrimary from a dict
auth_policy_primary_form_dict = auth_policy_primary.from_dict(auth_policy_primary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


