# DetailMfa


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) | A map of named links | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**tags** | [**Tags**](Tags.md) |  | [optional] 
**updated_at** | **datetime** |  | 
**is_verified** | **bool** |  | 
**provisioning_url** | **str** | Not provided if MFA verification has been completed | [optional] 
**recovery_codes** | **List[str]** | Not provided if MFA verification has been completed | [optional] 

## Example

```python
from openziti_edge_management.models.detail_mfa import DetailMfa

# TODO update the JSON string below
json = "{}"
# create an instance of DetailMfa from a JSON string
detail_mfa_instance = DetailMfa.from_json(json)
# print the JSON string representation of the object
print DetailMfa.to_json()

# convert the object into a dict
detail_mfa_dict = detail_mfa_instance.to_dict()
# create an instance of DetailMfa from a dict
detail_mfa_form_dict = detail_mfa.from_dict(detail_mfa_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


