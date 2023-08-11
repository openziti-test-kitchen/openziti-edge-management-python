# PostureCheckOperatingSystemUpdate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operating_systems** | [**List[OperatingSystem]**](OperatingSystem.md) |  | 

## Example

```python
from openziti_edge_management.models.posture_check_operating_system_update import PostureCheckOperatingSystemUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of PostureCheckOperatingSystemUpdate from a JSON string
posture_check_operating_system_update_instance = PostureCheckOperatingSystemUpdate.from_json(json)
# print the JSON string representation of the object
print PostureCheckOperatingSystemUpdate.to_json()

# convert the object into a dict
posture_check_operating_system_update_dict = posture_check_operating_system_update_instance.to_dict()
# create an instance of PostureCheckOperatingSystemUpdate from a dict
posture_check_operating_system_update_form_dict = posture_check_operating_system_update.from_dict(posture_check_operating_system_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


