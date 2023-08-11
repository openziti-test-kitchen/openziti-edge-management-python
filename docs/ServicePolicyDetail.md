# ServicePolicyDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) | A map of named links | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**tags** | [**Tags**](Tags.md) |  | [optional] 
**updated_at** | **datetime** |  | 
**identity_roles** | **List[str]** |  | 
**identity_roles_display** | [**List[NamedRole]**](NamedRole.md) |  | 
**name** | **str** |  | 
**posture_check_roles** | **List[str]** |  | 
**posture_check_roles_display** | [**List[NamedRole]**](NamedRole.md) |  | 
**semantic** | [**Semantic**](Semantic.md) |  | 
**service_roles** | **List[str]** |  | 
**service_roles_display** | [**List[NamedRole]**](NamedRole.md) |  | 
**type** | [**DialBind**](DialBind.md) |  | 

## Example

```python
from openziti_edge_management.models.service_policy_detail import ServicePolicyDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ServicePolicyDetail from a JSON string
service_policy_detail_instance = ServicePolicyDetail.from_json(json)
# print the JSON string representation of the object
print ServicePolicyDetail.to_json()

# convert the object into a dict
service_policy_detail_dict = service_policy_detail_instance.to_dict()
# create an instance of ServicePolicyDetail from a dict
service_policy_detail_form_dict = service_policy_detail.from_dict(service_policy_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


