# PostureCheckDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) | A map of named links | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**name** | **str** |  | 
**role_attributes** | **List[str]** | A set of strings used to loosly couple this resource to policies | 
**tags** | [**Tags**](Tags.md) |  | 
**type_id** | **str** |  | 
**updated_at** | **datetime** |  | 
**version** | **int** |  | 

## Example

```python
from openziti_edge_management.models.posture_check_detail import PostureCheckDetail

# TODO update the JSON string below
json = "{}"
# create an instance of PostureCheckDetail from a JSON string
posture_check_detail_instance = PostureCheckDetail.from_json(json)
# print the JSON string representation of the object
print PostureCheckDetail.to_json()

# convert the object into a dict
posture_check_detail_dict = posture_check_detail_instance.to_dict()
# create an instance of PostureCheckDetail from a dict
posture_check_detail_form_dict = posture_check_detail.from_dict(posture_check_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


