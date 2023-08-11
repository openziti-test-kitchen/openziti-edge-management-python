# SessionManagementDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) | A map of named links | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**tags** | [**Tags**](Tags.md) |  | [optional] 
**updated_at** | **datetime** |  | 
**api_session** | [**EntityRef**](EntityRef.md) |  | 
**api_session_id** | **str** |  | 
**edge_routers** | [**List[SessionEdgeRouter]**](SessionEdgeRouter.md) |  | 
**identity_id** | **str** |  | 
**service** | [**EntityRef**](EntityRef.md) |  | 
**service_id** | **str** |  | 
**token** | **str** |  | 
**type** | [**DialBind**](DialBind.md) |  | 
**service_policies** | [**List[EntityRef]**](EntityRef.md) |  | [optional] 

## Example

```python
from openziti_edge_management.models.session_management_detail import SessionManagementDetail

# TODO update the JSON string below
json = "{}"
# create an instance of SessionManagementDetail from a JSON string
session_management_detail_instance = SessionManagementDetail.from_json(json)
# print the JSON string representation of the object
print SessionManagementDetail.to_json()

# convert the object into a dict
session_management_detail_dict = session_management_detail_instance.to_dict()
# create an instance of SessionManagementDetail from a dict
session_management_detail_form_dict = session_management_detail.from_dict(session_management_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


