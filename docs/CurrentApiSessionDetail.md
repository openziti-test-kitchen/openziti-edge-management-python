# CurrentApiSessionDetail

An API Session object for the current API session

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) | A map of named links | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**tags** | [**Tags**](Tags.md) |  | [optional] 
**updated_at** | **datetime** |  | 
**auth_queries** | [**List[AuthQueryDetail]**](AuthQueryDetail.md) |  | 
**authenticator_id** | **str** |  | 
**cached_last_activity_at** | **datetime** |  | [optional] 
**config_types** | **List[str]** |  | 
**identity** | [**EntityRef**](EntityRef.md) |  | 
**identity_id** | **str** |  | 
**ip_address** | **str** |  | 
**is_mfa_complete** | **bool** |  | 
**is_mfa_required** | **bool** |  | 
**last_activity_at** | **datetime** |  | [optional] 
**token** | **str** |  | 
**expiration_seconds** | **int** |  | 
**expires_at** | **datetime** |  | 

## Example

```python
from openziti_edge_management.models.current_api_session_detail import CurrentApiSessionDetail

# TODO update the JSON string below
json = "{}"
# create an instance of CurrentApiSessionDetail from a JSON string
current_api_session_detail_instance = CurrentApiSessionDetail.from_json(json)
# print the JSON string representation of the object
print CurrentApiSessionDetail.to_json()

# convert the object into a dict
current_api_session_detail_dict = current_api_session_detail_instance.to_dict()
# create an instance of CurrentApiSessionDetail from a dict
current_api_session_detail_form_dict = current_api_session_detail.from_dict(current_api_session_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


