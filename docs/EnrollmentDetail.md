# EnrollmentDetail

An enrollment object. Enrollments are tied to identities and potentially a CA. Depending on the method, different fields are utilized. For example ottca enrollments use the `ca` field and updb enrollments use the username field, but not vice versa. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) | A map of named links | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**tags** | [**Tags**](Tags.md) |  | [optional] 
**updated_at** | **datetime** |  | 
**ca_id** | **str** |  | [optional] 
**edge_router** | [**EntityRef**](EntityRef.md) |  | [optional] 
**edge_router_id** | **str** |  | [optional] 
**expires_at** | **datetime** |  | 
**identity** | [**EntityRef**](EntityRef.md) |  | [optional] 
**identity_id** | **str** |  | [optional] 
**jwt** | **str** |  | [optional] 
**method** | **str** |  | 
**token** | **str** |  | 
**transit_router** | [**EntityRef**](EntityRef.md) |  | [optional] 
**transit_router_id** | **str** |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from openziti_edge_management.models.enrollment_detail import EnrollmentDetail

# TODO update the JSON string below
json = "{}"
# create an instance of EnrollmentDetail from a JSON string
enrollment_detail_instance = EnrollmentDetail.from_json(json)
# print the JSON string representation of the object
print EnrollmentDetail.to_json()

# convert the object into a dict
enrollment_detail_dict = enrollment_detail_instance.to_dict()
# create an instance of EnrollmentDetail from a dict
enrollment_detail_form_dict = enrollment_detail.from_dict(enrollment_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


