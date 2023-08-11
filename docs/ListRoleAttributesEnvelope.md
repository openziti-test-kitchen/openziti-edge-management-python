# ListRoleAttributesEnvelope


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **List[str]** | An array of role attributes | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openziti_edge_management.models.list_role_attributes_envelope import ListRoleAttributesEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ListRoleAttributesEnvelope from a JSON string
list_role_attributes_envelope_instance = ListRoleAttributesEnvelope.from_json(json)
# print the JSON string representation of the object
print ListRoleAttributesEnvelope.to_json()

# convert the object into a dict
list_role_attributes_envelope_dict = list_role_attributes_envelope_instance.to_dict()
# create an instance of ListRoleAttributesEnvelope from a dict
list_role_attributes_envelope_form_dict = list_role_attributes_envelope.from_dict(list_role_attributes_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


