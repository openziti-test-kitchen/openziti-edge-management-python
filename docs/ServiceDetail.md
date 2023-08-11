# ServiceDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) | A map of named links | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**tags** | [**Tags**](Tags.md) |  | [optional] 
**updated_at** | **datetime** |  | 
**config** | **Dict[str, Dict[str, object]]** | map of config data for this service keyed by the config type name. Only configs of the types requested will be returned. | 
**configs** | **List[str]** |  | 
**encryption_required** | **bool** | Describes whether connections must support end-to-end encryption on both sides of the connection. Read-only property, set at create. | 
**name** | **str** |  | 
**permissions** | [**List[DialBind]**](DialBind.md) |  | 
**posture_queries** | [**List[PostureQueries]**](PostureQueries.md) |  | 
**role_attributes** | **List[str]** | A set of strings used to loosly couple this resource to policies | 
**terminator_strategy** | **str** |  | 

## Example

```python
from openziti_edge_management.models.service_detail import ServiceDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceDetail from a JSON string
service_detail_instance = ServiceDetail.from_json(json)
# print the JSON string representation of the object
print ServiceDetail.to_json()

# convert the object into a dict
service_detail_dict = service_detail_instance.to_dict()
# create an instance of ServiceDetail from a dict
service_detail_form_dict = service_detail.from_dict(service_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


