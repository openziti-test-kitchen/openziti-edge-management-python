# CommonEdgeRouterProperties


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_data** | [**Tags**](Tags.md) |  | [optional] 
**cost** | **int** |  | 
**disabled** | **bool** |  | 
**hostname** | **str** |  | 
**is_online** | **bool** |  | 
**name** | **str** |  | 
**no_traversal** | **bool** |  | 
**supported_protocols** | **Dict[str, str]** |  | 
**sync_status** | **str** |  | 

## Example

```python
from openziti_edge_management.models.common_edge_router_properties import CommonEdgeRouterProperties

# TODO update the JSON string below
json = "{}"
# create an instance of CommonEdgeRouterProperties from a JSON string
common_edge_router_properties_instance = CommonEdgeRouterProperties.from_json(json)
# print the JSON string representation of the object
print CommonEdgeRouterProperties.to_json()

# convert the object into a dict
common_edge_router_properties_dict = common_edge_router_properties_instance.to_dict()
# create an instance of CommonEdgeRouterProperties from a dict
common_edge_router_properties_form_dict = common_edge_router_properties.from_dict(common_edge_router_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


