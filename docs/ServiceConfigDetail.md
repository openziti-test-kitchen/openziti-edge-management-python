# ServiceConfigDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**EntityRef**](EntityRef.md) |  | 
**config_id** | **str** |  | 
**service** | [**EntityRef**](EntityRef.md) |  | 
**service_id** | **str** |  | 

## Example

```python
from openziti_edge_management.models.service_config_detail import ServiceConfigDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceConfigDetail from a JSON string
service_config_detail_instance = ServiceConfigDetail.from_json(json)
# print the JSON string representation of the object
print ServiceConfigDetail.to_json()

# convert the object into a dict
service_config_detail_dict = service_config_detail_instance.to_dict()
# create an instance of ServiceConfigDetail from a dict
service_config_detail_form_dict = service_config_detail.from_dict(service_config_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


