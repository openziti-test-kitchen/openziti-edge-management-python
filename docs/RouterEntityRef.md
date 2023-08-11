# RouterEntityRef


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) | A map of named links | [optional] 
**entity** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**is_online** | **bool** |  | 

## Example

```python
from openziti_edge_management.models.router_entity_ref import RouterEntityRef

# TODO update the JSON string below
json = "{}"
# create an instance of RouterEntityRef from a JSON string
router_entity_ref_instance = RouterEntityRef.from_json(json)
# print the JSON string representation of the object
print RouterEntityRef.to_json()

# convert the object into a dict
router_entity_ref_dict = router_entity_ref_instance.to_dict()
# create an instance of RouterEntityRef from a dict
router_entity_ref_form_dict = router_entity_ref.from_dict(router_entity_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


