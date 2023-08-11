# PostureCheckFailureProcess


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actual_value** | [**PostureCheckFailureProcessActual**](PostureCheckFailureProcessActual.md) |  | 
**expected_value** | [**Process**](Process.md) |  | 

## Example

```python
from openziti_edge_management.models.posture_check_failure_process import PostureCheckFailureProcess

# TODO update the JSON string below
json = "{}"
# create an instance of PostureCheckFailureProcess from a JSON string
posture_check_failure_process_instance = PostureCheckFailureProcess.from_json(json)
# print the JSON string representation of the object
print PostureCheckFailureProcess.to_json()

# convert the object into a dict
posture_check_failure_process_dict = posture_check_failure_process_instance.to_dict()
# create an instance of PostureCheckFailureProcess from a dict
posture_check_failure_process_form_dict = posture_check_failure_process.from_dict(posture_check_failure_process_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


