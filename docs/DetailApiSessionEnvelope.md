# DetailApiSessionEnvelope


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ApiSessionDetail**](ApiSessionDetail.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openziti_edge_management.models.detail_api_session_envelope import DetailApiSessionEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of DetailApiSessionEnvelope from a JSON string
detail_api_session_envelope_instance = DetailApiSessionEnvelope.from_json(json)
# print the JSON string representation of the object
print DetailApiSessionEnvelope.to_json()

# convert the object into a dict
detail_api_session_envelope_dict = detail_api_session_envelope_instance.to_dict()
# create an instance of DetailApiSessionEnvelope from a dict
detail_api_session_envelope_form_dict = detail_api_session_envelope.from_dict(detail_api_session_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


