# PostureCheckDomainUpdate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domains** | **List[str]** |  | 

## Example

```python
from openziti_edge_management.models.posture_check_domain_update import PostureCheckDomainUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of PostureCheckDomainUpdate from a JSON string
posture_check_domain_update_instance = PostureCheckDomainUpdate.from_json(json)
# print the JSON string representation of the object
print PostureCheckDomainUpdate.to_json()

# convert the object into a dict
posture_check_domain_update_dict = posture_check_domain_update_instance.to_dict()
# create an instance of PostureCheckDomainUpdate from a dict
posture_check_domain_update_form_dict = posture_check_domain_update.from_dict(posture_check_domain_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


