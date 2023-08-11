# ListEnrollmentsEnvelope


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[EnrollmentDetail]**](EnrollmentDetail.md) | An array of enrollment resources | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openziti_edge_management.models.list_enrollments_envelope import ListEnrollmentsEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ListEnrollmentsEnvelope from a JSON string
list_enrollments_envelope_instance = ListEnrollmentsEnvelope.from_json(json)
# print the JSON string representation of the object
print ListEnrollmentsEnvelope.to_json()

# convert the object into a dict
list_enrollments_envelope_dict = list_enrollments_envelope_instance.to_dict()
# create an instance of ListEnrollmentsEnvelope from a dict
list_enrollments_envelope_form_dict = list_enrollments_envelope.from_dict(list_enrollments_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


