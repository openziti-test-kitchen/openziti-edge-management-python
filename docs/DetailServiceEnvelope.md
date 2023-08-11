# DetailServiceEnvelope


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ServiceDetail**](ServiceDetail.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openziti_edge_management.models.detail_service_envelope import DetailServiceEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of DetailServiceEnvelope from a JSON string
detail_service_envelope_instance = DetailServiceEnvelope.from_json(json)
# print the JSON string representation of the object
print DetailServiceEnvelope.to_json()

# convert the object into a dict
detail_service_envelope_dict = detail_service_envelope_instance.to_dict()
# create an instance of DetailServiceEnvelope from a dict
detail_service_envelope_form_dict = detail_service_envelope.from_dict(detail_service_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


