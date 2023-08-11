# AuthPolicyPrimaryCert


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_expired_certs** | **bool** |  | 
**allowed** | **bool** |  | 

## Example

```python
from openziti_edge_management.models.auth_policy_primary_cert import AuthPolicyPrimaryCert

# TODO update the JSON string below
json = "{}"
# create an instance of AuthPolicyPrimaryCert from a JSON string
auth_policy_primary_cert_instance = AuthPolicyPrimaryCert.from_json(json)
# print the JSON string representation of the object
print AuthPolicyPrimaryCert.to_json()

# convert the object into a dict
auth_policy_primary_cert_dict = auth_policy_primary_cert_instance.to_dict()
# create an instance of AuthPolicyPrimaryCert from a dict
auth_policy_primary_cert_form_dict = auth_policy_primary_cert.from_dict(auth_policy_primary_cert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


