# PolicyAdvice


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**common_routers** | [**List[RouterEntityRef]**](RouterEntityRef.md) |  | [optional] 
**identity** | [**EntityRef**](EntityRef.md) |  | [optional] 
**identity_id** | **str** |  | [optional] 
**identity_router_count** | **float** |  | [optional] 
**is_bind_allowed** | **bool** |  | [optional] 
**is_dial_allowed** | **bool** |  | [optional] 
**service** | [**EntityRef**](EntityRef.md) |  | [optional] 
**service_id** | **str** |  | [optional] 
**service_router_count** | **float** |  | [optional] 

## Example

```python
from openziti_edge_management.models.policy_advice import PolicyAdvice

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyAdvice from a JSON string
policy_advice_instance = PolicyAdvice.from_json(json)
# print the JSON string representation of the object
print PolicyAdvice.to_json()

# convert the object into a dict
policy_advice_dict = policy_advice_instance.to_dict()
# create an instance of PolicyAdvice from a dict
policy_advice_form_dict = policy_advice.from_dict(policy_advice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


