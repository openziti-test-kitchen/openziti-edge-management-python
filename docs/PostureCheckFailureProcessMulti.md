# PostureCheckFailureProcessMulti


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actual_value** | [**List[PostureCheckFailureProcessActual]**](PostureCheckFailureProcessActual.md) |  | 
**expected_value** | [**List[ProcessMulti]**](ProcessMulti.md) |  | 
**semantic** | [**Semantic**](Semantic.md) |  | 

## Example

```python
from openziti_edge_management.models.posture_check_failure_process_multi import PostureCheckFailureProcessMulti

# TODO update the JSON string below
json = "{}"
# create an instance of PostureCheckFailureProcessMulti from a JSON string
posture_check_failure_process_multi_instance = PostureCheckFailureProcessMulti.from_json(json)
# print the JSON string representation of the object
print PostureCheckFailureProcessMulti.to_json()

# convert the object into a dict
posture_check_failure_process_multi_dict = posture_check_failure_process_multi_instance.to_dict()
# create an instance of PostureCheckFailureProcessMulti from a dict
posture_check_failure_process_multi_form_dict = posture_check_failure_process_multi.from_dict(posture_check_failure_process_multi_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


