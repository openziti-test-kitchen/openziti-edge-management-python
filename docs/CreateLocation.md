# CreateLocation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) | A map of named links | [optional] 
**id** | **str** |  | [optional] 

## Example

```python
from openziti_edge_management.models.create_location import CreateLocation

# TODO update the JSON string below
json = "{}"
# create an instance of CreateLocation from a JSON string
create_location_instance = CreateLocation.from_json(json)
# print the JSON string representation of the object
print CreateLocation.to_json()

# convert the object into a dict
create_location_dict = create_location_instance.to_dict()
# create an instance of CreateLocation from a dict
create_location_form_dict = create_location.from_dict(create_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


