# DetailPostureCheckTypeEnvelope


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PostureCheckTypeDetail**](PostureCheckTypeDetail.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openziti_edge_management.models.detail_posture_check_type_envelope import DetailPostureCheckTypeEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of DetailPostureCheckTypeEnvelope from a JSON string
detail_posture_check_type_envelope_instance = DetailPostureCheckTypeEnvelope.from_json(json)
# print the JSON string representation of the object
print DetailPostureCheckTypeEnvelope.to_json()

# convert the object into a dict
detail_posture_check_type_envelope_dict = detail_posture_check_type_envelope_instance.to_dict()
# create an instance of DetailPostureCheckTypeEnvelope from a dict
detail_posture_check_type_envelope_form_dict = detail_posture_check_type_envelope.from_dict(detail_posture_check_type_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


