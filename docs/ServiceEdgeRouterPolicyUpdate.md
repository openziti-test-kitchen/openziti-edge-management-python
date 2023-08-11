# ServiceEdgeRouterPolicyUpdate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**edge_router_roles** | **List[str]** |  | [optional] 
**name** | **str** |  | 
**semantic** | [**Semantic**](Semantic.md) |  | 
**service_roles** | **List[str]** |  | [optional] 
**tags** | [**Tags**](Tags.md) |  | [optional] 

## Example

```python
from openziti_edge_management.models.service_edge_router_policy_update import ServiceEdgeRouterPolicyUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceEdgeRouterPolicyUpdate from a JSON string
service_edge_router_policy_update_instance = ServiceEdgeRouterPolicyUpdate.from_json(json)
# print the JSON string representation of the object
print ServiceEdgeRouterPolicyUpdate.to_json()

# convert the object into a dict
service_edge_router_policy_update_dict = service_edge_router_policy_update_instance.to_dict()
# create an instance of ServiceEdgeRouterPolicyUpdate from a dict
service_edge_router_policy_update_form_dict = service_edge_router_policy_update.from_dict(service_edge_router_policy_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


