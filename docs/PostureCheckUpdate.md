# PostureCheckUpdate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**role_attributes** | **List[str]** | A set of strings used to loosly couple this resource to policies | [optional] 
**tags** | [**Tags**](Tags.md) |  | [optional] 
**type_id** | [**PostureCheckType**](PostureCheckType.md) |  | [optional] 

## Example

```python
from openziti_edge_management.models.posture_check_update import PostureCheckUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of PostureCheckUpdate from a JSON string
posture_check_update_instance = PostureCheckUpdate.from_json(json)
# print the JSON string representation of the object
print PostureCheckUpdate.to_json()

# convert the object into a dict
posture_check_update_dict = posture_check_update_instance.to_dict()
# create an instance of PostureCheckUpdate from a dict
posture_check_update_form_dict = posture_check_update.from_dict(posture_check_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


