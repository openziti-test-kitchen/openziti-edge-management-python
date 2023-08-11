# Authenticate

A generic authenticate object meant for use with the /authenticate path. Required fields depend on authentication method.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_types** | **List[str]** | Specific configuration types that should be returned | [optional] 
**env_info** | [**EnvInfo**](EnvInfo.md) |  | [optional] 
**password** | **str** |  | [optional] 
**sdk_info** | [**SdkInfo**](SdkInfo.md) |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from openziti_edge_management.models.authenticate import Authenticate

# TODO update the JSON string below
json = "{}"
# create an instance of Authenticate from a JSON string
authenticate_instance = Authenticate.from_json(json)
# print the JSON string representation of the object
print Authenticate.to_json()

# convert the object into a dict
authenticate_dict = authenticate_instance.to_dict()
# create an instance of Authenticate from a dict
authenticate_form_dict = authenticate.from_dict(authenticate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


