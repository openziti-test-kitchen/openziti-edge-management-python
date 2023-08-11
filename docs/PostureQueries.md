# PostureQueries


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_passing** | **bool** |  | 
**policy_id** | **str** |  | 
**policy_type** | [**DialBind**](DialBind.md) |  | [optional] 
**posture_queries** | [**List[PostureQuery]**](PostureQuery.md) |  | 

## Example

```python
from openziti_edge_management.models.posture_queries import PostureQueries

# TODO update the JSON string below
json = "{}"
# create an instance of PostureQueries from a JSON string
posture_queries_instance = PostureQueries.from_json(json)
# print the JSON string representation of the object
print PostureQueries.to_json()

# convert the object into a dict
posture_queries_dict = posture_queries_instance.to_dict()
# create an instance of PostureQueries from a dict
posture_queries_form_dict = posture_queries.from_dict(posture_queries_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


