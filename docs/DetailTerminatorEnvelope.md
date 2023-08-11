# DetailTerminatorEnvelope


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TerminatorDetail**](TerminatorDetail.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openziti_edge_management.models.detail_terminator_envelope import DetailTerminatorEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of DetailTerminatorEnvelope from a JSON string
detail_terminator_envelope_instance = DetailTerminatorEnvelope.from_json(json)
# print the JSON string representation of the object
print DetailTerminatorEnvelope.to_json()

# convert the object into a dict
detail_terminator_envelope_dict = detail_terminator_envelope_instance.to_dict()
# create an instance of DetailTerminatorEnvelope from a dict
detail_terminator_envelope_form_dict = detail_terminator_envelope.from_dict(detail_terminator_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


