# DetailedEdgeRouterEnvelope


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**EdgeRouterDetail**](EdgeRouterDetail.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openziti_edge_management.models.detailed_edge_router_envelope import DetailedEdgeRouterEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of DetailedEdgeRouterEnvelope from a JSON string
detailed_edge_router_envelope_instance = DetailedEdgeRouterEnvelope.from_json(json)
# print the JSON string representation of the object
print DetailedEdgeRouterEnvelope.to_json()

# convert the object into a dict
detailed_edge_router_envelope_dict = detailed_edge_router_envelope_instance.to_dict()
# create an instance of DetailedEdgeRouterEnvelope from a dict
detailed_edge_router_envelope_form_dict = detailed_edge_router_envelope.from_dict(detailed_edge_router_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


