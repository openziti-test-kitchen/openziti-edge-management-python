# ApiVersion


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_base_urls** | **List[str]** |  | [optional] 
**path** | **str** |  | 
**version** | **str** |  | [optional] 

## Example

```python
from openziti_edge_management.models.api_version import ApiVersion

# TODO update the JSON string below
json = "{}"
# create an instance of ApiVersion from a JSON string
api_version_instance = ApiVersion.from_json(json)
# print the JSON string representation of the object
print ApiVersion.to_json()

# convert the object into a dict
api_version_dict = api_version_instance.to_dict()
# create an instance of ApiVersion from a dict
api_version_form_dict = api_version.from_dict(api_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


