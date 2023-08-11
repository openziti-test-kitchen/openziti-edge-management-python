# DataIntegrityCheckDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | 
**fixed** | **bool** |  | 

## Example

```python
from openziti_edge_management.models.data_integrity_check_detail import DataIntegrityCheckDetail

# TODO update the JSON string below
json = "{}"
# create an instance of DataIntegrityCheckDetail from a JSON string
data_integrity_check_detail_instance = DataIntegrityCheckDetail.from_json(json)
# print the JSON string representation of the object
print DataIntegrityCheckDetail.to_json()

# convert the object into a dict
data_integrity_check_detail_dict = data_integrity_check_detail_instance.to_dict()
# create an instance of DataIntegrityCheckDetail from a dict
data_integrity_check_detail_form_dict = data_integrity_check_detail.from_dict(data_integrity_check_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


