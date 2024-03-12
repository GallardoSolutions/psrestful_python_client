# PO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | **object** | The environment the purchase order is being sent from. Should be STAGING or PROD | [optional] 
**order_type** | [**OrderType**](OrderType.md) |  | 
**order_number** | **object** |  | 
**order_date** | **object** |  | 
**last_modified** | **object** |  | 
**total_amount** | **object** | The total amount of the purchase order | 
**payment_terms** | **object** | ie. NET15, NET30, etc. | 
**rush** | **object** | Used to indicate a rush on the purchase order | [optional] 
**currency** | **object** | The currency the purchase order is transacted in ISO4217 format. ie. USD, CAD, EUR, JPY, GBP, etc. | 
**digital_proof** | **object** |  | 
**order_contact_array** | **object** |  | 
**shipment_array** | [**ShipmentArray**](ShipmentArray.md) |  | 
**line_item_array** | [**LineItemArray**](LineItemArray.md) |  | 
**terms_and_conditions** | **object** | The terms and conditions of the purchase order | 
**sales_channel** | **object** | The sales channel the purchase order | 
**promo_code** | **object** |  | [optional] 
**tax_information_array** | **object** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

