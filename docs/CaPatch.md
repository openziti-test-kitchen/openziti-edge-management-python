# CaPatch


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_id_claim** | [**ExternalIdClaimPatch**](ExternalIdClaimPatch.md) |  | [optional] 
**identity_name_format** | **str** |  | [optional] 
**identity_roles** | **List[str]** |  | [optional] 
**is_auth_enabled** | **bool** |  | [optional] 
**is_auto_ca_enrollment_enabled** | **bool** |  | [optional] 
**is_ott_ca_enrollment_enabled** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**tags** | [**Tags**](Tags.md) |  | [optional] 

## Example

```python
from openziti_edge_management.models.ca_patch import CaPatch

# TODO update the JSON string below
json = "{}"
# create an instance of CaPatch from a JSON string
ca_patch_instance = CaPatch.from_json(json)
# print the JSON string representation of the object
print CaPatch.to_json()

# convert the object into a dict
ca_patch_dict = ca_patch_instance.to_dict()
# create an instance of CaPatch from a dict
ca_patch_form_dict = ca_patch.from_dict(ca_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


