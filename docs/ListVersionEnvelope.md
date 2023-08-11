# ListVersionEnvelope


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Version**](Version.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openziti_edge_management.models.list_version_envelope import ListVersionEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ListVersionEnvelope from a JSON string
list_version_envelope_instance = ListVersionEnvelope.from_json(json)
# print the JSON string representation of the object
print ListVersionEnvelope.to_json()

# convert the object into a dict
list_version_envelope_dict = list_version_envelope_instance.to_dict()
# create an instance of ListVersionEnvelope from a dict
list_version_envelope_form_dict = list_version_envelope.from_dict(list_version_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


