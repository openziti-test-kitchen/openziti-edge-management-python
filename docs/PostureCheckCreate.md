# PostureCheckCreate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**role_attributes** | **List[str]** | A set of strings used to loosly couple this resource to policies | [optional] 
**tags** | [**Tags**](Tags.md) |  | [optional] 
**type_id** | [**PostureCheckType**](PostureCheckType.md) |  | 

## Example

```python
from openziti_edge_management.models.posture_check_create import PostureCheckCreate

# TODO update the JSON string below
json = "{}"
# create an instance of PostureCheckCreate from a JSON string
posture_check_create_instance = PostureCheckCreate.from_json(json)
# print the JSON string representation of the object
print PostureCheckCreate.to_json()

# convert the object into a dict
posture_check_create_dict = posture_check_create_instance.to_dict()
# create an instance of PostureCheckCreate from a dict
posture_check_create_form_dict = posture_check_create.from_dict(posture_check_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


