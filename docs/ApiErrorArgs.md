# ApiErrorArgs


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url_vars** | **Dict[str, str]** |  | [optional] 

## Example

```python
from openziti_edge_management.models.api_error_args import ApiErrorArgs

# TODO update the JSON string below
json = "{}"
# create an instance of ApiErrorArgs from a JSON string
api_error_args_instance = ApiErrorArgs.from_json(json)
# print the JSON string representation of the object
print ApiErrorArgs.to_json()

# convert the object into a dict
api_error_args_dict = api_error_args_instance.to_dict()
# create an instance of ApiErrorArgs from a dict
api_error_args_form_dict = api_error_args.from_dict(api_error_args_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


