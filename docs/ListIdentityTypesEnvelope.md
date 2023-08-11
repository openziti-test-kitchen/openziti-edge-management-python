# ListIdentityTypesEnvelope


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[IdentityTypeDetail]**](IdentityTypeDetail.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openziti_edge_management.models.list_identity_types_envelope import ListIdentityTypesEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ListIdentityTypesEnvelope from a JSON string
list_identity_types_envelope_instance = ListIdentityTypesEnvelope.from_json(json)
# print the JSON string representation of the object
print ListIdentityTypesEnvelope.to_json()

# convert the object into a dict
list_identity_types_envelope_dict = list_identity_types_envelope_instance.to_dict()
# create an instance of ListIdentityTypesEnvelope from a dict
list_identity_types_envelope_form_dict = list_identity_types_envelope.from_dict(list_identity_types_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


