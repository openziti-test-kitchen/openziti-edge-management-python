# PostureCheckFailureMacAddress


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actual_value** | **List[str]** |  | 
**expected_value** | **List[str]** |  | 

## Example

```python
from openziti_edge_management.models.posture_check_failure_mac_address import PostureCheckFailureMacAddress

# TODO update the JSON string below
json = "{}"
# create an instance of PostureCheckFailureMacAddress from a JSON string
posture_check_failure_mac_address_instance = PostureCheckFailureMacAddress.from_json(json)
# print the JSON string representation of the object
print PostureCheckFailureMacAddress.to_json()

# convert the object into a dict
posture_check_failure_mac_address_dict = posture_check_failure_mac_address_instance.to_dict()
# create an instance of PostureCheckFailureMacAddress from a dict
posture_check_failure_mac_address_form_dict = posture_check_failure_mac_address.from_dict(posture_check_failure_mac_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


