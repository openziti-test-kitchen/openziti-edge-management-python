# ListServiceConfigsEnvelope


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ServiceConfigDetail]**](ServiceConfigDetail.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openziti_edge_management.models.list_service_configs_envelope import ListServiceConfigsEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ListServiceConfigsEnvelope from a JSON string
list_service_configs_envelope_instance = ListServiceConfigsEnvelope.from_json(json)
# print the JSON string representation of the object
print ListServiceConfigsEnvelope.to_json()

# convert the object into a dict
list_service_configs_envelope_dict = list_service_configs_envelope_instance.to_dict()
# create an instance of ListServiceConfigsEnvelope from a dict
list_service_configs_envelope_form_dict = list_service_configs_envelope.from_dict(list_service_configs_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


