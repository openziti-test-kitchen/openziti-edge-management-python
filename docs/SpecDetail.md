# SpecDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) | A map of named links | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**tags** | [**Tags**](Tags.md) |  | [optional] 
**updated_at** | **datetime** |  | 
**name** | **str** |  | 

## Example

```python
from openziti_edge_management.models.spec_detail import SpecDetail

# TODO update the JSON string below
json = "{}"
# create an instance of SpecDetail from a JSON string
spec_detail_instance = SpecDetail.from_json(json)
# print the JSON string representation of the object
print SpecDetail.to_json()

# convert the object into a dict
spec_detail_dict = spec_detail_instance.to_dict()
# create an instance of SpecDetail from a dict
spec_detail_form_dict = spec_detail.from_dict(spec_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


