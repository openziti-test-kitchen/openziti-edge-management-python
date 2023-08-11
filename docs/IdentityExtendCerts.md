# IdentityExtendCerts


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ca** | **str** | A PEM encoded set of CA certificates | [optional] 
**client_cert** | **str** | A PEM encoded client certificate | [optional] 

## Example

```python
from openziti_edge_management.models.identity_extend_certs import IdentityExtendCerts

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityExtendCerts from a JSON string
identity_extend_certs_instance = IdentityExtendCerts.from_json(json)
# print the JSON string representation of the object
print IdentityExtendCerts.to_json()

# convert the object into a dict
identity_extend_certs_dict = identity_extend_certs_instance.to_dict()
# create an instance of IdentityExtendCerts from a dict
identity_extend_certs_form_dict = identity_extend_certs.from_dict(identity_extend_certs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


