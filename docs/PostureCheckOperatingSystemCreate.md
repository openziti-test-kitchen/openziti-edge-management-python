# PostureCheckOperatingSystemCreate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operating_systems** | [**List[OperatingSystem]**](OperatingSystem.md) |  | 

## Example

```python
from openziti_edge_management.models.posture_check_operating_system_create import PostureCheckOperatingSystemCreate

# TODO update the JSON string below
json = "{}"
# create an instance of PostureCheckOperatingSystemCreate from a JSON string
posture_check_operating_system_create_instance = PostureCheckOperatingSystemCreate.from_json(json)
# print the JSON string representation of the object
print PostureCheckOperatingSystemCreate.to_json()

# convert the object into a dict
posture_check_operating_system_create_dict = posture_check_operating_system_create_instance.to_dict()
# create an instance of PostureCheckOperatingSystemCreate from a dict
posture_check_operating_system_create_form_dict = posture_check_operating_system_create.from_dict(posture_check_operating_system_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


