# DataIntegrityCheckResultEnvelope


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DataIntegrityCheckDetails**](DataIntegrityCheckDetails.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openziti_edge_management.models.data_integrity_check_result_envelope import DataIntegrityCheckResultEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of DataIntegrityCheckResultEnvelope from a JSON string
data_integrity_check_result_envelope_instance = DataIntegrityCheckResultEnvelope.from_json(json)
# print the JSON string representation of the object
print DataIntegrityCheckResultEnvelope.to_json()

# convert the object into a dict
data_integrity_check_result_envelope_dict = data_integrity_check_result_envelope_instance.to_dict()
# create an instance of DataIntegrityCheckResultEnvelope from a dict
data_integrity_check_result_envelope_form_dict = data_integrity_check_result_envelope.from_dict(data_integrity_check_result_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


