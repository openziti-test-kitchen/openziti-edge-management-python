# IdentityCreate

An identity to create

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_data** | [**Tags**](Tags.md) |  | [optional] 
**auth_policy_id** | **str** |  | [optional] 
**default_hosting_cost** | **int** |  | [optional] 
**default_hosting_precedence** | [**TerminatorPrecedence**](TerminatorPrecedence.md) |  | [optional] 
**enrollment** | [**IdentityCreateEnrollment**](IdentityCreateEnrollment.md) |  | [optional] 
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
from openziti_edge_management.models.identity_create import IdentityCreate

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityCreate from a JSON string
identity_create_instance = IdentityCreate.from_json(json)
# print the JSON string representation of the object
print IdentityCreate.to_json()

# convert the object into a dict
identity_create_dict = identity_create_instance.to_dict()
# create an instance of IdentityCreate from a dict
identity_create_form_dict = identity_create.from_dict(identity_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


