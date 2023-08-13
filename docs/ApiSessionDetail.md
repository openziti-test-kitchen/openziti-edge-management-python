# ApiSessionDetail

An API Session object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Links**](Links.md) |  | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**updated_at** | **datetime** |  | 
**auth_queries** | [**AuthQueryList**](AuthQueryList.md) |  | 
**authenticator_id** | **str** |  | 
**config_types** | **[str]** |  | 
**identity** | [**EntityRef**](EntityRef.md) |  | 
**identity_id** | **str** |  | 
**ip_address** | **str** |  | 
**is_mfa_complete** | **bool** |  | 
**is_mfa_required** | **bool** |  | 
**token** | **str** |  | 
**tags** | [**Tags**](Tags.md) |  | [optional] 
**cached_last_activity_at** | **datetime** |  | [optional] 
**last_activity_at** | **datetime** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


