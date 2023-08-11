# ListCasEnvelope


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CaDetail]**](CaDetail.md) | An array of Certificate Authority (CA) resources | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openziti_edge_management.models.list_cas_envelope import ListCasEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ListCasEnvelope from a JSON string
list_cas_envelope_instance = ListCasEnvelope.from_json(json)
# print the JSON string representation of the object
print ListCasEnvelope.to_json()

# convert the object into a dict
list_cas_envelope_dict = list_cas_envelope_instance.to_dict()
# create an instance of ListCasEnvelope from a dict
list_cas_envelope_form_dict = list_cas_envelope.from_dict(list_cas_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


