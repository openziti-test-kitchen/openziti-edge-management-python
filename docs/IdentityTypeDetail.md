# IdentityTypeDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) | A map of named links | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**tags** | [**Tags**](Tags.md) |  | [optional] 
**updated_at** | **datetime** |  | 
**name** | **str** |  | [optional] 

## Example

```python
from openziti_edge_management.models.identity_type_detail import IdentityTypeDetail

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityTypeDetail from a JSON string
identity_type_detail_instance = IdentityTypeDetail.from_json(json)
# print the JSON string representation of the object
print IdentityTypeDetail.to_json()

# convert the object into a dict
identity_type_detail_dict = identity_type_detail_instance.to_dict()
# create an instance of IdentityTypeDetail from a dict
identity_type_detail_form_dict = identity_type_detail.from_dict(identity_type_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


