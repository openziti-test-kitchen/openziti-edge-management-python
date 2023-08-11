# PostureCheckOperatingSystemPatch


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operating_systems** | [**List[OperatingSystem]**](OperatingSystem.md) |  | [optional] 

## Example

```python
from openziti_edge_management.models.posture_check_operating_system_patch import PostureCheckOperatingSystemPatch

# TODO update the JSON string below
json = "{}"
# create an instance of PostureCheckOperatingSystemPatch from a JSON string
posture_check_operating_system_patch_instance = PostureCheckOperatingSystemPatch.from_json(json)
# print the JSON string representation of the object
print PostureCheckOperatingSystemPatch.to_json()

# convert the object into a dict
posture_check_operating_system_patch_dict = posture_check_operating_system_patch_instance.to_dict()
# create an instance of PostureCheckOperatingSystemPatch from a dict
posture_check_operating_system_patch_form_dict = posture_check_operating_system_patch.from_dict(posture_check_operating_system_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


