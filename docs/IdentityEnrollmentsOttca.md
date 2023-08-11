# IdentityEnrollmentsOttca


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ca** | [**EntityRef**](EntityRef.md) |  | [optional] 
**ca_id** | **str** |  | [optional] 
**expires_at** | **datetime** |  | [optional] 
**id** | **str** |  | [optional] 
**jwt** | **str** |  | [optional] 
**token** | **str** |  | [optional] 

## Example

```python
from openziti_edge_management.models.identity_enrollments_ottca import IdentityEnrollmentsOttca

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityEnrollmentsOttca from a JSON string
identity_enrollments_ottca_instance = IdentityEnrollmentsOttca.from_json(json)
# print the JSON string representation of the object
print IdentityEnrollmentsOttca.to_json()

# convert the object into a dict
identity_enrollments_ottca_dict = identity_enrollments_ottca_instance.to_dict()
# create an instance of IdentityEnrollmentsOttca from a dict
identity_enrollments_ottca_form_dict = identity_enrollments_ottca.from_dict(identity_enrollments_ottca_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


