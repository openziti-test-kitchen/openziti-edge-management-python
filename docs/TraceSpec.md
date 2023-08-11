# TraceSpec


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channels** | **List[str]** |  | [optional] 
**duration** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**trace_id** | **str** |  | [optional] 

## Example

```python
from openziti_edge_management.models.trace_spec import TraceSpec

# TODO update the JSON string below
json = "{}"
# create an instance of TraceSpec from a JSON string
trace_spec_instance = TraceSpec.from_json(json)
# print the JSON string representation of the object
print TraceSpec.to_json()

# convert the object into a dict
trace_spec_dict = trace_spec_instance.to_dict()
# create an instance of TraceSpec from a dict
trace_spec_form_dict = trace_spec.from_dict(trace_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


