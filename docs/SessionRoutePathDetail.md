# SessionRoutePathDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**route_path** | **List[str]** |  | [optional] 

## Example

```python
from openziti_edge_management.models.session_route_path_detail import SessionRoutePathDetail

# TODO update the JSON string below
json = "{}"
# create an instance of SessionRoutePathDetail from a JSON string
session_route_path_detail_instance = SessionRoutePathDetail.from_json(json)
# print the JSON string representation of the object
print SessionRoutePathDetail.to_json()

# convert the object into a dict
session_route_path_detail_dict = session_route_path_detail_instance.to_dict()
# create an instance of SessionRoutePathDetail from a dict
session_route_path_detail_form_dict = session_route_path_detail.from_dict(session_route_path_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


