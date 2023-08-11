# DataIntegrityCheckDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_time** | **datetime** |  | 
**error** | **str** |  | 
**fixing_errors** | **bool** |  | 
**in_progress** | **bool** |  | 
**results** | [**List[DataIntegrityCheckDetail]**](DataIntegrityCheckDetail.md) |  | 
**start_time** | **datetime** |  | 
**too_many_errors** | **bool** |  | 

## Example

```python
from openziti_edge_management.models.data_integrity_check_details import DataIntegrityCheckDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DataIntegrityCheckDetails from a JSON string
data_integrity_check_details_instance = DataIntegrityCheckDetails.from_json(json)
# print the JSON string representation of the object
print DataIntegrityCheckDetails.to_json()

# convert the object into a dict
data_integrity_check_details_dict = data_integrity_check_details_instance.to_dict()
# create an instance of DataIntegrityCheckDetails from a dict
data_integrity_check_details_form_dict = data_integrity_check_details.from_dict(data_integrity_check_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


