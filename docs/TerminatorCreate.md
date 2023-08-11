# TerminatorCreate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | 
**binding** | **str** |  | 
**cost** | **int** |  | [optional] 
**identity** | **str** |  | [optional] 
**identity_secret** | **bytearray** |  | [optional] 
**precedence** | [**TerminatorPrecedence**](TerminatorPrecedence.md) |  | [optional] 
**router** | **str** |  | 
**service** | **str** |  | 
**tags** | [**Tags**](Tags.md) |  | [optional] 

## Example

```python
from openziti_edge_management.models.terminator_create import TerminatorCreate

# TODO update the JSON string below
json = "{}"
# create an instance of TerminatorCreate from a JSON string
terminator_create_instance = TerminatorCreate.from_json(json)
# print the JSON string representation of the object
print TerminatorCreate.to_json()

# convert the object into a dict
terminator_create_dict = terminator_create_instance.to_dict()
# create an instance of TerminatorCreate from a dict
terminator_create_form_dict = terminator_create.from_dict(terminator_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


