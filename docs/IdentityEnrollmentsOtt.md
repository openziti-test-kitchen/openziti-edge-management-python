# IdentityEnrollmentsOtt


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expires_at** | **datetime** |  | [optional] 
**id** | **str** |  | [optional] 
**jwt** | **str** |  | [optional] 
**token** | **str** |  | [optional] 

## Example

```python
from openziti_edge_management.models.identity_enrollments_ott import IdentityEnrollmentsOtt

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityEnrollmentsOtt from a JSON string
identity_enrollments_ott_instance = IdentityEnrollmentsOtt.from_json(json)
# print the JSON string representation of the object
print IdentityEnrollmentsOtt.to_json()

# convert the object into a dict
identity_enrollments_ott_dict = identity_enrollments_ott_instance.to_dict()
# create an instance of IdentityEnrollmentsOtt from a dict
identity_enrollments_ott_form_dict = identity_enrollments_ott.from_dict(identity_enrollments_ott_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


