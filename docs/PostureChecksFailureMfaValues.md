# PostureChecksFailureMfaValues


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**passed_mfa** | **bool** |  | [optional] 
**passed_on_unlock** | **bool** |  | [optional] 
**passed_on_wake** | **bool** |  | [optional] 
**timed_out** | **bool** |  | [optional] 

## Example

```python
from openziti_edge_management.models.posture_checks_failure_mfa_values import PostureChecksFailureMfaValues

# TODO update the JSON string below
json = "{}"
# create an instance of PostureChecksFailureMfaValues from a JSON string
posture_checks_failure_mfa_values_instance = PostureChecksFailureMfaValues.from_json(json)
# print the JSON string representation of the object
print PostureChecksFailureMfaValues.to_json()

# convert the object into a dict
posture_checks_failure_mfa_values_dict = posture_checks_failure_mfa_values_instance.to_dict()
# create an instance of PostureChecksFailureMfaValues from a dict
posture_checks_failure_mfa_values_form_dict = posture_checks_failure_mfa_values.from_dict(posture_checks_failure_mfa_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


