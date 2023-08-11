# EdgeRouterPolicyCreate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**edge_router_roles** | **List[str]** |  | [optional] 
**identity_roles** | **List[str]** |  | [optional] 
**name** | **str** |  | 
**semantic** | [**Semantic**](Semantic.md) |  | 
**tags** | [**Tags**](Tags.md) |  | [optional] 

## Example

```python
from openziti_edge_management.models.edge_router_policy_create import EdgeRouterPolicyCreate

# TODO update the JSON string below
json = "{}"
# create an instance of EdgeRouterPolicyCreate from a JSON string
edge_router_policy_create_instance = EdgeRouterPolicyCreate.from_json(json)
# print the JSON string representation of the object
print EdgeRouterPolicyCreate.to_json()

# convert the object into a dict
edge_router_policy_create_dict = edge_router_policy_create_instance.to_dict()
# create an instance of EdgeRouterPolicyCreate from a dict
edge_router_policy_create_form_dict = edge_router_policy_create.from_dict(edge_router_policy_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


