# EdgeRouterPatch

An edge router patch object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_data** | [**Tags**](Tags.md) |  | [optional] 
**cost** | **int** |  | [optional] 
**disabled** | **bool** |  | [optional] 
**is_tunneler_enabled** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**no_traversal** | **bool** |  | [optional] 
**role_attributes** | **List[str]** | A set of strings used to loosly couple this resource to policies | [optional] 
**tags** | [**Tags**](Tags.md) |  | [optional] 

## Example

```python
from openziti_edge_management.models.edge_router_patch import EdgeRouterPatch

# TODO update the JSON string below
json = "{}"
# create an instance of EdgeRouterPatch from a JSON string
edge_router_patch_instance = EdgeRouterPatch.from_json(json)
# print the JSON string representation of the object
print EdgeRouterPatch.to_json()

# convert the object into a dict
edge_router_patch_dict = edge_router_patch_instance.to_dict()
# create an instance of EdgeRouterPatch from a dict
edge_router_patch_form_dict = edge_router_patch.from_dict(edge_router_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


