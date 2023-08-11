# RouterCreate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cost** | **int** |  | [optional] 
**disabled** | **bool** |  | [optional] 
**name** | **str** |  | 
**no_traversal** | **bool** |  | [optional] 
**tags** | [**Tags**](Tags.md) |  | [optional] 

## Example

```python
from openziti_edge_management.models.router_create import RouterCreate

# TODO update the JSON string below
json = "{}"
# create an instance of RouterCreate from a JSON string
router_create_instance = RouterCreate.from_json(json)
# print the JSON string representation of the object
print RouterCreate.to_json()

# convert the object into a dict
router_create_dict = router_create_instance.to_dict()
# create an instance of RouterCreate from a dict
router_create_form_dict = router_create.from_dict(router_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


