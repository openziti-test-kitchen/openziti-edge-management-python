# AuthPolicyCreate

A Auth Policy resource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**primary** | [**AuthPolicyPrimary**](AuthPolicyPrimary.md) |  | 
**secondary** | [**AuthPolicySecondary**](AuthPolicySecondary.md) |  | 
**tags** | [**Tags**](Tags.md) |  | [optional] 

## Example

```python
from openziti_edge_management.models.auth_policy_create import AuthPolicyCreate

# TODO update the JSON string below
json = "{}"
# create an instance of AuthPolicyCreate from a JSON string
auth_policy_create_instance = AuthPolicyCreate.from_json(json)
# print the JSON string representation of the object
print AuthPolicyCreate.to_json()

# convert the object into a dict
auth_policy_create_dict = auth_policy_create_instance.to_dict()
# create an instance of AuthPolicyCreate from a dict
auth_policy_create_form_dict = auth_policy_create.from_dict(auth_policy_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


