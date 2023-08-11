# ListConfigTypesEnvelope


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ConfigTypeDetail]**](ConfigTypeDetail.md) | An array of config-type resources | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openziti_edge_management.models.list_config_types_envelope import ListConfigTypesEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ListConfigTypesEnvelope from a JSON string
list_config_types_envelope_instance = ListConfigTypesEnvelope.from_json(json)
# print the JSON string representation of the object
print ListConfigTypesEnvelope.to_json()

# convert the object into a dict
list_config_types_envelope_dict = list_config_types_envelope_instance.to_dict()
# create an instance of ListConfigTypesEnvelope from a dict
list_config_types_envelope_form_dict = list_config_types_envelope.from_dict(list_config_types_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


