# DetailSessionRoutePathEnvelope


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SessionRoutePathDetail**](SessionRoutePathDetail.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openziti_edge_management.models.detail_session_route_path_envelope import DetailSessionRoutePathEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of DetailSessionRoutePathEnvelope from a JSON string
detail_session_route_path_envelope_instance = DetailSessionRoutePathEnvelope.from_json(json)
# print the JSON string representation of the object
print DetailSessionRoutePathEnvelope.to_json()

# convert the object into a dict
detail_session_route_path_envelope_dict = detail_session_route_path_envelope_instance.to_dict()
# create an instance of DetailSessionRoutePathEnvelope from a dict
detail_session_route_path_envelope_form_dict = detail_session_route_path_envelope.from_dict(detail_session_route_path_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


