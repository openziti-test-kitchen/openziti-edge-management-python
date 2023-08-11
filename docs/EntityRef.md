# EntityRef

A reference to another resource and links to interact with it

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) | A map of named links | [optional] 
**entity** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from openziti_edge_management.models.entity_ref import EntityRef

# TODO update the JSON string below
json = "{}"
# create an instance of EntityRef from a JSON string
entity_ref_instance = EntityRef.from_json(json)
# print the JSON string representation of the object
print EntityRef.to_json()

# convert the object into a dict
entity_ref_dict = entity_ref_instance.to_dict()
# create an instance of EntityRef from a dict
entity_ref_form_dict = entity_ref.from_dict(entity_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


