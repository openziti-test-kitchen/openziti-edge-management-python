# ListSummaryCountsEnvelope


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **Dict[str, int]** |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openziti_edge_management.models.list_summary_counts_envelope import ListSummaryCountsEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ListSummaryCountsEnvelope from a JSON string
list_summary_counts_envelope_instance = ListSummaryCountsEnvelope.from_json(json)
# print the JSON string representation of the object
print ListSummaryCountsEnvelope.to_json()

# convert the object into a dict
list_summary_counts_envelope_dict = list_summary_counts_envelope_instance.to_dict()
# create an instance of ListSummaryCountsEnvelope from a dict
list_summary_counts_envelope_form_dict = list_summary_counts_envelope.from_dict(list_summary_counts_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


