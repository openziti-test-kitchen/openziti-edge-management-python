# PostureCheckProcessUpdate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**process** | [**Process**](Process.md) |  | 

## Example

```python
from openziti_edge_management.models.posture_check_process_update import PostureCheckProcessUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of PostureCheckProcessUpdate from a JSON string
posture_check_process_update_instance = PostureCheckProcessUpdate.from_json(json)
# print the JSON string representation of the object
print PostureCheckProcessUpdate.to_json()

# convert the object into a dict
posture_check_process_update_dict = posture_check_process_update_instance.to_dict()
# create an instance of PostureCheckProcessUpdate from a dict
posture_check_process_update_form_dict = posture_check_process_update.from_dict(posture_check_process_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


