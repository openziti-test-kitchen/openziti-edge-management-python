# ExternalJwtSignerDetail

A External JWT Signer resource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) | A map of named links | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**tags** | [**Tags**](Tags.md) |  | [optional] 
**updated_at** | **datetime** |  | 
**audience** | **str** |  | 
**cert_pem** | **str** |  | 
**claims_property** | **str** |  | 
**common_name** | **str** |  | 
**enabled** | **bool** |  | 
**external_auth_url** | **str** |  | 
**fingerprint** | **str** |  | 
**issuer** | **str** |  | 
**jwks_endpoint** | **str** |  | 
**kid** | **str** |  | 
**name** | **str** |  | 
**not_after** | **datetime** |  | 
**not_before** | **datetime** |  | 
**use_external_id** | **bool** |  | 

## Example

```python
from openziti_edge_management.models.external_jwt_signer_detail import ExternalJwtSignerDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalJwtSignerDetail from a JSON string
external_jwt_signer_detail_instance = ExternalJwtSignerDetail.from_json(json)
# print the JSON string representation of the object
print ExternalJwtSignerDetail.to_json()

# convert the object into a dict
external_jwt_signer_detail_dict = external_jwt_signer_detail_instance.to_dict()
# create an instance of ExternalJwtSignerDetail from a dict
external_jwt_signer_detail_form_dict = external_jwt_signer_detail.from_dict(external_jwt_signer_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


