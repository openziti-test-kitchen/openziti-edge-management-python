# PostureDataBase


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_updated_at** | **datetime** |  | 
**posture_check_id** | **str** |  | 
**timed_out** | **bool** |  | 

## Example

```python
from openziti_edge_management.models.posture_data_base import PostureDataBase

# TODO update the JSON string below
json = "{}"
# create an instance of PostureDataBase from a JSON string
posture_data_base_instance = PostureDataBase.from_json(json)
# print the JSON string representation of the object
print PostureDataBase.to_json()

# convert the object into a dict
posture_data_base_dict = posture_data_base_instance.to_dict()
# create an instance of PostureDataBase from a dict
posture_data_base_form_dict = posture_data_base.from_dict(posture_data_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


