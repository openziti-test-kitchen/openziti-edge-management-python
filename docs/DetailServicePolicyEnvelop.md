# DetailServicePolicyEnvelop


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ServicePolicyDetail**](ServicePolicyDetail.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openziti_edge_management.models.detail_service_policy_envelop import DetailServicePolicyEnvelop

# TODO update the JSON string below
json = "{}"
# create an instance of DetailServicePolicyEnvelop from a JSON string
detail_service_policy_envelop_instance = DetailServicePolicyEnvelop.from_json(json)
# print the JSON string representation of the object
print DetailServicePolicyEnvelop.to_json()

# convert the object into a dict
detail_service_policy_envelop_dict = detail_service_policy_envelop_instance.to_dict()
# create an instance of DetailServicePolicyEnvelop from a dict
detail_service_policy_envelop_form_dict = detail_service_policy_envelop.from_dict(detail_service_policy_envelop_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


