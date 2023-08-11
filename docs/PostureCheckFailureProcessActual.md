# PostureCheckFailureProcessActual


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hash** | **str** |  | 
**is_running** | **bool** |  | 
**os_type** | [**OsType**](OsType.md) |  | [optional] 
**path** | **str** |  | [optional] 
**signer_fingerprints** | **List[str]** |  | 

## Example

```python
from openziti_edge_management.models.posture_check_failure_process_actual import PostureCheckFailureProcessActual

# TODO update the JSON string below
json = "{}"
# create an instance of PostureCheckFailureProcessActual from a JSON string
posture_check_failure_process_actual_instance = PostureCheckFailureProcessActual.from_json(json)
# print the JSON string representation of the object
print PostureCheckFailureProcessActual.to_json()

# convert the object into a dict
posture_check_failure_process_actual_dict = posture_check_failure_process_actual_instance.to_dict()
# create an instance of PostureCheckFailureProcessActual from a dict
posture_check_failure_process_actual_form_dict = posture_check_failure_process_actual.from_dict(posture_check_failure_process_actual_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


