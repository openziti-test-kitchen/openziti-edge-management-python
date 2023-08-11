# DetailSpecEnvelope


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SpecDetail**](SpecDetail.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openziti_edge_management.models.detail_spec_envelope import DetailSpecEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of DetailSpecEnvelope from a JSON string
detail_spec_envelope_instance = DetailSpecEnvelope.from_json(json)
# print the JSON string representation of the object
print DetailSpecEnvelope.to_json()

# convert the object into a dict
detail_spec_envelope_dict = detail_spec_envelope_instance.to_dict()
# create an instance of DetailSpecEnvelope from a dict
detail_spec_envelope_form_dict = detail_spec_envelope.from_dict(detail_spec_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


