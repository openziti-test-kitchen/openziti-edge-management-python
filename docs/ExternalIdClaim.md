# ExternalIdClaim


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** |  | 
**location** | **str** |  | 
**matcher** | **str** |  | 
**matcher_criteria** | **str** |  | 
**parser** | **str** |  | 
**parser_criteria** | **str** |  | 

## Example

```python
from openziti_edge_management.models.external_id_claim import ExternalIdClaim

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalIdClaim from a JSON string
external_id_claim_instance = ExternalIdClaim.from_json(json)
# print the JSON string representation of the object
print ExternalIdClaim.to_json()

# convert the object into a dict
external_id_claim_dict = external_id_claim_instance.to_dict()
# create an instance of ExternalIdClaim from a dict
external_id_claim_form_dict = external_id_claim.from_dict(external_id_claim_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


