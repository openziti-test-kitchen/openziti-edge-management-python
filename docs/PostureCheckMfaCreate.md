# PostureCheckMfaCreate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ignore_legacy_endpoints** | **bool** |  | [optional] 
**prompt_on_unlock** | **bool** |  | [optional] 
**prompt_on_wake** | **bool** |  | [optional] 
**timeout_seconds** | **int** |  | [optional] 

## Example

```python
from openziti_edge_management.models.posture_check_mfa_create import PostureCheckMfaCreate

# TODO update the JSON string below
json = "{}"
# create an instance of PostureCheckMfaCreate from a JSON string
posture_check_mfa_create_instance = PostureCheckMfaCreate.from_json(json)
# print the JSON string representation of the object
print PostureCheckMfaCreate.to_json()

# convert the object into a dict
posture_check_mfa_create_dict = posture_check_mfa_create_instance.to_dict()
# create an instance of PostureCheckMfaCreate from a dict
posture_check_mfa_create_form_dict = posture_check_mfa_create.from_dict(posture_check_mfa_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


