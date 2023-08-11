# EdgeRouterPolicyPatch


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**edge_router_roles** | **List[str]** |  | [optional] 
**identity_roles** | **List[str]** |  | [optional] 
**name** | **str** |  | [optional] 
**semantic** | [**Semantic**](Semantic.md) |  | [optional] 
**tags** | [**Tags**](Tags.md) |  | [optional] 

## Example

```python
from openziti_edge_management.models.edge_router_policy_patch import EdgeRouterPolicyPatch

# TODO update the JSON string below
json = "{}"
# create an instance of EdgeRouterPolicyPatch from a JSON string
edge_router_policy_patch_instance = EdgeRouterPolicyPatch.from_json(json)
# print the JSON string representation of the object
print EdgeRouterPolicyPatch.to_json()

# convert the object into a dict
edge_router_policy_patch_dict = edge_router_policy_patch_instance.to_dict()
# create an instance of EdgeRouterPolicyPatch from a dict
edge_router_policy_patch_form_dict = edge_router_policy_patch.from_dict(edge_router_policy_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


