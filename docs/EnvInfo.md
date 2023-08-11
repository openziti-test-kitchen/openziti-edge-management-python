# EnvInfo

Environment information an authenticating client may provide

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arch** | **str** |  | [optional] 
**os** | **str** |  | [optional] 
**os_release** | **str** |  | [optional] 
**os_version** | **str** |  | [optional] 

## Example

```python
from openziti_edge_management.models.env_info import EnvInfo

# TODO update the JSON string below
json = "{}"
# create an instance of EnvInfo from a JSON string
env_info_instance = EnvInfo.from_json(json)
# print the JSON string representation of the object
print EnvInfo.to_json()

# convert the object into a dict
env_info_dict = env_info_instance.to_dict()
# create an instance of EnvInfo from a dict
env_info_form_dict = env_info.from_dict(env_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


