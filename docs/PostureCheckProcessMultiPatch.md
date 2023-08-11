# PostureCheckProcessMultiPatch


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**processes** | [**List[ProcessMulti]**](ProcessMulti.md) |  | [optional] 
**semantic** | [**Semantic**](Semantic.md) |  | [optional] 

## Example

```python
from openziti_edge_management.models.posture_check_process_multi_patch import PostureCheckProcessMultiPatch

# TODO update the JSON string below
json = "{}"
# create an instance of PostureCheckProcessMultiPatch from a JSON string
posture_check_process_multi_patch_instance = PostureCheckProcessMultiPatch.from_json(json)
# print the JSON string representation of the object
print PostureCheckProcessMultiPatch.to_json()

# convert the object into a dict
posture_check_process_multi_patch_dict = posture_check_process_multi_patch_instance.to_dict()
# create an instance of PostureCheckProcessMultiPatch from a dict
posture_check_process_multi_patch_form_dict = posture_check_process_multi_patch.from_dict(posture_check_process_multi_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


