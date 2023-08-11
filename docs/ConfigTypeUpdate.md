# ConfigTypeUpdate

A config-type update object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**var_schema** | **Dict[str, object]** | A JSON schema to enforce configuration against | [optional] 
**tags** | [**Tags**](Tags.md) |  | [optional] 

## Example

```python
from openziti_edge_management.models.config_type_update import ConfigTypeUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigTypeUpdate from a JSON string
config_type_update_instance = ConfigTypeUpdate.from_json(json)
# print the JSON string representation of the object
print ConfigTypeUpdate.to_json()

# convert the object into a dict
config_type_update_dict = config_type_update_instance.to_dict()
# create an instance of ConfigTypeUpdate from a dict
config_type_update_form_dict = config_type_update.from_dict(config_type_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


