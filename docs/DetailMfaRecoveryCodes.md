# DetailMfaRecoveryCodes


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) | A map of named links | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**tags** | [**Tags**](Tags.md) |  | [optional] 
**updated_at** | **datetime** |  | 
**recovery_codes** | **List[str]** |  | 

## Example

```python
from openziti_edge_management.models.detail_mfa_recovery_codes import DetailMfaRecoveryCodes

# TODO update the JSON string below
json = "{}"
# create an instance of DetailMfaRecoveryCodes from a JSON string
detail_mfa_recovery_codes_instance = DetailMfaRecoveryCodes.from_json(json)
# print the JSON string representation of the object
print DetailMfaRecoveryCodes.to_json()

# convert the object into a dict
detail_mfa_recovery_codes_dict = detail_mfa_recovery_codes_instance.to_dict()
# create an instance of DetailMfaRecoveryCodes from a dict
detail_mfa_recovery_codes_form_dict = detail_mfa_recovery_codes.from_dict(detail_mfa_recovery_codes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


