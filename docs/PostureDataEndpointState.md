# PostureDataEndpointState


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unlocked_at** | **datetime** |  | 
**woken_at** | **datetime** |  | 

## Example

```python
from openziti_edge_management.models.posture_data_endpoint_state import PostureDataEndpointState

# TODO update the JSON string below
json = "{}"
# create an instance of PostureDataEndpointState from a JSON string
posture_data_endpoint_state_instance = PostureDataEndpointState.from_json(json)
# print the JSON string representation of the object
print PostureDataEndpointState.to_json()

# convert the object into a dict
posture_data_endpoint_state_dict = posture_data_endpoint_state_instance.to_dict()
# create an instance of PostureDataEndpointState from a dict
posture_data_endpoint_state_form_dict = posture_data_endpoint_state.from_dict(posture_data_endpoint_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


