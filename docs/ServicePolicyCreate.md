# ServicePolicyCreate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity_roles** | **List[str]** |  | [optional] 
**name** | **str** |  | 
**posture_check_roles** | **List[str]** |  | [optional] 
**semantic** | [**Semantic**](Semantic.md) |  | 
**service_roles** | **List[str]** |  | [optional] 
**tags** | [**Tags**](Tags.md) |  | [optional] 
**type** | [**DialBind**](DialBind.md) |  | 

## Example

```python
from openziti_edge_management.models.service_policy_create import ServicePolicyCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ServicePolicyCreate from a JSON string
service_policy_create_instance = ServicePolicyCreate.from_json(json)
# print the JSON string representation of the object
print ServicePolicyCreate.to_json()

# convert the object into a dict
service_policy_create_dict = service_policy_create_instance.to_dict()
# create an instance of ServicePolicyCreate from a dict
service_policy_create_form_dict = service_policy_create.from_dict(service_policy_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


