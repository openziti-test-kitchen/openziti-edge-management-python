# AuthenticatorUpdate

All of the fields on an authenticator that will be updated

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** |  | 
**tags** | [**Tags**](Tags.md) |  | [optional] 
**username** | **str** |  | 

## Example

```python
from openziti_edge_management.models.authenticator_update import AuthenticatorUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorUpdate from a JSON string
authenticator_update_instance = AuthenticatorUpdate.from_json(json)
# print the JSON string representation of the object
print AuthenticatorUpdate.to_json()

# convert the object into a dict
authenticator_update_dict = authenticator_update_instance.to_dict()
# create an instance of AuthenticatorUpdate from a dict
authenticator_update_form_dict = authenticator_update.from_dict(authenticator_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


