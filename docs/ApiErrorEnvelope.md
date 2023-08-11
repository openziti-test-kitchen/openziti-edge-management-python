# ApiErrorEnvelope


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**ApiError**](ApiError.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openziti_edge_management.models.api_error_envelope import ApiErrorEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ApiErrorEnvelope from a JSON string
api_error_envelope_instance = ApiErrorEnvelope.from_json(json)
# print the JSON string representation of the object
print ApiErrorEnvelope.to_json()

# convert the object into a dict
api_error_envelope_dict = api_error_envelope_instance.to_dict()
# create an instance of ApiErrorEnvelope from a dict
api_error_envelope_form_dict = api_error_envelope.from_dict(api_error_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


