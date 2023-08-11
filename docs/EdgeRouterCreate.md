# EdgeRouterCreate

An edge router create object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_data** | [**Tags**](Tags.md) |  | [optional] 
**cost** | **int** |  | [optional] 
**disabled** | **bool** |  | [optional] 
**is_tunneler_enabled** | **bool** |  | [optional] 
**name** | **str** |  | 
**no_traversal** | **bool** |  | [optional] 
**role_attributes** | **List[str]** | A set of strings used to loosly couple this resource to policies | [optional] 
**tags** | [**Tags**](Tags.md) |  | [optional] 

## Example

```python
from openziti_edge_management.models.edge_router_create import EdgeRouterCreate

# TODO update the JSON string below
json = "{}"
# create an instance of EdgeRouterCreate from a JSON string
edge_router_create_instance = EdgeRouterCreate.from_json(json)
# print the JSON string representation of the object
print EdgeRouterCreate.to_json()

# convert the object into a dict
edge_router_create_dict = edge_router_create_instance.to_dict()
# create an instance of EdgeRouterCreate from a dict
edge_router_create_form_dict = edge_router_create.from_dict(edge_router_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


