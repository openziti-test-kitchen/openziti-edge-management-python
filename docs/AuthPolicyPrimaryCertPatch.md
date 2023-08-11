# AuthPolicyPrimaryCertPatch


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_expired_certs** | **bool** |  | [optional] 
**allowed** | **bool** |  | [optional] 

## Example

```python
from openziti_edge_management.models.auth_policy_primary_cert_patch import AuthPolicyPrimaryCertPatch

# TODO update the JSON string below
json = "{}"
# create an instance of AuthPolicyPrimaryCertPatch from a JSON string
auth_policy_primary_cert_patch_instance = AuthPolicyPrimaryCertPatch.from_json(json)
# print the JSON string representation of the object
print AuthPolicyPrimaryCertPatch.to_json()

# convert the object into a dict
auth_policy_primary_cert_patch_dict = auth_policy_primary_cert_patch_instance.to_dict()
# create an instance of AuthPolicyPrimaryCertPatch from a dict
auth_policy_primary_cert_patch_form_dict = auth_policy_primary_cert_patch.from_dict(auth_policy_primary_cert_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


