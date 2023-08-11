# IdentityExtendEnrollmentRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_cert_csr** | **str** |  | 

## Example

```python
from openziti_edge_management.models.identity_extend_enrollment_request import IdentityExtendEnrollmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityExtendEnrollmentRequest from a JSON string
identity_extend_enrollment_request_instance = IdentityExtendEnrollmentRequest.from_json(json)
# print the JSON string representation of the object
print IdentityExtendEnrollmentRequest.to_json()

# convert the object into a dict
identity_extend_enrollment_request_dict = identity_extend_enrollment_request_instance.to_dict()
# create an instance of IdentityExtendEnrollmentRequest from a dict
identity_extend_enrollment_request_form_dict = identity_extend_enrollment_request.from_dict(identity_extend_enrollment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


