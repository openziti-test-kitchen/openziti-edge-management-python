# CaCreate

A create Certificate Authority (CA) object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cert_pem** | **str** |  | 
**external_id_claim** | [**ExternalIdClaim**](ExternalIdClaim.md) |  | [optional] 
**identity_name_format** | **str** |  | [optional] 
**identity_roles** | **List[str]** |  | 
**is_auth_enabled** | **bool** |  | 
**is_auto_ca_enrollment_enabled** | **bool** |  | 
**is_ott_ca_enrollment_enabled** | **bool** |  | 
**name** | **str** |  | 
**tags** | [**Tags**](Tags.md) |  | [optional] 

## Example

```python
from openziti_edge_management.models.ca_create import CaCreate

# TODO update the JSON string below
json = "{}"
# create an instance of CaCreate from a JSON string
ca_create_instance = CaCreate.from_json(json)
# print the JSON string representation of the object
print CaCreate.to_json()

# convert the object into a dict
ca_create_dict = ca_create_instance.to_dict()
# create an instance of CaCreate from a dict
ca_create_form_dict = ca_create.from_dict(ca_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


