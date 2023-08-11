# TerminatorDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) | A map of named links | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**tags** | [**Tags**](Tags.md) |  | [optional] 
**updated_at** | **datetime** |  | 
**address** | **str** |  | 
**binding** | **str** |  | 
**cost** | **int** |  | 
**dynamic_cost** | **int** |  | 
**identity** | **str** |  | 
**precedence** | [**TerminatorPrecedence**](TerminatorPrecedence.md) |  | 
**router** | [**EntityRef**](EntityRef.md) |  | 
**router_id** | **str** |  | 
**service** | [**EntityRef**](EntityRef.md) |  | 
**service_id** | **str** |  | 

## Example

```python
from openziti_edge_management.models.terminator_detail import TerminatorDetail

# TODO update the JSON string below
json = "{}"
# create an instance of TerminatorDetail from a JSON string
terminator_detail_instance = TerminatorDetail.from_json(json)
# print the JSON string representation of the object
print TerminatorDetail.to_json()

# convert the object into a dict
terminator_detail_dict = terminator_detail_instance.to_dict()
# create an instance of TerminatorDetail from a dict
terminator_detail_form_dict = terminator_detail.from_dict(terminator_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


