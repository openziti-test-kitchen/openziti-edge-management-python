# ApiSessionPostureData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint_state** | [**PostureDataEndpointState**](PostureDataEndpointState.md) |  | [optional] 
**mfa** | [**PostureDataMfa**](PostureDataMfa.md) |  | 
**sdk_info** | [**SdkInfo**](SdkInfo.md) |  | [optional] 

## Example

```python
from openziti_edge_management.models.api_session_posture_data import ApiSessionPostureData

# TODO update the JSON string below
json = "{}"
# create an instance of ApiSessionPostureData from a JSON string
api_session_posture_data_instance = ApiSessionPostureData.from_json(json)
# print the JSON string representation of the object
print ApiSessionPostureData.to_json()

# convert the object into a dict
api_session_posture_data_dict = api_session_posture_data_instance.to_dict()
# create an instance of ApiSessionPostureData from a dict
api_session_posture_data_form_dict = api_session_posture_data.from_dict(api_session_posture_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


