# BaseEntity

Fields shared by all Edge API entities

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) | A map of named links | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**tags** | [**Tags**](Tags.md) |  | [optional] 
**updated_at** | **datetime** |  | 

## Example

```python
from openziti_edge_management.models.base_entity import BaseEntity

# TODO update the JSON string below
json = "{}"
# create an instance of BaseEntity from a JSON string
base_entity_instance = BaseEntity.from_json(json)
# print the JSON string representation of the object
print BaseEntity.to_json()

# convert the object into a dict
base_entity_dict = base_entity_instance.to_dict()
# create an instance of BaseEntity from a dict
base_entity_form_dict = base_entity.from_dict(base_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


