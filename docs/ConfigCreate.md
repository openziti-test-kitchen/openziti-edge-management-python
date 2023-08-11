# ConfigCreate

A config create object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_type_id** | **str** | The id of a config-type that the data section will match | 
**data** | **Dict[str, object]** | Data payload is defined by the schema of the config-type defined in the type parameter | 
**name** | **str** |  | 
**tags** | [**Tags**](Tags.md) |  | [optional] 

## Example

```python
from openziti_edge_management.models.config_create import ConfigCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigCreate from a JSON string
config_create_instance = ConfigCreate.from_json(json)
# print the JSON string representation of the object
print ConfigCreate.to_json()

# convert the object into a dict
config_create_dict = config_create_instance.to_dict()
# create an instance of ConfigCreate from a dict
config_create_form_dict = config_create.from_dict(config_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


