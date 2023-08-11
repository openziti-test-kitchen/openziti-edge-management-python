# ListIdentitiesEnvelope


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[IdentityDetail]**](IdentityDetail.md) | A list of identities | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openziti_edge_management.models.list_identities_envelope import ListIdentitiesEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ListIdentitiesEnvelope from a JSON string
list_identities_envelope_instance = ListIdentitiesEnvelope.from_json(json)
# print the JSON string representation of the object
print ListIdentitiesEnvelope.to_json()

# convert the object into a dict
list_identities_envelope_dict = list_identities_envelope_instance.to_dict()
# create an instance of ListIdentitiesEnvelope from a dict
list_identities_envelope_form_dict = list_identities_envelope.from_dict(list_identities_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


