# ListExternalJwtSignersEnvelope


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ExternalJwtSignerDetail]**](ExternalJwtSignerDetail.md) | An array of External JWT Signers resources | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openziti_edge_management.models.list_external_jwt_signers_envelope import ListExternalJwtSignersEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ListExternalJwtSignersEnvelope from a JSON string
list_external_jwt_signers_envelope_instance = ListExternalJwtSignersEnvelope.from_json(json)
# print the JSON string representation of the object
print ListExternalJwtSignersEnvelope.to_json()

# convert the object into a dict
list_external_jwt_signers_envelope_dict = list_external_jwt_signers_envelope_instance.to_dict()
# create an instance of ListExternalJwtSignersEnvelope from a dict
list_external_jwt_signers_envelope_form_dict = list_external_jwt_signers_envelope.from_dict(list_external_jwt_signers_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


