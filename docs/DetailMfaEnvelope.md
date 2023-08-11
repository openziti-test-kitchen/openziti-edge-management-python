# DetailMfaEnvelope


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DetailMfa**](DetailMfa.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openziti_edge_management.models.detail_mfa_envelope import DetailMfaEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of DetailMfaEnvelope from a JSON string
detail_mfa_envelope_instance = DetailMfaEnvelope.from_json(json)
# print the JSON string representation of the object
print DetailMfaEnvelope.to_json()

# convert the object into a dict
detail_mfa_envelope_dict = detail_mfa_envelope_instance.to_dict()
# create an instance of DetailMfaEnvelope from a dict
detail_mfa_envelope_form_dict = detail_mfa_envelope.from_dict(detail_mfa_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


