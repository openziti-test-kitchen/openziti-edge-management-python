# PostureCheckFailure


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**posture_check_id** | **str** |  | 
**posture_check_name** | **str** |  | 
**posture_check_type** | **str** |  | 

## Example

```python
from openziti_edge_management.models.posture_check_failure import PostureCheckFailure

# TODO update the JSON string below
json = "{}"
# create an instance of PostureCheckFailure from a JSON string
posture_check_failure_instance = PostureCheckFailure.from_json(json)
# print the JSON string representation of the object
print PostureCheckFailure.to_json()

# convert the object into a dict
posture_check_failure_dict = posture_check_failure_instance.to_dict()
# create an instance of PostureCheckFailure from a dict
posture_check_failure_form_dict = posture_check_failure.from_dict(posture_check_failure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


