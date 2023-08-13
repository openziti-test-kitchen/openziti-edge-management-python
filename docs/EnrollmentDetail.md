# EnrollmentDetail

An enrollment object. Enrollments are tied to identities and potentially a CA. Depending on the method, different fields are utilized. For example ottca enrollments use the `ca` field and updb enrollments use the username field, but not vice versa. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Links**](Links.md) |  | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**updated_at** | **datetime** |  | 
**expires_at** | **datetime** |  | 
**method** | **str** |  | 
**token** | **str** |  | 
**tags** | [**Tags**](Tags.md) |  | [optional] 
**ca_id** | **str, none_type** |  | [optional] 
**edge_router** | [**EntityRef**](EntityRef.md) |  | [optional] 
**edge_router_id** | **str** |  | [optional] 
**identity** | [**EntityRef**](EntityRef.md) |  | [optional] 
**identity_id** | **str** |  | [optional] 
**jwt** | **str** |  | [optional] 
**transit_router** | [**EntityRef**](EntityRef.md) |  | [optional] 
**transit_router_id** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


