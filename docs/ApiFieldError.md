# ApiFieldError


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field** | **str** |  | [optional] 
**reason** | **str** |  | [optional] 
**value** | **object** | can be any value - string, number, boolean, array or object | [optional] 

## Example

```python
from openziti_edge_management.models.api_field_error import ApiFieldError

# TODO update the JSON string below
json = "{}"
# create an instance of ApiFieldError from a JSON string
api_field_error_instance = ApiFieldError.from_json(json)
# print the JSON string representation of the object
print ApiFieldError.to_json()

# convert the object into a dict
api_field_error_dict = api_field_error_instance.to_dict()
# create an instance of ApiFieldError from a dict
api_field_error_form_dict = api_field_error.from_dict(api_field_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


