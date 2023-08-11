# ListServicesEnvelope


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ServiceDetail]**](ServiceDetail.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openziti_edge_management.models.list_services_envelope import ListServicesEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ListServicesEnvelope from a JSON string
list_services_envelope_instance = ListServicesEnvelope.from_json(json)
# print the JSON string representation of the object
print ListServicesEnvelope.to_json()

# convert the object into a dict
list_services_envelope_dict = list_services_envelope_instance.to_dict()
# create an instance of ListServicesEnvelope from a dict
list_services_envelope_form_dict = list_services_envelope.from_dict(list_services_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


