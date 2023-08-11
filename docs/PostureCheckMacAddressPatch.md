# PostureCheckMacAddressPatch


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mac_addresses** | **List[str]** |  | [optional] 

## Example

```python
from openziti_edge_management.models.posture_check_mac_address_patch import PostureCheckMacAddressPatch

# TODO update the JSON string below
json = "{}"
# create an instance of PostureCheckMacAddressPatch from a JSON string
posture_check_mac_address_patch_instance = PostureCheckMacAddressPatch.from_json(json)
# print the JSON string representation of the object
print PostureCheckMacAddressPatch.to_json()

# convert the object into a dict
posture_check_mac_address_patch_dict = posture_check_mac_address_patch_instance.to_dict()
# create an instance of PostureCheckMacAddressPatch from a dict
posture_check_mac_address_patch_form_dict = posture_check_mac_address_patch.from_dict(posture_check_mac_address_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


