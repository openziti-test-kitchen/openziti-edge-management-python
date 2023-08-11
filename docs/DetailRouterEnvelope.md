# DetailRouterEnvelope


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**RouterDetail**](RouterDetail.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openziti_edge_management.models.detail_router_envelope import DetailRouterEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of DetailRouterEnvelope from a JSON string
detail_router_envelope_instance = DetailRouterEnvelope.from_json(json)
# print the JSON string representation of the object
print DetailRouterEnvelope.to_json()

# convert the object into a dict
detail_router_envelope_dict = detail_router_envelope_instance.to_dict()
# create an instance of DetailRouterEnvelope from a dict
detail_router_envelope_form_dict = detail_router_envelope.from_dict(detail_router_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


