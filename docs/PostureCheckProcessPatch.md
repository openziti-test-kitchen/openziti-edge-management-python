# PostureCheckProcessPatch


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**process** | [**Process**](Process.md) |  | [optional] 

## Example

```python
from openziti_edge_management.models.posture_check_process_patch import PostureCheckProcessPatch

# TODO update the JSON string below
json = "{}"
# create an instance of PostureCheckProcessPatch from a JSON string
posture_check_process_patch_instance = PostureCheckProcessPatch.from_json(json)
# print the JSON string representation of the object
print PostureCheckProcessPatch.to_json()

# convert the object into a dict
posture_check_process_patch_dict = posture_check_process_patch_instance.to_dict()
# create an instance of PostureCheckProcessPatch from a dict
posture_check_process_patch_form_dict = posture_check_process_patch.from_dict(posture_check_process_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


