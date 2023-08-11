# PostureData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_session_posture_data** | [**Dict[str, ApiSessionPostureData]**](ApiSessionPostureData.md) |  | 
**domain** | [**PostureDataDomain**](PostureDataDomain.md) |  | 
**mac** | [**PostureDataMac**](PostureDataMac.md) |  | 
**os** | [**PostureDataOs**](PostureDataOs.md) |  | 
**processes** | [**List[PostureDataProcess]**](PostureDataProcess.md) |  | 

## Example

```python
from openziti_edge_management.models.posture_data import PostureData

# TODO update the JSON string below
json = "{}"
# create an instance of PostureData from a JSON string
posture_data_instance = PostureData.from_json(json)
# print the JSON string representation of the object
print PostureData.to_json()

# convert the object into a dict
posture_data_dict = posture_data_instance.to_dict()
# create an instance of PostureData from a dict
posture_data_form_dict = posture_data.from_dict(posture_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


