# PostureCheckOperatingSystemDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operating_systems** | [**List[OperatingSystem]**](OperatingSystem.md) |  | 

## Example

```python
from openziti_edge_management.models.posture_check_operating_system_detail import PostureCheckOperatingSystemDetail

# TODO update the JSON string below
json = "{}"
# create an instance of PostureCheckOperatingSystemDetail from a JSON string
posture_check_operating_system_detail_instance = PostureCheckOperatingSystemDetail.from_json(json)
# print the JSON string representation of the object
print PostureCheckOperatingSystemDetail.to_json()

# convert the object into a dict
posture_check_operating_system_detail_dict = posture_check_operating_system_detail_instance.to_dict()
# create an instance of PostureCheckOperatingSystemDetail from a dict
posture_check_operating_system_detail_form_dict = posture_check_operating_system_detail.from_dict(posture_check_operating_system_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


