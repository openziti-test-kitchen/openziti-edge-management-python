# AuthPolicyDetail

A Auth Policy resource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) | A map of named links | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**tags** | [**Tags**](Tags.md) |  | [optional] 
**updated_at** | **datetime** |  | 
**name** | **str** |  | 
**primary** | [**AuthPolicyPrimary**](AuthPolicyPrimary.md) |  | 
**secondary** | [**AuthPolicySecondary**](AuthPolicySecondary.md) |  | 

## Example

```python
from openziti_edge_management.models.auth_policy_detail import AuthPolicyDetail

# TODO update the JSON string below
json = "{}"
# create an instance of AuthPolicyDetail from a JSON string
auth_policy_detail_instance = AuthPolicyDetail.from_json(json)
# print the JSON string representation of the object
print AuthPolicyDetail.to_json()

# convert the object into a dict
auth_policy_detail_dict = auth_policy_detail_instance.to_dict()
# create an instance of AuthPolicyDetail from a dict
auth_policy_detail_form_dict = auth_policy_detail.from_dict(auth_policy_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


