# ListConfigsEnvelope


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ConfigDetail]**](ConfigDetail.md) | An array of config resources | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openziti_edge_management.models.list_configs_envelope import ListConfigsEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ListConfigsEnvelope from a JSON string
list_configs_envelope_instance = ListConfigsEnvelope.from_json(json)
# print the JSON string representation of the object
print ListConfigsEnvelope.to_json()

# convert the object into a dict
list_configs_envelope_dict = list_configs_envelope_instance.to_dict()
# create an instance of ListConfigsEnvelope from a dict
list_configs_envelope_form_dict = list_configs_envelope.from_dict(list_configs_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


