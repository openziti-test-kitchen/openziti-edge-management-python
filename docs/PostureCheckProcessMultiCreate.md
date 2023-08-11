# PostureCheckProcessMultiCreate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**processes** | [**List[ProcessMulti]**](ProcessMulti.md) |  | 
**semantic** | [**Semantic**](Semantic.md) |  | 

## Example

```python
from openziti_edge_management.models.posture_check_process_multi_create import PostureCheckProcessMultiCreate

# TODO update the JSON string below
json = "{}"
# create an instance of PostureCheckProcessMultiCreate from a JSON string
posture_check_process_multi_create_instance = PostureCheckProcessMultiCreate.from_json(json)
# print the JSON string representation of the object
print PostureCheckProcessMultiCreate.to_json()

# convert the object into a dict
posture_check_process_multi_create_dict = posture_check_process_multi_create_instance.to_dict()
# create an instance of PostureCheckProcessMultiCreate from a dict
posture_check_process_multi_create_form_dict = posture_check_process_multi_create.from_dict(posture_check_process_multi_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


