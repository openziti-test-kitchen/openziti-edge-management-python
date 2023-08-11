# DetailSpecBodyEnvelope


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openziti_edge_management.models.detail_spec_body_envelope import DetailSpecBodyEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of DetailSpecBodyEnvelope from a JSON string
detail_spec_body_envelope_instance = DetailSpecBodyEnvelope.from_json(json)
# print the JSON string representation of the object
print DetailSpecBodyEnvelope.to_json()

# convert the object into a dict
detail_spec_body_envelope_dict = detail_spec_body_envelope_instance.to_dict()
# create an instance of DetailSpecBodyEnvelope from a dict
detail_spec_body_envelope_form_dict = detail_spec_body_envelope.from_dict(detail_spec_body_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


