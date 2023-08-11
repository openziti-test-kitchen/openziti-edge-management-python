# TerminatorUpdate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | 
**binding** | **str** |  | 
**cost** | **int** |  | [optional] 
**precedence** | [**TerminatorPrecedence**](TerminatorPrecedence.md) |  | [optional] 
**router** | **str** |  | 
**service** | **str** |  | 
**tags** | [**Tags**](Tags.md) |  | [optional] 

## Example

```python
from openziti_edge_management.models.terminator_update import TerminatorUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of TerminatorUpdate from a JSON string
terminator_update_instance = TerminatorUpdate.from_json(json)
# print the JSON string representation of the object
print TerminatorUpdate.to_json()

# convert the object into a dict
terminator_update_dict = terminator_update_instance.to_dict()
# create an instance of TerminatorUpdate from a dict
terminator_update_form_dict = terminator_update.from_dict(terminator_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


