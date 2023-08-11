# ListEdgeRoutersEnvelope


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[EdgeRouterDetail]**](EdgeRouterDetail.md) | A list of edge router resources | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openziti_edge_management.models.list_edge_routers_envelope import ListEdgeRoutersEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ListEdgeRoutersEnvelope from a JSON string
list_edge_routers_envelope_instance = ListEdgeRoutersEnvelope.from_json(json)
# print the JSON string representation of the object
print ListEdgeRoutersEnvelope.to_json()

# convert the object into a dict
list_edge_routers_envelope_dict = list_edge_routers_envelope_instance.to_dict()
# create an instance of ListEdgeRoutersEnvelope from a dict
list_edge_routers_envelope_form_dict = list_edge_routers_envelope.from_dict(list_edge_routers_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


