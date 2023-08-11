# DetailExternalJwtSignerEnvelope


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ExternalJwtSignerDetail**](ExternalJwtSignerDetail.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openziti_edge_management.models.detail_external_jwt_signer_envelope import DetailExternalJwtSignerEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of DetailExternalJwtSignerEnvelope from a JSON string
detail_external_jwt_signer_envelope_instance = DetailExternalJwtSignerEnvelope.from_json(json)
# print the JSON string representation of the object
print DetailExternalJwtSignerEnvelope.to_json()

# convert the object into a dict
detail_external_jwt_signer_envelope_dict = detail_external_jwt_signer_envelope_instance.to_dict()
# create an instance of DetailExternalJwtSignerEnvelope from a dict
detail_external_jwt_signer_envelope_form_dict = detail_external_jwt_signer_envelope.from_dict(detail_external_jwt_signer_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


