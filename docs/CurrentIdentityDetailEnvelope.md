# CurrentIdentityDetailEnvelope


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**IdentityDetail**](IdentityDetail.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openziti_edge_management.models.current_identity_detail_envelope import CurrentIdentityDetailEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of CurrentIdentityDetailEnvelope from a JSON string
current_identity_detail_envelope_instance = CurrentIdentityDetailEnvelope.from_json(json)
# print the JSON string representation of the object
print CurrentIdentityDetailEnvelope.to_json()

# convert the object into a dict
current_identity_detail_envelope_dict = current_identity_detail_envelope_instance.to_dict()
# create an instance of CurrentIdentityDetailEnvelope from a dict
current_identity_detail_envelope_form_dict = current_identity_detail_envelope.from_dict(current_identity_detail_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


