# CaDetail

A Certificate Authority (CA) resource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) | A map of named links | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**tags** | [**Tags**](Tags.md) |  | [optional] 
**updated_at** | **datetime** |  | 
**cert_pem** | **str** |  | 
**external_id_claim** | [**ExternalIdClaim**](ExternalIdClaim.md) |  | [optional] 
**fingerprint** | **str** |  | 
**identity_name_format** | **str** |  | 
**identity_roles** | **List[str]** |  | 
**is_auth_enabled** | **bool** |  | 
**is_auto_ca_enrollment_enabled** | **bool** |  | 
**is_ott_ca_enrollment_enabled** | **bool** |  | 
**is_verified** | **bool** |  | 
**name** | **str** |  | 
**verification_token** | **str** |  | [optional] 

## Example

```python
from openziti_edge_management.models.ca_detail import CaDetail

# TODO update the JSON string below
json = "{}"
# create an instance of CaDetail from a JSON string
ca_detail_instance = CaDetail.from_json(json)
# print the JSON string representation of the object
print CaDetail.to_json()

# convert the object into a dict
ca_detail_dict = ca_detail_instance.to_dict()
# create an instance of CaDetail from a dict
ca_detail_form_dict = ca_detail.from_dict(ca_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


