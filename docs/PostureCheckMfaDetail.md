# PostureCheckMfaDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ignore_legacy_endpoints** | **bool** |  | [optional] 
**prompt_on_unlock** | **bool** |  | [optional] 
**prompt_on_wake** | **bool** |  | [optional] 
**timeout_seconds** | **int** |  | [optional] 

## Example

```python
from openziti_edge_management.models.posture_check_mfa_detail import PostureCheckMfaDetail

# TODO update the JSON string below
json = "{}"
# create an instance of PostureCheckMfaDetail from a JSON string
posture_check_mfa_detail_instance = PostureCheckMfaDetail.from_json(json)
# print the JSON string representation of the object
print PostureCheckMfaDetail.to_json()

# convert the object into a dict
posture_check_mfa_detail_dict = posture_check_mfa_detail_instance.to_dict()
# create an instance of PostureCheckMfaDetail from a dict
posture_check_mfa_detail_form_dict = posture_check_mfa_detail.from_dict(posture_check_mfa_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


