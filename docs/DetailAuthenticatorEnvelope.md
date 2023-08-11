# DetailAuthenticatorEnvelope


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AuthenticatorDetail**](AuthenticatorDetail.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openziti_edge_management.models.detail_authenticator_envelope import DetailAuthenticatorEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of DetailAuthenticatorEnvelope from a JSON string
detail_authenticator_envelope_instance = DetailAuthenticatorEnvelope.from_json(json)
# print the JSON string representation of the object
print DetailAuthenticatorEnvelope.to_json()

# convert the object into a dict
detail_authenticator_envelope_dict = detail_authenticator_envelope_instance.to_dict()
# create an instance of DetailAuthenticatorEnvelope from a dict
detail_authenticator_envelope_form_dict = detail_authenticator_envelope.from_dict(detail_authenticator_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


