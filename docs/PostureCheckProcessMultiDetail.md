# PostureCheckProcessMultiDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**processes** | [**List[ProcessMulti]**](ProcessMulti.md) |  | 
**semantic** | [**Semantic**](Semantic.md) |  | 

## Example

```python
from openziti_edge_management.models.posture_check_process_multi_detail import PostureCheckProcessMultiDetail

# TODO update the JSON string below
json = "{}"
# create an instance of PostureCheckProcessMultiDetail from a JSON string
posture_check_process_multi_detail_instance = PostureCheckProcessMultiDetail.from_json(json)
# print the JSON string representation of the object
print PostureCheckProcessMultiDetail.to_json()

# convert the object into a dict
posture_check_process_multi_detail_dict = posture_check_process_multi_detail_instance.to_dict()
# create an instance of PostureCheckProcessMultiDetail from a dict
posture_check_process_multi_detail_form_dict = posture_check_process_multi_detail.from_dict(posture_check_process_multi_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


