# PostureCheckTypeDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) | A map of named links | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**tags** | [**Tags**](Tags.md) |  | [optional] 
**updated_at** | **datetime** |  | 
**name** | **str** |  | 
**operating_systems** | [**List[OperatingSystem]**](OperatingSystem.md) |  | 
**version** | **str** |  | 

## Example

```python
from openziti_edge_management.models.posture_check_type_detail import PostureCheckTypeDetail

# TODO update the JSON string below
json = "{}"
# create an instance of PostureCheckTypeDetail from a JSON string
posture_check_type_detail_instance = PostureCheckTypeDetail.from_json(json)
# print the JSON string representation of the object
print PostureCheckTypeDetail.to_json()

# convert the object into a dict
posture_check_type_detail_dict = posture_check_type_detail_instance.to_dict()
# create an instance of PostureCheckTypeDetail from a dict
posture_check_type_detail_form_dict = posture_check_type_detail.from_dict(posture_check_type_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


