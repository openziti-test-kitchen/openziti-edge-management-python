# IdentityAuthenticatorsUpdb


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from openziti_edge_management.models.identity_authenticators_updb import IdentityAuthenticatorsUpdb

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityAuthenticatorsUpdb from a JSON string
identity_authenticators_updb_instance = IdentityAuthenticatorsUpdb.from_json(json)
# print the JSON string representation of the object
print IdentityAuthenticatorsUpdb.to_json()

# convert the object into a dict
identity_authenticators_updb_dict = identity_authenticators_updb_instance.to_dict()
# create an instance of IdentityAuthenticatorsUpdb from a dict
identity_authenticators_updb_form_dict = identity_authenticators_updb.from_dict(identity_authenticators_updb_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


