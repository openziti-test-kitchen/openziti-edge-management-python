# ListPostureCheckTypesEnvelope


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PostureCheckTypeDetail]**](PostureCheckTypeDetail.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openziti_edge_management.models.list_posture_check_types_envelope import ListPostureCheckTypesEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ListPostureCheckTypesEnvelope from a JSON string
list_posture_check_types_envelope_instance = ListPostureCheckTypesEnvelope.from_json(json)
# print the JSON string representation of the object
print ListPostureCheckTypesEnvelope.to_json()

# convert the object into a dict
list_posture_check_types_envelope_dict = list_posture_check_types_envelope_instance.to_dict()
# create an instance of ListPostureCheckTypesEnvelope from a dict
list_posture_check_types_envelope_form_dict = list_posture_check_types_envelope.from_dict(list_posture_check_types_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


