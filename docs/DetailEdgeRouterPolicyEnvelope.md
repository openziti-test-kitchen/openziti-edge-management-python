# DetailEdgeRouterPolicyEnvelope


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**EdgeRouterPolicyDetail**](EdgeRouterPolicyDetail.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openziti_edge_management.models.detail_edge_router_policy_envelope import DetailEdgeRouterPolicyEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of DetailEdgeRouterPolicyEnvelope from a JSON string
detail_edge_router_policy_envelope_instance = DetailEdgeRouterPolicyEnvelope.from_json(json)
# print the JSON string representation of the object
print DetailEdgeRouterPolicyEnvelope.to_json()

# convert the object into a dict
detail_edge_router_policy_envelope_dict = detail_edge_router_policy_envelope_instance.to_dict()
# create an instance of DetailEdgeRouterPolicyEnvelope from a dict
detail_edge_router_policy_envelope_form_dict = detail_edge_router_policy_envelope.from_dict(detail_edge_router_policy_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


