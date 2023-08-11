# IdentityExtendEnrollmentEnvelope


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**IdentityExtendCerts**](IdentityExtendCerts.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from openziti_edge_management.models.identity_extend_enrollment_envelope import IdentityExtendEnrollmentEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityExtendEnrollmentEnvelope from a JSON string
identity_extend_enrollment_envelope_instance = IdentityExtendEnrollmentEnvelope.from_json(json)
# print the JSON string representation of the object
print IdentityExtendEnrollmentEnvelope.to_json()

# convert the object into a dict
identity_extend_enrollment_envelope_dict = identity_extend_enrollment_envelope_instance.to_dict()
# create an instance of IdentityExtendEnrollmentEnvelope from a dict
identity_extend_enrollment_envelope_form_dict = identity_extend_enrollment_envelope.from_dict(identity_extend_enrollment_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


