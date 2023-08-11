# NamedRole


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**role** | **str** |  | [optional] 

## Example

```python
from openziti_edge_management.models.named_role import NamedRole

# TODO update the JSON string below
json = "{}"
# create an instance of NamedRole from a JSON string
named_role_instance = NamedRole.from_json(json)
# print the JSON string representation of the object
print NamedRole.to_json()

# convert the object into a dict
named_role_dict = named_role_instance.to_dict()
# create an instance of NamedRole from a dict
named_role_form_dict = named_role.from_dict(named_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


