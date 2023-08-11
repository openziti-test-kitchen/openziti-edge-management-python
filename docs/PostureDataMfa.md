# PostureDataMfa


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_session_id** | **str** |  | 
**passed_at** | **datetime** |  | 
**passed_mfa** | **bool** |  | 
**passed_on_unlock** | **bool** |  | 
**passed_on_wake** | **bool** |  | 

## Example

```python
from openziti_edge_management.models.posture_data_mfa import PostureDataMfa

# TODO update the JSON string below
json = "{}"
# create an instance of PostureDataMfa from a JSON string
posture_data_mfa_instance = PostureDataMfa.from_json(json)
# print the JSON string representation of the object
print PostureDataMfa.to_json()

# convert the object into a dict
posture_data_mfa_dict = posture_data_mfa_instance.to_dict()
# create an instance of PostureDataMfa from a dict
posture_data_mfa_form_dict = posture_data_mfa.from_dict(posture_data_mfa_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


