# OperatingSystem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**OsType**](OsType.md) |  | 
**versions** | **List[str]** |  | 

## Example

```python
from openziti_edge_management.models.operating_system import OperatingSystem

# TODO update the JSON string below
json = "{}"
# create an instance of OperatingSystem from a JSON string
operating_system_instance = OperatingSystem.from_json(json)
# print the JSON string representation of the object
print OperatingSystem.to_json()

# convert the object into a dict
operating_system_dict = operating_system_instance.to_dict()
# create an instance of OperatingSystem from a dict
operating_system_form_dict = operating_system.from_dict(operating_system_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


