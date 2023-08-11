# CreateEnvelope


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CreateLocation**](CreateLocation.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from openziti_edge_management.models.create_envelope import CreateEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEnvelope from a JSON string
create_envelope_instance = CreateEnvelope.from_json(json)
# print the JSON string representation of the object
print CreateEnvelope.to_json()

# convert the object into a dict
create_envelope_dict = create_envelope_instance.to_dict()
# create an instance of CreateEnvelope from a dict
create_envelope_form_dict = create_envelope.from_dict(create_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


