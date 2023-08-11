# TraceDetailEnvelope


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TraceDetail**](TraceDetail.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openziti_edge_management.models.trace_detail_envelope import TraceDetailEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of TraceDetailEnvelope from a JSON string
trace_detail_envelope_instance = TraceDetailEnvelope.from_json(json)
# print the JSON string representation of the object
print TraceDetailEnvelope.to_json()

# convert the object into a dict
trace_detail_envelope_dict = trace_detail_envelope_instance.to_dict()
# create an instance of TraceDetailEnvelope from a dict
trace_detail_envelope_form_dict = trace_detail_envelope.from_dict(trace_detail_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


