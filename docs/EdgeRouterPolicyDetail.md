# EdgeRouterPolicyDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) | A map of named links | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**tags** | [**Tags**](Tags.md) |  | [optional] 
**updated_at** | **datetime** |  | 
**edge_router_roles** | **List[str]** |  | 
**edge_router_roles_display** | [**List[NamedRole]**](NamedRole.md) |  | 
**identity_roles** | **List[str]** |  | 
**identity_roles_display** | [**List[NamedRole]**](NamedRole.md) |  | 
**is_system** | **bool** |  | 
**name** | **str** |  | 
**semantic** | [**Semantic**](Semantic.md) |  | 

## Example

```python
from openziti_edge_management.models.edge_router_policy_detail import EdgeRouterPolicyDetail

# TODO update the JSON string below
json = "{}"
# create an instance of EdgeRouterPolicyDetail from a JSON string
edge_router_policy_detail_instance = EdgeRouterPolicyDetail.from_json(json)
# print the JSON string representation of the object
print EdgeRouterPolicyDetail.to_json()

# convert the object into a dict
edge_router_policy_detail_dict = edge_router_policy_detail_instance.to_dict()
# create an instance of EdgeRouterPolicyDetail from a dict
edge_router_policy_detail_form_dict = edge_router_policy_detail.from_dict(edge_router_policy_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


