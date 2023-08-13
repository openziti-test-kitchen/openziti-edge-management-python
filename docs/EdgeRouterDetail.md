# EdgeRouterDetail

A detail edge router resource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Links**](Links.md) |  | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**updated_at** | **datetime** |  | 
**cost** | **int, none_type** |  | 
**disabled** | **bool** |  | 
**hostname** | **str** |  | 
**is_online** | **bool** |  | 
**name** | **str** |  | 
**no_traversal** | **bool, none_type** |  | 
**supported_protocols** | **{str: (str,)}** |  | 
**sync_status** | **str** |  | 
**is_tunneler_enabled** | **bool** |  | 
**is_verified** | **bool** |  | 
**role_attributes** | [**Attributes**](Attributes.md) |  | 
**tags** | [**Tags**](Tags.md) |  | [optional] 
**app_data** | [**Tags**](Tags.md) |  | [optional] 
**cert_pem** | **str, none_type** |  | [optional] 
**enrollment_created_at** | **datetime, none_type** |  | [optional] 
**enrollment_expires_at** | **datetime, none_type** |  | [optional] 
**enrollment_jwt** | **str, none_type** |  | [optional] 
**enrollment_token** | **str, none_type** |  | [optional] 
**fingerprint** | **str** |  | [optional] 
**unverified_cert_pem** | **str, none_type** |  | [optional] 
**unverified_fingerprint** | **str, none_type** |  | [optional] 
**version_info** | [**VersionInfo**](VersionInfo.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


