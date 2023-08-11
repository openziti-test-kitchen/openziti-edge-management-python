# IdentityEnrollments


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ott** | [**IdentityEnrollmentsOtt**](IdentityEnrollmentsOtt.md) |  | [optional] 
**ottca** | [**IdentityEnrollmentsOttca**](IdentityEnrollmentsOttca.md) |  | [optional] 
**updb** | [**IdentityEnrollmentsOtt**](IdentityEnrollmentsOtt.md) |  | [optional] 

## Example

```python
from openziti_edge_management.models.identity_enrollments import IdentityEnrollments

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityEnrollments from a JSON string
identity_enrollments_instance = IdentityEnrollments.from_json(json)
# print the JSON string representation of the object
print IdentityEnrollments.to_json()

# convert the object into a dict
identity_enrollments_dict = identity_enrollments_instance.to_dict()
# create an instance of IdentityEnrollments from a dict
identity_enrollments_form_dict = identity_enrollments.from_dict(identity_enrollments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


