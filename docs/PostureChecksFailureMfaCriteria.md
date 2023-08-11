# PostureChecksFailureMfaCriteria


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**passed_mfa_at** | **datetime** |  | 
**timeout_remaining_seconds** | **int** |  | 
**timeout_seconds** | **int** |  | 
**unlocked_at** | **datetime** |  | 
**woken_at** | **datetime** |  | 

## Example

```python
from openziti_edge_management.models.posture_checks_failure_mfa_criteria import PostureChecksFailureMfaCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of PostureChecksFailureMfaCriteria from a JSON string
posture_checks_failure_mfa_criteria_instance = PostureChecksFailureMfaCriteria.from_json(json)
# print the JSON string representation of the object
print PostureChecksFailureMfaCriteria.to_json()

# convert the object into a dict
posture_checks_failure_mfa_criteria_dict = posture_checks_failure_mfa_criteria_instance.to_dict()
# create an instance of PostureChecksFailureMfaCriteria from a dict
posture_checks_failure_mfa_criteria_form_dict = posture_checks_failure_mfa_criteria.from_dict(posture_checks_failure_mfa_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


