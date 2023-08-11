# ServicePatch


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configs** | **List[str]** |  | [optional] 
**encryption_required** | **bool** | Describes whether connections must support end-to-end encryption on both sides of the connection. Read-only property, set at create. | [optional] 
**name** | **str** |  | [optional] 
**role_attributes** | **List[str]** |  | [optional] 
**tags** | [**Tags**](Tags.md) |  | [optional] 
**terminator_strategy** | **str** |  | [optional] 

## Example

```python
from openziti_edge_management.models.service_patch import ServicePatch

# TODO update the JSON string below
json = "{}"
# create an instance of ServicePatch from a JSON string
service_patch_instance = ServicePatch.from_json(json)
# print the JSON string representation of the object
print ServicePatch.to_json()

# convert the object into a dict
service_patch_dict = service_patch_instance.to_dict()
# create an instance of ServicePatch from a dict
service_patch_form_dict = service_patch.from_dict(service_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


