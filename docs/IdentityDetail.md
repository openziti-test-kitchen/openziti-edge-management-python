# IdentityDetail

Detail of a specific identity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) | A map of named links | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**tags** | [**Tags**](Tags.md) |  | [optional] 
**updated_at** | **datetime** |  | 
**app_data** | [**Tags**](Tags.md) |  | [optional] 
**auth_policy** | [**EntityRef**](EntityRef.md) |  | 
**auth_policy_id** | **str** |  | 
**authenticators** | [**IdentityAuthenticators**](IdentityAuthenticators.md) |  | 
**default_hosting_cost** | **int** |  | 
**default_hosting_precedence** | [**TerminatorPrecedence**](TerminatorPrecedence.md) |  | [optional] 
**disabled** | **bool** |  | 
**disabled_at** | **datetime** |  | [optional] 
**disabled_until** | **datetime** |  | [optional] 
**enrollment** | [**IdentityEnrollments**](IdentityEnrollments.md) |  | 
**env_info** | [**EnvInfo**](EnvInfo.md) |  | 
**external_id** | **str** |  | 
**has_api_session** | **bool** |  | 
**has_edge_router_connection** | **bool** |  | 
**is_admin** | **bool** |  | 
**is_default_admin** | **bool** |  | 
**is_mfa_enabled** | **bool** |  | 
**name** | **str** |  | 
**role_attributes** | **List[str]** | A set of strings used to loosly couple this resource to policies | 
**sdk_info** | [**SdkInfo**](SdkInfo.md) |  | 
**service_hosting_costs** | **Dict[str, int]** |  | 
**service_hosting_precedences** | [**Dict[str, TerminatorPrecedence]**](TerminatorPrecedence.md) |  | 
**type** | [**EntityRef**](EntityRef.md) |  | 
**type_id** | **str** |  | 

## Example

```python
from openziti_edge_management.models.identity_detail import IdentityDetail

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityDetail from a JSON string
identity_detail_instance = IdentityDetail.from_json(json)
# print the JSON string representation of the object
print IdentityDetail.to_json()

# convert the object into a dict
identity_detail_dict = identity_detail_instance.to_dict()
# create an instance of IdentityDetail from a dict
identity_detail_form_dict = identity_detail.from_dict(identity_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


