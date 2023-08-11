# PostureCheckMacAddressDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mac_addresses** | **List[str]** |  | 

## Example

```python
from openziti_edge_management.models.posture_check_mac_address_detail import PostureCheckMacAddressDetail

# TODO update the JSON string below
json = "{}"
# create an instance of PostureCheckMacAddressDetail from a JSON string
posture_check_mac_address_detail_instance = PostureCheckMacAddressDetail.from_json(json)
# print the JSON string representation of the object
print PostureCheckMacAddressDetail.to_json()

# convert the object into a dict
posture_check_mac_address_detail_dict = posture_check_mac_address_detail_instance.to_dict()
# create an instance of PostureCheckMacAddressDetail from a dict
posture_check_mac_address_detail_form_dict = posture_check_mac_address_detail.from_dict(posture_check_mac_address_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


