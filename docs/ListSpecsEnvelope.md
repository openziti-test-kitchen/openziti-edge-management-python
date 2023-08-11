# ListSpecsEnvelope


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SpecDetail]**](SpecDetail.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openziti_edge_management.models.list_specs_envelope import ListSpecsEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ListSpecsEnvelope from a JSON string
list_specs_envelope_instance = ListSpecsEnvelope.from_json(json)
# print the JSON string representation of the object
print ListSpecsEnvelope.to_json()

# convert the object into a dict
list_specs_envelope_dict = list_specs_envelope_instance.to_dict()
# create an instance of ListSpecsEnvelope from a dict
list_specs_envelope_form_dict = list_specs_envelope.from_dict(list_specs_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


