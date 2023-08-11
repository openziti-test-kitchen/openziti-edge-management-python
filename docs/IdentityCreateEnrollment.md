# IdentityCreateEnrollment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ott** | **bool** |  | [optional] 
**ottca** | **str** |  | [optional] 
**updb** | **str** |  | [optional] 

## Example

```python
from openziti_edge_management.models.identity_create_enrollment import IdentityCreateEnrollment

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityCreateEnrollment from a JSON string
identity_create_enrollment_instance = IdentityCreateEnrollment.from_json(json)
# print the JSON string representation of the object
print IdentityCreateEnrollment.to_json()

# convert the object into a dict
identity_create_enrollment_dict = identity_create_enrollment_instance.to_dict()
# create an instance of IdentityCreateEnrollment from a dict
identity_create_enrollment_form_dict = identity_create_enrollment.from_dict(identity_create_enrollment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


