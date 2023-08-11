# DetailConfigEnvelope


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ConfigDetail**](ConfigDetail.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openziti_edge_management.models.detail_config_envelope import DetailConfigEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of DetailConfigEnvelope from a JSON string
detail_config_envelope_instance = DetailConfigEnvelope.from_json(json)
# print the JSON string representation of the object
print DetailConfigEnvelope.to_json()

# convert the object into a dict
detail_config_envelope_dict = detail_config_envelope_instance.to_dict()
# create an instance of DetailConfigEnvelope from a dict
detail_config_envelope_form_dict = detail_config_envelope.from_dict(detail_config_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


