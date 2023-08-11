# IdentityAuthenticatorsCert


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fingerprint** | **str** |  | [optional] 
**id** | **str** |  | [optional] 

## Example

```python
from openziti_edge_management.models.identity_authenticators_cert import IdentityAuthenticatorsCert

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityAuthenticatorsCert from a JSON string
identity_authenticators_cert_instance = IdentityAuthenticatorsCert.from_json(json)
# print the JSON string representation of the object
print IdentityAuthenticatorsCert.to_json()

# convert the object into a dict
identity_authenticators_cert_dict = identity_authenticators_cert_instance.to_dict()
# create an instance of IdentityAuthenticatorsCert from a dict
identity_authenticators_cert_form_dict = identity_authenticators_cert.from_dict(identity_authenticators_cert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


