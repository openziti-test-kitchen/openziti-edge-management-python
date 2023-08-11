# DetailCaEnvelope


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CaDetail**](CaDetail.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openziti_edge_management.models.detail_ca_envelope import DetailCaEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of DetailCaEnvelope from a JSON string
detail_ca_envelope_instance = DetailCaEnvelope.from_json(json)
# print the JSON string representation of the object
print DetailCaEnvelope.to_json()

# convert the object into a dict
detail_ca_envelope_dict = detail_ca_envelope_instance.to_dict()
# create an instance of DetailCaEnvelope from a dict
detail_ca_envelope_form_dict = detail_ca_envelope.from_dict(detail_ca_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


