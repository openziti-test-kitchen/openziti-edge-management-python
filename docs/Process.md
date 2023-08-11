# Process


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hashes** | **List[str]** |  | [optional] 
**os_type** | [**OsType**](OsType.md) |  | 
**path** | **str** |  | 
**signer_fingerprint** | **str** |  | [optional] 

## Example

```python
from openziti_edge_management.models.process import Process

# TODO update the JSON string below
json = "{}"
# create an instance of Process from a JSON string
process_instance = Process.from_json(json)
# print the JSON string representation of the object
print Process.to_json()

# convert the object into a dict
process_dict = process_instance.to_dict()
# create an instance of Process from a dict
process_form_dict = process.from_dict(process_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


