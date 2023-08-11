# ServiceConfigAssign


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_id** | **str** |  | 
**service_id** | **str** |  | 

## Example

```python
from openziti_edge_management.models.service_config_assign import ServiceConfigAssign

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceConfigAssign from a JSON string
service_config_assign_instance = ServiceConfigAssign.from_json(json)
# print the JSON string representation of the object
print ServiceConfigAssign.to_json()

# convert the object into a dict
service_config_assign_dict = service_config_assign_instance.to_dict()
# create an instance of ServiceConfigAssign from a dict
service_config_assign_form_dict = service_config_assign.from_dict(service_config_assign_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


