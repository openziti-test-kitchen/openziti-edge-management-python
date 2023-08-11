# PostureCheckMacAddressUpdate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mac_addresses** | **List[str]** |  | 

## Example

```python
from openziti_edge_management.models.posture_check_mac_address_update import PostureCheckMacAddressUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of PostureCheckMacAddressUpdate from a JSON string
posture_check_mac_address_update_instance = PostureCheckMacAddressUpdate.from_json(json)
# print the JSON string representation of the object
print PostureCheckMacAddressUpdate.to_json()

# convert the object into a dict
posture_check_mac_address_update_dict = posture_check_mac_address_update_instance.to_dict()
# create an instance of PostureCheckMacAddressUpdate from a dict
posture_check_mac_address_update_form_dict = posture_check_mac_address_update.from_dict(posture_check_mac_address_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


