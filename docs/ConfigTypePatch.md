# ConfigTypePatch

A config-type patch object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**var_schema** | **Dict[str, object]** | A JSON schema to enforce configuration against | [optional] 
**tags** | [**Tags**](Tags.md) |  | [optional] 

## Example

```python
from openziti_edge_management.models.config_type_patch import ConfigTypePatch

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigTypePatch from a JSON string
config_type_patch_instance = ConfigTypePatch.from_json(json)
# print the JSON string representation of the object
print ConfigTypePatch.to_json()

# convert the object into a dict
config_type_patch_dict = config_type_patch_instance.to_dict()
# create an instance of ConfigTypePatch from a dict
config_type_patch_form_dict = config_type_patch.from_dict(config_type_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


