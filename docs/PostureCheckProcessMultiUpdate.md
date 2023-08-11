# PostureCheckProcessMultiUpdate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**processes** | [**List[ProcessMulti]**](ProcessMulti.md) |  | 
**semantic** | [**Semantic**](Semantic.md) |  | 

## Example

```python
from openziti_edge_management.models.posture_check_process_multi_update import PostureCheckProcessMultiUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of PostureCheckProcessMultiUpdate from a JSON string
posture_check_process_multi_update_instance = PostureCheckProcessMultiUpdate.from_json(json)
# print the JSON string representation of the object
print PostureCheckProcessMultiUpdate.to_json()

# convert the object into a dict
posture_check_process_multi_update_dict = posture_check_process_multi_update_instance.to_dict()
# create an instance of PostureCheckProcessMultiUpdate from a dict
posture_check_process_multi_update_form_dict = posture_check_process_multi_update.from_dict(posture_check_process_multi_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


