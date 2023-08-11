# ExternalIdClaimPatch


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** |  | [optional] 
**location** | **str** |  | [optional] 
**matcher** | **str** |  | [optional] 
**matcher_criteria** | **str** |  | [optional] 
**parser** | **str** |  | [optional] 
**parser_criteria** | **str** |  | [optional] 

## Example

```python
from openziti_edge_management.models.external_id_claim_patch import ExternalIdClaimPatch

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalIdClaimPatch from a JSON string
external_id_claim_patch_instance = ExternalIdClaimPatch.from_json(json)
# print the JSON string representation of the object
print ExternalIdClaimPatch.to_json()

# convert the object into a dict
external_id_claim_patch_dict = external_id_claim_patch_instance.to_dict()
# create an instance of ExternalIdClaimPatch from a dict
external_id_claim_patch_form_dict = external_id_claim_patch.from_dict(external_id_claim_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


