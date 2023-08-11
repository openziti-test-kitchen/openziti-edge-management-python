# ConfigDetail

A config resource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) | A map of named links | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**tags** | [**Tags**](Tags.md) |  | [optional] 
**updated_at** | **datetime** |  | 
**config_type** | [**EntityRef**](EntityRef.md) |  | 
**config_type_id** | **str** |  | 
**data** | **object** | The data section of a config is based on the schema of its type | 
**name** | **str** |  | 

## Example

```python
from openziti_edge_management.models.config_detail import ConfigDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigDetail from a JSON string
config_detail_instance = ConfigDetail.from_json(json)
# print the JSON string representation of the object
print ConfigDetail.to_json()

# convert the object into a dict
config_detail_dict = config_detail_instance.to_dict()
# create an instance of ConfigDetail from a dict
config_detail_form_dict = config_detail.from_dict(config_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


