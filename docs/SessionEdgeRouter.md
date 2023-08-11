# SessionEdgeRouter


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
**urls** | **Dict[str, str]** |  | 

## Example

```python
from openziti_edge_management.models.session_edge_router import SessionEdgeRouter

# TODO update the JSON string below
json = "{}"
# create an instance of SessionEdgeRouter from a JSON string
session_edge_router_instance = SessionEdgeRouter.from_json(json)
# print the JSON string representation of the object
print SessionEdgeRouter.to_json()

# convert the object into a dict
session_edge_router_dict = session_edge_router_instance.to_dict()
# create an instance of SessionEdgeRouter from a dict
session_edge_router_form_dict = session_edge_router.from_dict(session_edge_router_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


