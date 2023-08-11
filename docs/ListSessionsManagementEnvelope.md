# ListSessionsManagementEnvelope


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SessionManagementDetail]**](SessionManagementDetail.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openziti_edge_management.models.list_sessions_management_envelope import ListSessionsManagementEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ListSessionsManagementEnvelope from a JSON string
list_sessions_management_envelope_instance = ListSessionsManagementEnvelope.from_json(json)
# print the JSON string representation of the object
print ListSessionsManagementEnvelope.to_json()

# convert the object into a dict
list_sessions_management_envelope_dict = list_sessions_management_envelope_instance.to_dict()
# create an instance of ListSessionsManagementEnvelope from a dict
list_sessions_management_envelope_form_dict = list_sessions_management_envelope.from_dict(list_sessions_management_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


