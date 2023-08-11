# PostureCheckMacAddressCreate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mac_addresses** | **List[str]** |  | 

## Example

```python
from openziti_edge_management.models.posture_check_mac_address_create import PostureCheckMacAddressCreate

# TODO update the JSON string below
json = "{}"
# create an instance of PostureCheckMacAddressCreate from a JSON string
posture_check_mac_address_create_instance = PostureCheckMacAddressCreate.from_json(json)
# print the JSON string representation of the object
print PostureCheckMacAddressCreate.to_json()

# convert the object into a dict
posture_check_mac_address_create_dict = posture_check_mac_address_create_instance.to_dict()
# create an instance of PostureCheckMacAddressCreate from a dict
posture_check_mac_address_create_form_dict = posture_check_mac_address_create.from_dict(posture_check_mac_address_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


