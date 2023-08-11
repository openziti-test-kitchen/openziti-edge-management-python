# PostureCheckDomainCreate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domains** | **List[str]** |  | 

## Example

```python
from openziti_edge_management.models.posture_check_domain_create import PostureCheckDomainCreate

# TODO update the JSON string below
json = "{}"
# create an instance of PostureCheckDomainCreate from a JSON string
posture_check_domain_create_instance = PostureCheckDomainCreate.from_json(json)
# print the JSON string representation of the object
print PostureCheckDomainCreate.to_json()

# convert the object into a dict
posture_check_domain_create_dict = posture_check_domain_create_instance.to_dict()
# create an instance of PostureCheckDomainCreate from a dict
posture_check_domain_create_form_dict = posture_check_domain_create.from_dict(posture_check_domain_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


