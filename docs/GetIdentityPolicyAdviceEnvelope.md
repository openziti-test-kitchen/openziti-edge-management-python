# GetIdentityPolicyAdviceEnvelope


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PolicyAdvice**](PolicyAdvice.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openziti_edge_management.models.get_identity_policy_advice_envelope import GetIdentityPolicyAdviceEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of GetIdentityPolicyAdviceEnvelope from a JSON string
get_identity_policy_advice_envelope_instance = GetIdentityPolicyAdviceEnvelope.from_json(json)
# print the JSON string representation of the object
print GetIdentityPolicyAdviceEnvelope.to_json()

# convert the object into a dict
get_identity_policy_advice_envelope_dict = get_identity_policy_advice_envelope_instance.to_dict()
# create an instance of GetIdentityPolicyAdviceEnvelope from a dict
get_identity_policy_advice_envelope_form_dict = get_identity_policy_advice_envelope.from_dict(get_identity_policy_advice_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


