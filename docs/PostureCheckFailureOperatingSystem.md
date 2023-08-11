# PostureCheckFailureOperatingSystem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actual_value** | [**PostureCheckFailureOperatingSystemActual**](PostureCheckFailureOperatingSystemActual.md) |  | 
**expected_value** | [**List[OperatingSystem]**](OperatingSystem.md) |  | 

## Example

```python
from openziti_edge_management.models.posture_check_failure_operating_system import PostureCheckFailureOperatingSystem

# TODO update the JSON string below
json = "{}"
# create an instance of PostureCheckFailureOperatingSystem from a JSON string
posture_check_failure_operating_system_instance = PostureCheckFailureOperatingSystem.from_json(json)
# print the JSON string representation of the object
print PostureCheckFailureOperatingSystem.to_json()

# convert the object into a dict
posture_check_failure_operating_system_dict = posture_check_failure_operating_system_instance.to_dict()
# create an instance of PostureCheckFailureOperatingSystem from a dict
posture_check_failure_operating_system_form_dict = posture_check_failure_operating_system.from_dict(posture_check_failure_operating_system_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


