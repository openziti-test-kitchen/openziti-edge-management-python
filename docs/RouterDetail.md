# RouterDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) | A map of named links | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**tags** | [**Tags**](Tags.md) |  | [optional] 
**updated_at** | **datetime** |  | 
**cost** | **int** |  | 
**disabled** | **bool** |  | 
**enrollment_created_at** | **datetime** |  | [optional] 
**enrollment_expires_at** | **datetime** |  | [optional] 
**enrollment_jwt** | **str** |  | [optional] 
**enrollment_token** | **str** |  | [optional] 
**fingerprint** | **str** |  | 
**is_online** | **bool** |  | 
**is_verified** | **bool** |  | 
**name** | **str** |  | 
**no_traversal** | **bool** |  | 
**unverified_cert_pem** | **str** |  | [optional] 
**unverified_fingerprint** | **str** |  | [optional] 

## Example

```python
from openziti_edge_management.models.router_detail import RouterDetail

# TODO update the JSON string below
json = "{}"
# create an instance of RouterDetail from a JSON string
router_detail_instance = RouterDetail.from_json(json)
# print the JSON string representation of the object
print RouterDetail.to_json()

# convert the object into a dict
router_detail_dict = router_detail_instance.to_dict()
# create an instance of RouterDetail from a dict
router_detail_form_dict = router_detail.from_dict(router_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


