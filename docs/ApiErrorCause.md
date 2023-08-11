# ApiErrorCause


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field** | **str** |  | [optional] 
**reason** | **str** |  | [optional] 
**value** | **object** | can be any value - string, number, boolean, array or object | [optional] 
**args** | [**ApiErrorArgs**](ApiErrorArgs.md) |  | [optional] 
**cause** | [**ApiErrorCause**](ApiErrorCause.md) |  | [optional] 
**cause_message** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**data** | **Dict[str, object]** |  | [optional] 
**message** | **str** |  | [optional] 
**request_id** | **str** |  | [optional] 

## Example

```python
from openziti_edge_management.models.api_error_cause import ApiErrorCause

# TODO update the JSON string below
json = "{}"
# create an instance of ApiErrorCause from a JSON string
api_error_cause_instance = ApiErrorCause.from_json(json)
# print the JSON string representation of the object
print ApiErrorCause.to_json()

# convert the object into a dict
api_error_cause_dict = api_error_cause_instance.to_dict()
# create an instance of ApiErrorCause from a dict
api_error_cause_form_dict = api_error_cause.from_dict(api_error_cause_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


