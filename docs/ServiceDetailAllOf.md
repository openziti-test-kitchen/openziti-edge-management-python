# ServiceDetailAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **{str: ({str: (bool, date, datetime, dict, float, int, list, str, none_type,)},)}** | map of config data for this service keyed by the config type name. Only configs of the types requested will be returned. | 
**configs** | **[str]** |  | 
**encryption_required** | **bool** | Describes whether connections must support end-to-end encryption on both sides of the connection. Read-only property, set at create. | 
**name** | **str** |  | 
**permissions** | [**DialBindArray**](DialBindArray.md) |  | 
**posture_queries** | [**[PostureQueries]**](PostureQueries.md) |  | 
**role_attributes** | [**Attributes**](Attributes.md) |  | 
**terminator_strategy** | **str** |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


