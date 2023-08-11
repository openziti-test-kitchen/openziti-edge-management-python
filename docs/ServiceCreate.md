# ServiceCreate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configs** | **List[str]** |  | [optional] 
**encryption_required** | **bool** | Describes whether connections must support end-to-end encryption on both sides of the connection. | 
**name** | **str** |  | 
**role_attributes** | **List[str]** |  | [optional] 
**tags** | [**Tags**](Tags.md) |  | [optional] 
**terminator_strategy** | **str** |  | [optional] 

## Example

```python
from openziti_edge_management.models.service_create import ServiceCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCreate from a JSON string
service_create_instance = ServiceCreate.from_json(json)
# print the JSON string representation of the object
print ServiceCreate.to_json()

# convert the object into a dict
service_create_dict = service_create_instance.to_dict()
# create an instance of ServiceCreate from a dict
service_create_form_dict = service_create.from_dict(service_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


