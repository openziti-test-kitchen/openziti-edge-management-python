# EnrollmentCreate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ca_id** | **str** |  | [optional] 
**expires_at** | **datetime** |  | 
**identity_id** | **str** |  | 
**method** | **str** |  | 
**username** | **str** |  | [optional] 

## Example

```python
from openziti_edge_management.models.enrollment_create import EnrollmentCreate

# TODO update the JSON string below
json = "{}"
# create an instance of EnrollmentCreate from a JSON string
enrollment_create_instance = EnrollmentCreate.from_json(json)
# print the JSON string representation of the object
print EnrollmentCreate.to_json()

# convert the object into a dict
enrollment_create_dict = enrollment_create_instance.to_dict()
# create an instance of EnrollmentCreate from a dict
enrollment_create_form_dict = enrollment_create.from_dict(enrollment_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


