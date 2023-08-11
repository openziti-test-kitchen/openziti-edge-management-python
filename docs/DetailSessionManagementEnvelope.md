# DetailSessionManagementEnvelope


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SessionManagementDetail**](SessionManagementDetail.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openziti_edge_management.models.detail_session_management_envelope import DetailSessionManagementEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of DetailSessionManagementEnvelope from a JSON string
detail_session_management_envelope_instance = DetailSessionManagementEnvelope.from_json(json)
# print the JSON string representation of the object
print DetailSessionManagementEnvelope.to_json()

# convert the object into a dict
detail_session_management_envelope_dict = detail_session_management_envelope_instance.to_dict()
# create an instance of DetailSessionManagementEnvelope from a dict
detail_session_management_envelope_form_dict = detail_session_management_envelope.from_dict(detail_session_management_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


