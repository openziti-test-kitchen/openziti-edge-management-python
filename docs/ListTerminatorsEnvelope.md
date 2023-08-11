# ListTerminatorsEnvelope


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TerminatorDetail]**](TerminatorDetail.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openziti_edge_management.models.list_terminators_envelope import ListTerminatorsEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ListTerminatorsEnvelope from a JSON string
list_terminators_envelope_instance = ListTerminatorsEnvelope.from_json(json)
# print the JSON string representation of the object
print ListTerminatorsEnvelope.to_json()

# convert the object into a dict
list_terminators_envelope_dict = list_terminators_envelope_instance.to_dict()
# create an instance of ListTerminatorsEnvelope from a dict
list_terminators_envelope_form_dict = list_terminators_envelope.from_dict(list_terminators_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


