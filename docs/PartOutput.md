# PartOutput

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**part_id** | **object** |  | 
**part_description** | **object** |  | 
**part_price_array** | **object** |  | 
**part_group** | **object** | A numeric identifier grouping mutually exclusive parts together. When configuring data, always start with part group “1” | 
**next_part_group** | **object** | The next mutually exclusive partGroup to complete configuration ofthe product | [optional] 
**part_group_required** | **object** | A boolean value specifying if this partGroup is required for the product configuration. If set to TRUE, a selection in the partGroup is required for ordering | 
**part_group_description** | **object** | A description of the partGroup: Optional Lid&#x60;, &#x60;Straw | 
**ratio** | **object** | Describes how the amount of partIds that need to be added to the order based on the number of products ordered | 
**default_part** | **object** | This part is included in the “Basic Pricing Configuration” service price. This field is optional, but highly encouraged | 
**location_id_array** | **object** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

