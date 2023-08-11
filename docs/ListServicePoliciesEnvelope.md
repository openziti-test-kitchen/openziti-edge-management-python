# ListServicePoliciesEnvelope


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ServicePolicyDetail]**](ServicePolicyDetail.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openziti_edge_management.models.list_service_policies_envelope import ListServicePoliciesEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ListServicePoliciesEnvelope from a JSON string
list_service_policies_envelope_instance = ListServicePoliciesEnvelope.from_json(json)
# print the JSON string representation of the object
print ListServicePoliciesEnvelope.to_json()

# convert the object into a dict
list_service_policies_envelope_dict = list_service_policies_envelope_instance.to_dict()
# create an instance of ListServicePoliciesEnvelope from a dict
list_service_policies_envelope_form_dict = list_service_policies_envelope.from_dict(list_service_policies_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


