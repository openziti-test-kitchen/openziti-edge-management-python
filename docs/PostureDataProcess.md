# PostureDataProcess


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_updated_at** | **datetime** |  | 
**posture_check_id** | **str** |  | 
**timed_out** | **bool** |  | 
**binary_hash** | **str** |  | [optional] 
**is_running** | **bool** |  | [optional] 
**signer_fingerprints** | **List[str]** |  | [optional] 

## Example

```python
from openziti_edge_management.models.posture_data_process import PostureDataProcess

# TODO update the JSON string below
json = "{}"
# create an instance of PostureDataProcess from a JSON string
posture_data_process_instance = PostureDataProcess.from_json(json)
# print the JSON string representation of the object
print PostureDataProcess.to_json()

# convert the object into a dict
posture_data_process_dict = posture_data_process_instance.to_dict()
# create an instance of PostureDataProcess from a dict
posture_data_process_form_dict = posture_data_process.from_dict(posture_data_process_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


