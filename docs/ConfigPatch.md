# ConfigPatch

A config patch object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **Dict[str, object]** | Data payload is defined by the schema of the config-type defined in the type parameter | [optional] 
**name** | **str** |  | [optional] 
**tags** | [**Tags**](Tags.md) |  | [optional] 

## Example

```python
from openziti_edge_management.models.config_patch import ConfigPatch

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigPatch from a JSON string
config_patch_instance = ConfigPatch.from_json(json)
# print the JSON string representation of the object
print ConfigPatch.to_json()

# convert the object into a dict
config_patch_dict = config_patch_instance.to_dict()
# create an instance of ConfigPatch from a dict
config_patch_form_dict = config_patch.from_dict(config_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


