# RouterPatch


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cost** | **int** |  | [optional] 
**disabled** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**no_traversal** | **bool** |  | [optional] 
**tags** | [**Tags**](Tags.md) |  | [optional] 

## Example

```python
from openziti_edge_management.models.router_patch import RouterPatch

# TODO update the JSON string below
json = "{}"
# create an instance of RouterPatch from a JSON string
router_patch_instance = RouterPatch.from_json(json)
# print the JSON string representation of the object
print RouterPatch.to_json()

# convert the object into a dict
router_patch_dict = router_patch_instance.to_dict()
# create an instance of RouterPatch from a dict
router_patch_form_dict = router_patch.from_dict(router_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


