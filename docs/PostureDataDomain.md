# PostureDataDomain


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_updated_at** | **datetime** |  | 
**posture_check_id** | **str** |  | 
**timed_out** | **bool** |  | 
**domain** | **str** |  | 

## Example

```python
from openziti_edge_management.models.posture_data_domain import PostureDataDomain

# TODO update the JSON string below
json = "{}"
# create an instance of PostureDataDomain from a JSON string
posture_data_domain_instance = PostureDataDomain.from_json(json)
# print the JSON string representation of the object
print PostureDataDomain.to_json()

# convert the object into a dict
posture_data_domain_dict = posture_data_domain_instance.to_dict()
# create an instance of PostureDataDomain from a dict
posture_data_domain_form_dict = posture_data_domain.from_dict(posture_data_domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


