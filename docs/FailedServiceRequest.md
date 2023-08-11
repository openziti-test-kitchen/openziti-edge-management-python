# FailedServiceRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_session_id** | **str** |  | [optional] 
**policy_failures** | [**List[PolicyFailure]**](PolicyFailure.md) |  | [optional] 
**service_id** | **str** |  | [optional] 
**service_name** | **str** |  | [optional] 
**session_type** | [**DialBind**](DialBind.md) |  | [optional] 
**when** | **datetime** |  | [optional] 

## Example

```python
from openziti_edge_management.models.failed_service_request import FailedServiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FailedServiceRequest from a JSON string
failed_service_request_instance = FailedServiceRequest.from_json(json)
# print the JSON string representation of the object
print FailedServiceRequest.to_json()

# convert the object into a dict
failed_service_request_dict = failed_service_request_instance.to_dict()
# create an instance of FailedServiceRequest from a dict
failed_service_request_form_dict = failed_service_request.from_dict(failed_service_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


