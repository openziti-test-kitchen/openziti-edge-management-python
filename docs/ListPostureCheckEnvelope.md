# ListPostureCheckEnvelope


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PostureCheckDetail]**](PostureCheckDetail.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openziti_edge_management.models.list_posture_check_envelope import ListPostureCheckEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ListPostureCheckEnvelope from a JSON string
list_posture_check_envelope_instance = ListPostureCheckEnvelope.from_json(json)
# print the JSON string representation of the object
print ListPostureCheckEnvelope.to_json()

# convert the object into a dict
list_posture_check_envelope_dict = list_posture_check_envelope_instance.to_dict()
# create an instance of ListPostureCheckEnvelope from a dict
list_posture_check_envelope_form_dict = list_posture_check_envelope.from_dict(list_posture_check_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


