# PolicyFailure


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checks** | [**List[PostureCheckFailure]**](PostureCheckFailure.md) |  | [optional] 
**policy_id** | **str** |  | [optional] 
**policy_name** | **str** |  | [optional] 

## Example

```python
from openziti_edge_management.models.policy_failure import PolicyFailure

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyFailure from a JSON string
policy_failure_instance = PolicyFailure.from_json(json)
# print the JSON string representation of the object
print PolicyFailure.to_json()

# convert the object into a dict
policy_failure_dict = policy_failure_instance.to_dict()
# create an instance of PolicyFailure from a dict
policy_failure_form_dict = policy_failure.from_dict(policy_failure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


