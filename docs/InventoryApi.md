# swagger_client.InventoryApi

All URIs are relative to *https://api.psrestful.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_filter_values**](InventoryApi.md#get_filter_values) | **GET** /v{api_version}/suppliers/{supplier_code}/inventory/filter-values/{product_id} | Get Filter Values
[**get_inventory_by_product_v121**](InventoryApi.md#get_inventory_by_product_v121) | **GET** /v1.2.1/suppliers/{supplier_code}/inventory/{product_id} | Get Inventory By Product V121
[**get_inventory_by_product_v200**](InventoryApi.md#get_inventory_by_product_v200) | **GET** /v2.0.0/suppliers/{supplier_code}/inventory/{product_id} | Get Inventory By Product V200

# **get_filter_values**
> FilterValuesResponseV200 get_filter_values(supplier_code, api_version, product_id, body=body, x_forwarded_for=x_forwarded_for, x_account_id=x_account_id, product_id_type=product_id_type, environment=environment)

Get Filter Values

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
api_instance = psrestful.InventoryApi(psrestful.ApiClient(configuration))
supplier_code = NULL  # object | 
api_version = NULL  # object | 
product_id = NULL  # object | 
body = NULL  # object |  (optional)
x_forwarded_for = NULL  # object |  (optional)
x_account_id = NULL  # object |  (optional)
product_id_type = NULL  # object |  (optional)
environment = PROD  # object |  (optional) (default to PROD)

try:
    # Get Filter Values
    api_response = api_instance.get_filter_values(supplier_code, api_version, product_id, body=body,
                                                  x_forwarded_for=x_forwarded_for, x_account_id=x_account_id,
                                                  product_id_type=product_id_type, environment=environment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InventoryApi->get_filter_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_code** | [**object**](.md)|  | 
 **api_version** | [**object**](.md)|  | 
 **product_id** | [**object**](.md)|  | 
 **body** | [**object**](object.md)|  | [optional] 
 **x_forwarded_for** | [**object**](.md)|  | [optional] 
 **x_account_id** | [**object**](.md)|  | [optional] 
 **product_id_type** | [**object**](.md)|  | [optional] 
 **environment** | [**object**](.md)|  | [optional] [default to PROD]

### Return type

[**FilterValuesResponseV200**](FilterValuesResponseV200.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBasic](../README.md#HTTPBasic), [OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inventory_by_product_v121**
> InventoryLevelsResponseV121 get_inventory_by_product_v121(supplier_code, product_id, body=body, x_forwarded_for=x_forwarded_for, x_account_id=x_account_id, environment=environment)

Get Inventory By Product V121

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
api_instance = psrestful.InventoryApi(psrestful.ApiClient(configuration))
supplier_code = NULL  # object | 
product_id = NULL  # object | 
body = NULL  # object |  (optional)
x_forwarded_for = NULL  # object |  (optional)
x_account_id = NULL  # object |  (optional)
environment = PROD  # object |  (optional) (default to PROD)

try:
    # Get Inventory By Product V121
    api_response = api_instance.get_inventory_by_product_v121(supplier_code, product_id, body=body,
                                                              x_forwarded_for=x_forwarded_for,
                                                              x_account_id=x_account_id, environment=environment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InventoryApi->get_inventory_by_product_v121: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_code** | [**object**](.md)|  | 
 **product_id** | [**object**](.md)|  | 
 **body** | [**object**](object.md)|  | [optional] 
 **x_forwarded_for** | [**object**](.md)|  | [optional] 
 **x_account_id** | [**object**](.md)|  | [optional] 
 **environment** | [**object**](.md)|  | [optional] [default to PROD]

### Return type

[**InventoryLevelsResponseV121**](InventoryLevelsResponseV121.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBasic](../README.md#HTTPBasic), [OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inventory_by_product_v200**
> InventoryLevelsResponseV200 get_inventory_by_product_v200(supplier_code, product_id, body=body, x_forwarded_for=x_forwarded_for, x_account_id=x_account_id, environment=environment)

Get Inventory By Product V200

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
api_instance = psrestful.InventoryApi(psrestful.ApiClient(configuration))
supplier_code = NULL  # object | 
product_id = NULL  # object | 
body = NULL  # object |  (optional)
x_forwarded_for = NULL  # object |  (optional)
x_account_id = NULL  # object |  (optional)
environment = PROD  # object |  (optional) (default to PROD)

try:
    # Get Inventory By Product V200
    api_response = api_instance.get_inventory_by_product_v200(supplier_code, product_id, body=body,
                                                              x_forwarded_for=x_forwarded_for,
                                                              x_account_id=x_account_id, environment=environment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InventoryApi->get_inventory_by_product_v200: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_code** | [**object**](.md)|  | 
 **product_id** | [**object**](.md)|  | 
 **body** | [**object**](object.md)|  | [optional] 
 **x_forwarded_for** | [**object**](.md)|  | [optional] 
 **x_account_id** | [**object**](.md)|  | [optional] 
 **environment** | [**object**](.md)|  | [optional] [default to PROD]

### Return type

[**InventoryLevelsResponseV200**](InventoryLevelsResponseV200.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBasic](../README.md#HTTPBasic), [OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

