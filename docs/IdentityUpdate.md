# IdentityUpdate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_data** | [**Tags**](Tags.md) |  | [optional] 
**auth_policy_id** | **str** |  | [optional] 
**default_hosting_cost** | **int** |  | [optional] 
**default_hosting_precedence** | [**TerminatorPrecedence**](TerminatorPrecedence.md) |  | [optional] 
**external_id** | **str** |  | [optional] 
**is_admin** | **bool** |  | 
**name** | **str** |  | 
**role_attributes** | **List[str]** | A set of strings used to loosly couple this resource to policies | [optional] 
**service_hosting_costs** | **Dict[str, int]** |  | [optional] 
**service_hosting_precedences** | [**Dict[str, TerminatorPrecedence]**](TerminatorPrecedence.md) |  | [optional] 
**tags** | [**Tags**](Tags.md) |  | [optional] 
**type** | [**IdentityType**](IdentityType.md) |  | 

## Example

```python
from openziti_edge_management.models.identity_update import IdentityUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityUpdate from a JSON string
identity_update_instance = IdentityUpdate.from_json(json)
# print the JSON string representation of the object
print IdentityUpdate.to_json()

# convert the object into a dict
identity_update_dict = identity_update_instance.to_dict()
# create an instance of IdentityUpdate from a dict
identity_update_form_dict = identity_update.from_dict(identity_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


