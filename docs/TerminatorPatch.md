# TerminatorPatch


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | [optional] 
**binding** | **str** |  | [optional] 
**cost** | **int** |  | [optional] 
**precedence** | [**TerminatorPrecedence**](TerminatorPrecedence.md) |  | [optional] 
**router** | **str** |  | [optional] 
**service** | **str** |  | [optional] 
**tags** | [**Tags**](Tags.md) |  | [optional] 

## Example

```python
from openziti_edge_management.models.terminator_patch import TerminatorPatch

# TODO update the JSON string below
json = "{}"
# create an instance of TerminatorPatch from a JSON string
terminator_patch_instance = TerminatorPatch.from_json(json)
# print the JSON string representation of the object
print TerminatorPatch.to_json()

# convert the object into a dict
terminator_patch_dict = terminator_patch_instance.to_dict()
# create an instance of TerminatorPatch from a dict
terminator_patch_form_dict = terminator_patch.from_dict(terminator_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


