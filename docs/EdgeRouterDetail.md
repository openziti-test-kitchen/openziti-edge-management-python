# EdgeRouterDetail

A detail edge router resource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) | A map of named links | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**tags** | [**Tags**](Tags.md) |  | [optional] 
**updated_at** | **datetime** |  | 
**app_data** | [**Tags**](Tags.md) |  | [optional] 
**cost** | **int** |  | 
**disabled** | **bool** |  | 
**hostname** | **str** |  | 
**is_online** | **bool** |  | 
**name** | **str** |  | 
**no_traversal** | **bool** |  | 
**supported_protocols** | **Dict[str, str]** |  | 
**sync_status** | **str** |  | 
**cert_pem** | **str** |  | [optional] 
**enrollment_created_at** | **datetime** |  | [optional] 
**enrollment_expires_at** | **datetime** |  | [optional] 
**enrollment_jwt** | **str** |  | [optional] 
**enrollment_token** | **str** |  | [optional] 
**fingerprint** | **str** |  | [optional] 
**is_tunneler_enabled** | **bool** |  | 
**is_verified** | **bool** |  | 
**role_attributes** | **List[str]** | A set of strings used to loosly couple this resource to policies | 
**unverified_cert_pem** | **str** |  | [optional] 
**unverified_fingerprint** | **str** |  | [optional] 
**version_info** | [**VersionInfo**](VersionInfo.md) |  | [optional] 

## Example

```python
from openziti_edge_management.models.edge_router_detail import EdgeRouterDetail

# TODO update the JSON string below
json = "{}"
# create an instance of EdgeRouterDetail from a JSON string
edge_router_detail_instance = EdgeRouterDetail.from_json(json)
# print the JSON string representation of the object
print EdgeRouterDetail.to_json()

# convert the object into a dict
edge_router_detail_dict = edge_router_detail_instance.to_dict()
# create an instance of EdgeRouterDetail from a dict
edge_router_detail_form_dict = edge_router_detail.from_dict(edge_router_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


