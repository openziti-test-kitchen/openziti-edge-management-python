# PostureCheckDomainDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domains** | **List[str]** |  | 

## Example

```python
from openziti_edge_management.models.posture_check_domain_detail import PostureCheckDomainDetail

# TODO update the JSON string below
json = "{}"
# create an instance of PostureCheckDomainDetail from a JSON string
posture_check_domain_detail_instance = PostureCheckDomainDetail.from_json(json)
# print the JSON string representation of the object
print PostureCheckDomainDetail.to_json()

# convert the object into a dict
posture_check_domain_detail_dict = posture_check_domain_detail_instance.to_dict()
# create an instance of PostureCheckDomainDetail from a dict
posture_check_domain_detail_form_dict = posture_check_domain_detail.from_dict(posture_check_domain_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


