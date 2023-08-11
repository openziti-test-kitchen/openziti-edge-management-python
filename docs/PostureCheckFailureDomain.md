# PostureCheckFailureDomain


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actual_value** | **str** |  | 
**expected_value** | **List[str]** |  | 

## Example

```python
from openziti_edge_management.models.posture_check_failure_domain import PostureCheckFailureDomain

# TODO update the JSON string below
json = "{}"
# create an instance of PostureCheckFailureDomain from a JSON string
posture_check_failure_domain_instance = PostureCheckFailureDomain.from_json(json)
# print the JSON string representation of the object
print PostureCheckFailureDomain.to_json()

# convert the object into a dict
posture_check_failure_domain_dict = posture_check_failure_domain_instance.to_dict()
# create an instance of PostureCheckFailureDomain from a dict
posture_check_failure_domain_form_dict = posture_check_failure_domain.from_dict(posture_check_failure_domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


