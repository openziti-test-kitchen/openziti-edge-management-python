# RouterUpdate


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
from openziti_edge_management.models.router_update import RouterUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of RouterUpdate from a JSON string
router_update_instance = RouterUpdate.from_json(json)
# print the JSON string representation of the object
print RouterUpdate.to_json()

# convert the object into a dict
router_update_dict = router_update_instance.to_dict()
# create an instance of RouterUpdate from a dict
router_update_form_dict = router_update.from_dict(router_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


