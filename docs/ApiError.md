# ApiError


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**args** | [**ApiErrorArgs**](ApiErrorArgs.md) |  | [optional] 
**cause** | [**ApiErrorCause**](ApiErrorCause.md) |  | [optional] 
**cause_message** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**data** | **Dict[str, object]** |  | [optional] 
**message** | **str** |  | [optional] 
**request_id** | **str** |  | [optional] 

## Example

```python
from openziti_edge_management.models.api_error import ApiError

# TODO update the JSON string below
json = "{}"
# create an instance of ApiError from a JSON string
api_error_instance = ApiError.from_json(json)
# print the JSON string representation of the object
print ApiError.to_json()

# convert the object into a dict
api_error_dict = api_error_instance.to_dict()
# create an instance of ApiError from a dict
api_error_form_dict = api_error.from_dict(api_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


