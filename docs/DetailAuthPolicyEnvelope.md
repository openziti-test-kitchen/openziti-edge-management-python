# DetailAuthPolicyEnvelope


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AuthPolicyDetail**](AuthPolicyDetail.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openziti_edge_management.models.detail_auth_policy_envelope import DetailAuthPolicyEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of DetailAuthPolicyEnvelope from a JSON string
detail_auth_policy_envelope_instance = DetailAuthPolicyEnvelope.from_json(json)
# print the JSON string representation of the object
print DetailAuthPolicyEnvelope.to_json()

# convert the object into a dict
detail_auth_policy_envelope_dict = detail_auth_policy_envelope_instance.to_dict()
# create an instance of DetailAuthPolicyEnvelope from a dict
detail_auth_policy_envelope_form_dict = detail_auth_policy_envelope.from_dict(detail_auth_policy_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


