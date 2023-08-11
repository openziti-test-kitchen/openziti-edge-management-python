# ListAuthPoliciesEnvelope


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AuthPolicyDetail]**](AuthPolicyDetail.md) | An array of Auth Policies resources | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openziti_edge_management.models.list_auth_policies_envelope import ListAuthPoliciesEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ListAuthPoliciesEnvelope from a JSON string
list_auth_policies_envelope_instance = ListAuthPoliciesEnvelope.from_json(json)
# print the JSON string representation of the object
print ListAuthPoliciesEnvelope.to_json()

# convert the object into a dict
list_auth_policies_envelope_dict = list_auth_policies_envelope_instance.to_dict()
# create an instance of ListAuthPoliciesEnvelope from a dict
list_auth_policies_envelope_form_dict = list_auth_policies_envelope.from_dict(list_auth_policies_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


