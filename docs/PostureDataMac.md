# PostureDataMac


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_updated_at** | **datetime** |  | 
**posture_check_id** | **str** |  | 
**timed_out** | **bool** |  | 
**addresses** | **List[str]** |  | 

## Example

```python
from openziti_edge_management.models.posture_data_mac import PostureDataMac

# TODO update the JSON string below
json = "{}"
# create an instance of PostureDataMac from a JSON string
posture_data_mac_instance = PostureDataMac.from_json(json)
# print the JSON string representation of the object
print PostureDataMac.to_json()

# convert the object into a dict
posture_data_mac_dict = posture_data_mac_instance.to_dict()
# create an instance of PostureDataMac from a dict
posture_data_mac_form_dict = posture_data_mac.from_dict(posture_data_mac_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


