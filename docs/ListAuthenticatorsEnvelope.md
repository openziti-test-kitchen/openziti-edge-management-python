# ListAuthenticatorsEnvelope


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AuthenticatorDetail]**](AuthenticatorDetail.md) | An array of authenticator resources | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from openziti_edge_management.models.list_authenticators_envelope import ListAuthenticatorsEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ListAuthenticatorsEnvelope from a JSON string
list_authenticators_envelope_instance = ListAuthenticatorsEnvelope.from_json(json)
# print the JSON string representation of the object
print ListAuthenticatorsEnvelope.to_json()

# convert the object into a dict
list_authenticators_envelope_dict = list_authenticators_envelope_instance.to_dict()
# create an instance of ListAuthenticatorsEnvelope from a dict
list_authenticators_envelope_form_dict = list_authenticators_envelope.from_dict(list_authenticators_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


