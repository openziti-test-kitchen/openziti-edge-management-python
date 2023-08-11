# ProcessMulti


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hashes** | **List[str]** |  | [optional] 
**os_type** | [**OsType**](OsType.md) |  | 
**path** | **str** |  | 
**signer_fingerprints** | **List[str]** |  | [optional] 

## Example

```python
from openziti_edge_management.models.process_multi import ProcessMulti

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessMulti from a JSON string
process_multi_instance = ProcessMulti.from_json(json)
# print the JSON string representation of the object
print ProcessMulti.to_json()

# convert the object into a dict
process_multi_dict = process_multi_instance.to_dict()
# create an instance of ProcessMulti from a dict
process_multi_form_dict = process_multi.from_dict(process_multi_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


