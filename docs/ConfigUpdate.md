# ConfigUpdate

A config update object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **Dict[str, object]** | Data payload is defined by the schema of the config-type defined in the type parameter | 
**name** | **str** |  | 
**tags** | [**Tags**](Tags.md) |  | [optional] 

## Example

```python
from openziti_edge_management.models.config_update import ConfigUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigUpdate from a JSON string
config_update_instance = ConfigUpdate.from_json(json)
# print the JSON string representation of the object
print ConfigUpdate.to_json()

# convert the object into a dict
config_update_dict = config_update_instance.to_dict()
# create an instance of ConfigUpdate from a dict
config_update_form_dict = config_update.from_dict(config_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


