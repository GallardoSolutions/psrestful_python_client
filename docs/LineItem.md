# LineItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line_number** | **object** |  | 
**description** | **object** |  | 
**line_type** | [**LineType**](LineType.md) |  | 
**quantity** | **object** |  | 
**fob_id** | **object** | Used to indicate the FOB point.  Use fobId from the supplier’s Product Pricing and Configuration Service to populate this information | 
**tolerance_details** | [**ToleranceDetails**](ToleranceDetails.md) |  | 
**allow_partial_shipments** | **object** |  | 
**unit_price** | **object** |  | 
**line_item_total** | **object** |  | 
**requested_ship_date** | **object** | The date the line item is requested to ship from the FOB point | 
**requested_in_hands_date** | **object** | The date the line item is requested to arrive at the shipping destination | 
**reference_sales_quote** | **object** | The sales quote number associated with this purchase order line (if applicable) | 
**program** | **object** |  | 
**end_customer_sales_order** | **object** | The distributor’s order number provided to the end customer | 
**product_id** | **object** | The manufacturer’s product id associated with the configuration data | 
**customer_product_id** | **object** | The distributor’s product id | 
**line_item_grouping_id** | **object** | An identifier that allows configuration data to be spread out among multiple purchase order lines. Keep &#x60;lineItemGroupingID&#x60; unique when referencing the same product on the purchase order.  Any change to the product, location, decoration, or artwork should produce a unique &#x60;lineItemGroupingID&#x60; to the purchase order | 
**part_array** | **object** |  | 
**configuration** | **object** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

