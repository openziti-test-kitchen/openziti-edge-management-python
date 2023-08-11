# SdkInfo

SDK information an authenticating client may provide

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** |  | [optional] 
**app_version** | **str** |  | [optional] 
**branch** | **str** |  | [optional] 
**revision** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from openziti_edge_management.models.sdk_info import SdkInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SdkInfo from a JSON string
sdk_info_instance = SdkInfo.from_json(json)
# print the JSON string representation of the object
print SdkInfo.to_json()

# convert the object into a dict
sdk_info_dict = sdk_info_instance.to_dict()
# create an instance of SdkInfo from a dict
sdk_info_form_dict = sdk_info.from_dict(sdk_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


