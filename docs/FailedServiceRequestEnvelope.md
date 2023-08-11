# FailedServiceRequestEnvelope


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[FailedServiceRequest]**](FailedServiceRequest.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openziti_edge_management.models.failed_service_request_envelope import FailedServiceRequestEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of FailedServiceRequestEnvelope from a JSON string
failed_service_request_envelope_instance = FailedServiceRequestEnvelope.from_json(json)
# print the JSON string representation of the object
print FailedServiceRequestEnvelope.to_json()

# convert the object into a dict
failed_service_request_envelope_dict = failed_service_request_envelope_instance.to_dict()
# create an instance of FailedServiceRequestEnvelope from a dict
failed_service_request_envelope_form_dict = failed_service_request_envelope.from_dict(failed_service_request_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


