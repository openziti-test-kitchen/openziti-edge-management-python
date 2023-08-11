# AuthenticatorUpdateWithCurrent

All of the fields on an authenticator that will be updated

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** |  | 
**tags** | [**Tags**](Tags.md) |  | [optional] 
**username** | **str** |  | 
**current_password** | **str** |  | 

## Example

```python
from openziti_edge_management.models.authenticator_update_with_current import AuthenticatorUpdateWithCurrent

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorUpdateWithCurrent from a JSON string
authenticator_update_with_current_instance = AuthenticatorUpdateWithCurrent.from_json(json)
# print the JSON string representation of the object
print AuthenticatorUpdateWithCurrent.to_json()

# convert the object into a dict
authenticator_update_with_current_dict = authenticator_update_with_current_instance.to_dict()
# create an instance of AuthenticatorUpdateWithCurrent from a dict
authenticator_update_with_current_form_dict = authenticator_update_with_current.from_dict(authenticator_update_with_current_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


