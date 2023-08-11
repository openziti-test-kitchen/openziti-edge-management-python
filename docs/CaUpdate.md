# CaUpdate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_id_claim** | [**ExternalIdClaim**](ExternalIdClaim.md) |  | [optional] 
**identity_name_format** | **str** |  | 
**identity_roles** | **List[str]** |  | 
**is_auth_enabled** | **bool** |  | 
**is_auto_ca_enrollment_enabled** | **bool** |  | 
**is_ott_ca_enrollment_enabled** | **bool** |  | 
**name** | **str** |  | 
**tags** | [**Tags**](Tags.md) |  | [optional] 

## Example

```python
from openziti_edge_management.models.ca_update import CaUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of CaUpdate from a JSON string
ca_update_instance = CaUpdate.from_json(json)
# print the JSON string representation of the object
print CaUpdate.to_json()

# convert the object into a dict
ca_update_dict = ca_update_instance.to_dict()
# create an instance of CaUpdate from a dict
ca_update_form_dict = ca_update.from_dict(ca_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


