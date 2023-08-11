# DetailEnrollmentEnvelope


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**EnrollmentDetail**](EnrollmentDetail.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openziti_edge_management.models.detail_enrollment_envelope import DetailEnrollmentEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of DetailEnrollmentEnvelope from a JSON string
detail_enrollment_envelope_instance = DetailEnrollmentEnvelope.from_json(json)
# print the JSON string representation of the object
print DetailEnrollmentEnvelope.to_json()

# convert the object into a dict
detail_enrollment_envelope_dict = detail_enrollment_envelope_instance.to_dict()
# create an instance of DetailEnrollmentEnvelope from a dict
detail_enrollment_envelope_form_dict = detail_enrollment_envelope.from_dict(detail_enrollment_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


