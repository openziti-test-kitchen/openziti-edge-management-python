# DetailIdentityTypeEnvelope


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**IdentityTypeDetail**](IdentityTypeDetail.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openziti_edge_management.models.detail_identity_type_envelope import DetailIdentityTypeEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of DetailIdentityTypeEnvelope from a JSON string
detail_identity_type_envelope_instance = DetailIdentityTypeEnvelope.from_json(json)
# print the JSON string representation of the object
print DetailIdentityTypeEnvelope.to_json()

# convert the object into a dict
detail_identity_type_envelope_dict = detail_identity_type_envelope_instance.to_dict()
# create an instance of DetailIdentityTypeEnvelope from a dict
detail_identity_type_envelope_form_dict = detail_identity_type_envelope.from_dict(detail_identity_type_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


