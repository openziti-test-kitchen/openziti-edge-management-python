# AuthPolicyPrimaryUpdb


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed** | **bool** |  | 
**lockout_duration_minutes** | **int** |  | 
**max_attempts** | **int** |  | 
**min_password_length** | **int** |  | 
**require_mixed_case** | **bool** |  | 
**require_number_char** | **bool** |  | 
**require_special_char** | **bool** |  | 

## Example

```python
from openziti_edge_management.models.auth_policy_primary_updb import AuthPolicyPrimaryUpdb

# TODO update the JSON string below
json = "{}"
# create an instance of AuthPolicyPrimaryUpdb from a JSON string
auth_policy_primary_updb_instance = AuthPolicyPrimaryUpdb.from_json(json)
# print the JSON string representation of the object
print AuthPolicyPrimaryUpdb.to_json()

# convert the object into a dict
auth_policy_primary_updb_dict = auth_policy_primary_updb_instance.to_dict()
# create an instance of AuthPolicyPrimaryUpdb from a dict
auth_policy_primary_updb_form_dict = auth_policy_primary_updb.from_dict(auth_policy_primary_updb_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


