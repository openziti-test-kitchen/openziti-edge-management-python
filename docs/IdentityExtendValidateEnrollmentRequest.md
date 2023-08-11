# IdentityExtendValidateEnrollmentRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_cert** | **str** | A PEM encoded client certificate previously returned after an extension request | 

## Example

```python
from openziti_edge_management.models.identity_extend_validate_enrollment_request import IdentityExtendValidateEnrollmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityExtendValidateEnrollmentRequest from a JSON string
identity_extend_validate_enrollment_request_instance = IdentityExtendValidateEnrollmentRequest.from_json(json)
# print the JSON string representation of the object
print IdentityExtendValidateEnrollmentRequest.to_json()

# convert the object into a dict
identity_extend_validate_enrollment_request_dict = identity_extend_validate_enrollment_request_instance.to_dict()
# create an instance of IdentityExtendValidateEnrollmentRequest from a dict
identity_extend_validate_enrollment_request_form_dict = identity_extend_validate_enrollment_request.from_dict(identity_extend_validate_enrollment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


