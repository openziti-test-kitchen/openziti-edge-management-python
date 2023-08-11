# ListApiSessionsEnvelope


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ApiSessionDetail]**](ApiSessionDetail.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openziti_edge_management.models.list_api_sessions_envelope import ListApiSessionsEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ListApiSessionsEnvelope from a JSON string
list_api_sessions_envelope_instance = ListApiSessionsEnvelope.from_json(json)
# print the JSON string representation of the object
print ListApiSessionsEnvelope.to_json()

# convert the object into a dict
list_api_sessions_envelope_dict = list_api_sessions_envelope_instance.to_dict()
# create an instance of ListApiSessionsEnvelope from a dict
list_api_sessions_envelope_form_dict = list_api_sessions_envelope.from_dict(list_api_sessions_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


