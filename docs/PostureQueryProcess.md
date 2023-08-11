# PostureQueryProcess


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**os_type** | [**OsType**](OsType.md) |  | [optional] 
**path** | **str** |  | [optional] 

## Example

```python
from openziti_edge_management.models.posture_query_process import PostureQueryProcess

# TODO update the JSON string below
json = "{}"
# create an instance of PostureQueryProcess from a JSON string
posture_query_process_instance = PostureQueryProcess.from_json(json)
# print the JSON string representation of the object
print PostureQueryProcess.to_json()

# convert the object into a dict
posture_query_process_dict = posture_query_process_instance.to_dict()
# create an instance of PostureQueryProcess from a dict
posture_query_process_form_dict = posture_query_process.from_dict(posture_query_process_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


