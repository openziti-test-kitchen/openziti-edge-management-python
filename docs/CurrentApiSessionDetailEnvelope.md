# CurrentApiSessionDetailEnvelope


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CurrentApiSessionDetail**](CurrentApiSessionDetail.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openziti_edge_management.models.current_api_session_detail_envelope import CurrentApiSessionDetailEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of CurrentApiSessionDetailEnvelope from a JSON string
current_api_session_detail_envelope_instance = CurrentApiSessionDetailEnvelope.from_json(json)
# print the JSON string representation of the object
print CurrentApiSessionDetailEnvelope.to_json()

# convert the object into a dict
current_api_session_detail_envelope_dict = current_api_session_detail_envelope_instance.to_dict()
# create an instance of CurrentApiSessionDetailEnvelope from a dict
current_api_session_detail_envelope_form_dict = current_api_session_detail_envelope.from_dict(current_api_session_detail_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


