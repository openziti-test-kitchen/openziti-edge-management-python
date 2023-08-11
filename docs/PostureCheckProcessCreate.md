# PostureCheckProcessCreate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**process** | [**Process**](Process.md) |  | 

## Example

```python
from openziti_edge_management.models.posture_check_process_create import PostureCheckProcessCreate

# TODO update the JSON string below
json = "{}"
# create an instance of PostureCheckProcessCreate from a JSON string
posture_check_process_create_instance = PostureCheckProcessCreate.from_json(json)
# print the JSON string representation of the object
print PostureCheckProcessCreate.to_json()

# convert the object into a dict
posture_check_process_create_dict = posture_check_process_create_instance.to_dict()
# create an instance of PostureCheckProcessCreate from a dict
posture_check_process_create_form_dict = posture_check_process_create.from_dict(posture_check_process_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


