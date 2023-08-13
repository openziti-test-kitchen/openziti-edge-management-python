# IdentityDetail

Detail of a specific identity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Links**](Links.md) |  | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**updated_at** | **datetime** |  | 
**auth_policy** | [**EntityRef**](EntityRef.md) |  | 
**auth_policy_id** | **str** |  | 
**authenticators** | [**IdentityAuthenticators**](IdentityAuthenticators.md) |  | 
**default_hosting_cost** | [**TerminatorCost**](TerminatorCost.md) |  | 
**disabled** | **bool** |  | 
**enrollment** | [**IdentityEnrollments**](IdentityEnrollments.md) |  | 
**env_info** | [**EnvInfo**](EnvInfo.md) |  | 
**external_id** | **str, none_type** |  | 
**has_api_session** | **bool** |  | 
**has_edge_router_connection** | **bool** |  | 
**is_admin** | **bool** |  | 
**is_default_admin** | **bool** |  | 
**is_mfa_enabled** | **bool** |  | 
**name** | **str** |  | 
**role_attributes** | [**Attributes**](Attributes.md) |  | 
**sdk_info** | [**SdkInfo**](SdkInfo.md) |  | 
**service_hosting_costs** | [**TerminatorCostMap**](TerminatorCostMap.md) |  | 
**service_hosting_precedences** | [**TerminatorPrecedenceMap**](TerminatorPrecedenceMap.md) |  | 
**type** | [**EntityRef**](EntityRef.md) |  | 
**type_id** | **str** |  | 
**tags** | [**Tags**](Tags.md) |  | [optional] 
**app_data** | [**Tags**](Tags.md) |  | [optional] 
**default_hosting_precedence** | [**TerminatorPrecedence**](TerminatorPrecedence.md) |  | [optional] 
**disabled_at** | **datetime, none_type** |  | [optional] 
**disabled_until** | **datetime, none_type** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


