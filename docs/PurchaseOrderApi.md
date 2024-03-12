# swagger_client.PurchaseOrderApi

All URIs are relative to *https://api.psrestful.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_supported_order_types**](PurchaseOrderApi.md#get_supported_order_types) | **GET** /v1.0.0/suppliers/{supplier_code}/supported-order-types/ | Get Supported Order Types
[**send_po**](PurchaseOrderApi.md#send_po) | **POST** /v1.0.0/suppliers/{supplier_code}/purchase-orders/ | Send Po

# **get_supported_order_types**
> GetSupportedOrderTypesResponse get_supported_order_types(supplier_code, body=body, x_forwarded_for=x_forwarded_for, x_account_id=x_account_id, environment=environment)

Get Supported Order Types

This function returns the supported Order Types the vendor accepts.

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
api_instance = psrestful.PurchaseOrderApi(psrestful.ApiClient(configuration))
supplier_code = NULL  # object | 
body = NULL  # object |  (optional)
x_forwarded_for = NULL  # object |  (optional)
x_account_id = NULL  # object |  (optional)
environment = PROD  # object |  (optional) (default to PROD)

try:
    # Get Supported Order Types
    api_response = api_instance.get_supported_order_types(supplier_code, body=body, x_forwarded_for=x_forwarded_for,
                                                          x_account_id=x_account_id, environment=environment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PurchaseOrderApi->get_supported_order_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_code** | [**object**](.md)|  | 
 **body** | [**object**](object.md)|  | [optional] 
 **x_forwarded_for** | [**object**](.md)|  | [optional] 
 **x_account_id** | [**object**](.md)|  | [optional] 
 **environment** | [**object**](.md)|  | [optional] [default to PROD]

### Return type

[**GetSupportedOrderTypesResponse**](GetSupportedOrderTypesResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBasic](../README.md#HTTPBasic), [OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_po**
> SendPOResponse send_po(body, supplier_code, x_forwarded_for=x_forwarded_for, x_account_id=x_account_id)

Send Po

This function will send blank, sample, simple or configured purchase order to a supplier. The purchase order service is designed to work in conjunction with data from PPC service

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
api_instance = psrestful.PurchaseOrderApi(psrestful.ApiClient(configuration))
body = psrestful.BodySendPo()  # BodySendPo | 
supplier_code = NULL  # object | 
x_forwarded_for = NULL  # object |  (optional)
x_account_id = NULL  # object |  (optional)

try:
    # Send Po
    api_response = api_instance.send_po(body, supplier_code, x_forwarded_for=x_forwarded_for, x_account_id=x_account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PurchaseOrderApi->send_po: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BodySendPo**](BodySendPo.md)|  | 
 **supplier_code** | [**object**](.md)|  | 
 **x_forwarded_for** | [**object**](.md)|  | [optional] 
 **x_account_id** | [**object**](.md)|  | [optional] 

### Return type

[**SendPOResponse**](SendPOResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBasic](../README.md#HTTPBasic), [OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

