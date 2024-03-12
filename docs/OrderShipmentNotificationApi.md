# swagger_client.OrderShipmentNotificationApi

All URIs are relative to *https://api.psrestful.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_order_shipment_notification_v100**](OrderShipmentNotificationApi.md#get_order_shipment_notification_v100) | **GET** /v1.0.0/suppliers/{supplier_code}/order-shipment-notifications/ | Get Order Shipment Notification V100
[**get_order_shipment_notification_v200**](OrderShipmentNotificationApi.md#get_order_shipment_notification_v200) | **GET** /v2.0.0/suppliers/{supplier_code}/order-shipment-notifications/ | Get Order Shipment Notification V200

# **get_order_shipment_notification_v100**
> GetOrderShipmentNotificationResponse get_order_shipment_notification_v100(query_type, supplier_code, body=body, x_forwarded_for=x_forwarded_for, x_account_id=x_account_id, reference_number=reference_number, status_timestamp=status_timestamp, environment=environment)

Get Order Shipment Notification V100

### Example

```python
from __future__ import print_function
import time
import psrestful
from psrestful.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = psrestful.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'# Configure HTTP basic authorization: HTTPBasic
configuration = psrestful.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure OAuth2 access token for authorization: OAuth2PasswordBearer
configuration = psrestful.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = psrestful.OrderShipmentNotificationApi(psrestful.ApiClient(configuration))
query_type = psrestful.PsDomainModelOsnCommonQueryType()  # PsDomainModelOsnCommonQueryType | 
supplier_code = NULL  # object | 
body = NULL  # object |  (optional)
x_forwarded_for = NULL  # object |  (optional)
x_account_id = NULL  # object |  (optional)
reference_number = NULL  # object |  (optional)
status_timestamp = NULL  # object |  (optional)
environment = PROD  # object |  (optional) (default to PROD)

try:
    # Get Order Shipment Notification V100
    api_response = api_instance.get_order_shipment_notification_v100(query_type, supplier_code, body=body,
                                                                     x_forwarded_for=x_forwarded_for,
                                                                     x_account_id=x_account_id,
                                                                     reference_number=reference_number,
                                                                     status_timestamp=status_timestamp,
                                                                     environment=environment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderShipmentNotificationApi->get_order_shipment_notification_v100: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_type** | [**PsDomainModelOsnCommonQueryType**](.md)|  | 
 **supplier_code** | [**object**](.md)|  | 
 **body** | [**object**](object.md)|  | [optional] 
 **x_forwarded_for** | [**object**](.md)|  | [optional] 
 **x_account_id** | [**object**](.md)|  | [optional] 
 **reference_number** | [**object**](.md)|  | [optional] 
 **status_timestamp** | [**object**](.md)|  | [optional] 
 **environment** | [**object**](.md)|  | [optional] [default to PROD]

### Return type

[**GetOrderShipmentNotificationResponse**](GetOrderShipmentNotificationResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBasic](../README.md#HTTPBasic), [OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_shipment_notification_v200**
> GetOrderShipmentNotificationResponse get_order_shipment_notification_v200(query_type, supplier_code, body=body, x_forwarded_for=x_forwarded_for, x_account_id=x_account_id, reference_number=reference_number, shipment_date_timestamp=shipment_date_timestamp, environment=environment)

Get Order Shipment Notification V200

### Example

```python
from __future__ import print_function
import time
import psrestful
from psrestful.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = psrestful.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'# Configure HTTP basic authorization: HTTPBasic
configuration = psrestful.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure OAuth2 access token for authorization: OAuth2PasswordBearer
configuration = psrestful.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = psrestful.OrderShipmentNotificationApi(psrestful.ApiClient(configuration))
query_type = psrestful.PsDomainModelOsnCommonQueryType()  # PsDomainModelOsnCommonQueryType | 
supplier_code = NULL  # object | 
body = NULL  # object |  (optional)
x_forwarded_for = NULL  # object |  (optional)
x_account_id = NULL  # object |  (optional)
reference_number = NULL  # object |  (optional)
shipment_date_timestamp = NULL  # object |  (optional)
environment = PROD  # object |  (optional) (default to PROD)

try:
    # Get Order Shipment Notification V200
    api_response = api_instance.get_order_shipment_notification_v200(query_type, supplier_code, body=body,
                                                                     x_forwarded_for=x_forwarded_for,
                                                                     x_account_id=x_account_id,
                                                                     reference_number=reference_number,
                                                                     shipment_date_timestamp=shipment_date_timestamp,
                                                                     environment=environment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderShipmentNotificationApi->get_order_shipment_notification_v200: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_type** | [**PsDomainModelOsnCommonQueryType**](.md)|  | 
 **supplier_code** | [**object**](.md)|  | 
 **body** | [**object**](object.md)|  | [optional] 
 **x_forwarded_for** | [**object**](.md)|  | [optional] 
 **x_account_id** | [**object**](.md)|  | [optional] 
 **reference_number** | [**object**](.md)|  | [optional] 
 **shipment_date_timestamp** | [**object**](.md)|  | [optional] 
 **environment** | [**object**](.md)|  | [optional] [default to PROD]

### Return type

[**GetOrderShipmentNotificationResponse**](GetOrderShipmentNotificationResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBasic](../README.md#HTTPBasic), [OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

