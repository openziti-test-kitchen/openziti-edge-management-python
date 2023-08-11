# AuthenticatorDetail

A singular authenticator resource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) | A map of named links | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**tags** | [**Tags**](Tags.md) |  | [optional] 
**updated_at** | **datetime** |  | 
**cert_pem** | **str** |  | [optional] 
**fingerprint** | **str** |  | [optional] 
**identity** | [**EntityRef**](EntityRef.md) |  | 
**identity_id** | **str** |  | 
**method** | **str** |  | 
**username** | **str** |  | [optional] 

## Example

```python
from openziti_edge_management.models.authenticator_detail import AuthenticatorDetail

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorDetail from a JSON string
authenticator_detail_instance = AuthenticatorDetail.from_json(json)
# print the JSON string representation of the object
print AuthenticatorDetail.to_json()

# convert the object into a dict
authenticator_detail_dict = authenticator_detail_instance.to_dict()
# create an instance of AuthenticatorDetail from a dict
authenticator_detail_form_dict = authenticator_detail.from_dict(authenticator_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


