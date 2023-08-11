# PostureDataEnvelope


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PostureData**](PostureData.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openziti_edge_management.models.posture_data_envelope import PostureDataEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of PostureDataEnvelope from a JSON string
posture_data_envelope_instance = PostureDataEnvelope.from_json(json)
# print the JSON string representation of the object
print PostureDataEnvelope.to_json()

# convert the object into a dict
posture_data_envelope_dict = posture_data_envelope_instance.to_dict()
# create an instance of PostureDataEnvelope from a dict
posture_data_envelope_form_dict = posture_data_envelope.from_dict(posture_data_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


