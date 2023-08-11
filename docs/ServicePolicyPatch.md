# ServicePolicyPatch


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity_roles** | **List[str]** |  | [optional] 
**name** | **str** |  | [optional] 
**posture_check_roles** | **List[str]** |  | [optional] 
**semantic** | [**Semantic**](Semantic.md) |  | [optional] 
**service_roles** | **List[str]** |  | [optional] 
**tags** | [**Tags**](Tags.md) |  | [optional] 
**type** | [**DialBind**](DialBind.md) |  | [optional] 

## Example

```python
from openziti_edge_management.models.service_policy_patch import ServicePolicyPatch

# TODO update the JSON string below
json = "{}"
# create an instance of ServicePolicyPatch from a JSON string
service_policy_patch_instance = ServicePolicyPatch.from_json(json)
# print the JSON string representation of the object
print ServicePolicyPatch.to_json()

# convert the object into a dict
service_policy_patch_dict = service_policy_patch_instance.to_dict()
# create an instance of ServicePolicyPatch from a dict
service_policy_patch_form_dict = service_policy_patch.from_dict(service_policy_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


