# EdgeRouterPolicyUpdate


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
from openziti_edge_management.models.edge_router_policy_update import EdgeRouterPolicyUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of EdgeRouterPolicyUpdate from a JSON string
edge_router_policy_update_instance = EdgeRouterPolicyUpdate.from_json(json)
# print the JSON string representation of the object
print EdgeRouterPolicyUpdate.to_json()

# convert the object into a dict
edge_router_policy_update_dict = edge_router_policy_update_instance.to_dict()
# create an instance of EdgeRouterPolicyUpdate from a dict
edge_router_policy_update_form_dict = edge_router_policy_update.from_dict(edge_router_policy_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


