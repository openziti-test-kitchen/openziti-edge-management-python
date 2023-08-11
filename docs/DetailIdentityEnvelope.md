# DetailIdentityEnvelope


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**IdentityDetail**](IdentityDetail.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openziti_edge_management.models.detail_identity_envelope import DetailIdentityEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of DetailIdentityEnvelope from a JSON string
detail_identity_envelope_instance = DetailIdentityEnvelope.from_json(json)
# print the JSON string representation of the object
print DetailIdentityEnvelope.to_json()

# convert the object into a dict
detail_identity_envelope_dict = detail_identity_envelope_instance.to_dict()
# create an instance of DetailIdentityEnvelope from a dict
detail_identity_envelope_form_dict = detail_identity_envelope.from_dict(detail_identity_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


