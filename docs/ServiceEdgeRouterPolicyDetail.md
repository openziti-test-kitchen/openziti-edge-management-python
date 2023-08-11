# ServiceEdgeRouterPolicyDetail


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
**name** | **str** |  | 
**semantic** | [**Semantic**](Semantic.md) |  | 
**service_roles** | **List[str]** |  | 
**service_roles_display** | [**List[NamedRole]**](NamedRole.md) |  | 

## Example

```python
from openziti_edge_management.models.service_edge_router_policy_detail import ServiceEdgeRouterPolicyDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceEdgeRouterPolicyDetail from a JSON string
service_edge_router_policy_detail_instance = ServiceEdgeRouterPolicyDetail.from_json(json)
# print the JSON string representation of the object
print ServiceEdgeRouterPolicyDetail.to_json()

# convert the object into a dict
service_edge_router_policy_detail_dict = service_edge_router_policy_detail_instance.to_dict()
# create an instance of ServiceEdgeRouterPolicyDetail from a dict
service_edge_router_policy_detail_form_dict = service_edge_router_policy_detail.from_dict(service_edge_router_policy_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


