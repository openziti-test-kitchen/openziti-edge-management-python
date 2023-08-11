# PostureDataOs


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_updated_at** | **datetime** |  | 
**posture_check_id** | **str** |  | 
**timed_out** | **bool** |  | 
**build** | **str** |  | 
**type** | **str** |  | 
**version** | **str** |  | 

## Example

```python
from openziti_edge_management.models.posture_data_os import PostureDataOs

# TODO update the JSON string below
json = "{}"
# create an instance of PostureDataOs from a JSON string
posture_data_os_instance = PostureDataOs.from_json(json)
# print the JSON string representation of the object
print PostureDataOs.to_json()

# convert the object into a dict
posture_data_os_dict = posture_data_os_instance.to_dict()
# create an instance of PostureDataOs from a dict
posture_data_os_form_dict = posture_data_os.from_dict(posture_data_os_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


