# PostureCheckFailureMfa


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actual_value** | [**PostureChecksFailureMfaValues**](PostureChecksFailureMfaValues.md) |  | 
**criteria** | [**PostureChecksFailureMfaCriteria**](PostureChecksFailureMfaCriteria.md) |  | 
**expected_value** | [**PostureChecksFailureMfaValues**](PostureChecksFailureMfaValues.md) |  | 

## Example

```python
from openziti_edge_management.models.posture_check_failure_mfa import PostureCheckFailureMfa

# TODO update the JSON string below
json = "{}"
# create an instance of PostureCheckFailureMfa from a JSON string
posture_check_failure_mfa_instance = PostureCheckFailureMfa.from_json(json)
# print the JSON string representation of the object
print PostureCheckFailureMfa.to_json()

# convert the object into a dict
posture_check_failure_mfa_dict = posture_check_failure_mfa_instance.to_dict()
# create an instance of PostureCheckFailureMfa from a dict
posture_check_failure_mfa_form_dict = posture_check_failure_mfa.from_dict(posture_check_failure_mfa_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


