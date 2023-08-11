# PostureCheckProcessDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**process** | [**Process**](Process.md) |  | 

## Example

```python
from openziti_edge_management.models.posture_check_process_detail import PostureCheckProcessDetail

# TODO update the JSON string below
json = "{}"
# create an instance of PostureCheckProcessDetail from a JSON string
posture_check_process_detail_instance = PostureCheckProcessDetail.from_json(json)
# print the JSON string representation of the object
print PostureCheckProcessDetail.to_json()

# convert the object into a dict
posture_check_process_detail_dict = posture_check_process_detail_instance.to_dict()
# create an instance of PostureCheckProcessDetail from a dict
posture_check_process_detail_form_dict = posture_check_process_detail.from_dict(posture_check_process_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


