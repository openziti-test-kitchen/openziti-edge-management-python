# IdentityAuthenticators


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cert** | [**IdentityAuthenticatorsCert**](IdentityAuthenticatorsCert.md) |  | [optional] 
**updb** | [**IdentityAuthenticatorsUpdb**](IdentityAuthenticatorsUpdb.md) |  | [optional] 

## Example

```python
from openziti_edge_management.models.identity_authenticators import IdentityAuthenticators

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityAuthenticators from a JSON string
identity_authenticators_instance = IdentityAuthenticators.from_json(json)
# print the JSON string representation of the object
print IdentityAuthenticators.to_json()

# convert the object into a dict
identity_authenticators_dict = identity_authenticators_instance.to_dict()
# create an instance of IdentityAuthenticators from a dict
identity_authenticators_form_dict = identity_authenticators.from_dict(identity_authenticators_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


