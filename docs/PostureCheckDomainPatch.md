# PostureCheckDomainPatch


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domains** | **List[str]** |  | [optional] 

## Example

```python
from openziti_edge_management.models.posture_check_domain_patch import PostureCheckDomainPatch

# TODO update the JSON string below
json = "{}"
# create an instance of PostureCheckDomainPatch from a JSON string
posture_check_domain_patch_instance = PostureCheckDomainPatch.from_json(json)
# print the JSON string representation of the object
print PostureCheckDomainPatch.to_json()

# convert the object into a dict
posture_check_domain_patch_dict = posture_check_domain_patch_instance.to_dict()
# create an instance of PostureCheckDomainPatch from a dict
posture_check_domain_patch_form_dict = posture_check_domain_patch.from_dict(posture_check_domain_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


