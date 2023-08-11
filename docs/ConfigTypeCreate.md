# ConfigTypeCreate

A config-type create object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**var_schema** | **Dict[str, object]** | A JSON schema to enforce configuration against | [optional] 
**tags** | [**Tags**](Tags.md) |  | [optional] 

## Example

```python
from openziti_edge_management.models.config_type_create import ConfigTypeCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigTypeCreate from a JSON string
config_type_create_instance = ConfigTypeCreate.from_json(json)
# print the JSON string representation of the object
print ConfigTypeCreate.to_json()

# convert the object into a dict
config_type_create_dict = config_type_create_instance.to_dict()
# create an instance of ConfigTypeCreate from a dict
config_type_create_form_dict = config_type_create.from_dict(config_type_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


