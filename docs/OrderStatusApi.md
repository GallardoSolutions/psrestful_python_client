# swagger_client.OrderStatusApi

All URIs are relative to *https://api.psrestful.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_issue_v200**](OrderStatusApi.md#get_issue_v200) | **GET** /v2.0.0/suppliers/{supplier_code}/issues/{issue_id}/ | Get Issue
[**get_order_status_details_v100**](OrderStatusApi.md#get_order_status_details_v100) | **GET** /v1.0.0/suppliers/{supplier_code}/order-status-details/ | Get Order Status Details
[**get_order_status_types_v100**](OrderStatusApi.md#get_order_status_types_v100) | **GET** /v1.0.0/suppliers/{supplier_code}/order-status-types/ | Get Order Status Types
[**get_order_status_v200**](OrderStatusApi.md#get_order_status_v200) | **GET** /v2.0.0/suppliers/{supplier_code}/order-status/ | Get Order Status
[**get_service_methods_v200**](OrderStatusApi.md#get_service_methods_v200) | **GET** /v2.0.0/suppliers/{supplier_code}/service-methods/ | Get Service Methods

# **get_issue_v200**
> GetIssueResponseV200 get_issue_v200(supplier_code, issue_id, body=body, x_forwarded_for=x_forwarded_for, x_account_id=x_account_id, environment=environment)

Get Issue

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
api_instance = psrestful.OrderStatusApi(psrestful.ApiClient(configuration))
supplier_code = NULL  # object | 
issue_id = NULL  # object | 
body = NULL  # object |  (optional)
x_forwarded_for = NULL  # object |  (optional)
x_account_id = NULL  # object |  (optional)
environment = PROD  # object |  (optional) (default to PROD)

try:
    # Get Issue
    api_response = api_instance.get_issue_v200(supplier_code, issue_id, body=body, x_forwarded_for=x_forwarded_for,
                                               x_account_id=x_account_id, environment=environment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderStatusApi->get_issue_v200: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_code** | [**object**](.md)|  | 
 **issue_id** | [**object**](.md)|  | 
 **body** | [**object**](object.md)|  | [optional] 
 **x_forwarded_for** | [**object**](.md)|  | [optional] 
 **x_account_id** | [**object**](.md)|  | [optional] 
 **environment** | [**object**](.md)|  | [optional] [default to PROD]

### Return type

[**GetIssueResponseV200**](GetIssueResponseV200.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBasic](../README.md#HTTPBasic), [OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_status_details_v100**
> OrderStatusDetailsResponse get_order_status_details_v100(query_type, supplier_code, body=body, x_forwarded_for=x_forwarded_for, x_account_id=x_account_id, reference_number=reference_number, status_timestamp=status_timestamp, environment=environment)

Get Order Status Details

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
api_instance = psrestful.OrderStatusApi(psrestful.ApiClient(configuration))
query_type = psrestful.PsDomainModelOrderStatusV100QueryType()  # PsDomainModelOrderStatusV100QueryType | 
supplier_code = NULL  # object | 
body = NULL  # object |  (optional)
x_forwarded_for = NULL  # object |  (optional)
x_account_id = NULL  # object |  (optional)
reference_number = NULL  # object |  (optional)
status_timestamp = NULL  # object |  (optional)
environment = PROD  # object |  (optional) (default to PROD)

try:
    # Get Order Status Details
    api_response = api_instance.get_order_status_details_v100(query_type, supplier_code, body=body,
                                                              x_forwarded_for=x_forwarded_for,
                                                              x_account_id=x_account_id,
                                                              reference_number=reference_number,
                                                              status_timestamp=status_timestamp,
                                                              environment=environment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderStatusApi->get_order_status_details_v100: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_type** | [**PsDomainModelOrderStatusV100QueryType**](.md)|  | 
 **supplier_code** | [**object**](.md)|  | 
 **body** | [**object**](object.md)|  | [optional] 
 **x_forwarded_for** | [**object**](.md)|  | [optional] 
 **x_account_id** | [**object**](.md)|  | [optional] 
 **reference_number** | [**object**](.md)|  | [optional] 
 **status_timestamp** | [**object**](.md)|  | [optional] 
 **environment** | [**object**](.md)|  | [optional] [default to PROD]

### Return type

[**OrderStatusDetailsResponse**](OrderStatusDetailsResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBasic](../README.md#HTTPBasic), [OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_status_types_v100**
> OrderStatusTypesResponse get_order_status_types_v100(supplier_code, body=body, x_forwarded_for=x_forwarded_for, x_account_id=x_account_id, environment=environment)

Get Order Status Types

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
api_instance = psrestful.OrderStatusApi(psrestful.ApiClient(configuration))
supplier_code = NULL  # object | 
body = NULL  # object |  (optional)
x_forwarded_for = NULL  # object |  (optional)
x_account_id = NULL  # object |  (optional)
environment = PROD  # object |  (optional) (default to PROD)

try:
    # Get Order Status Types
    api_response = api_instance.get_order_status_types_v100(supplier_code, body=body, x_forwarded_for=x_forwarded_for,
                                                            x_account_id=x_account_id, environment=environment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderStatusApi->get_order_status_types_v100: %s\n" % e)
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

[**OrderStatusTypesResponse**](OrderStatusTypesResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBasic](../README.md#HTTPBasic), [OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_status_v200**
> GetOrderStatusResponseV200 get_order_status_v200(query_type, supplier_code, body=body, x_forwarded_for=x_forwarded_for, x_account_id=x_account_id, reference_number=reference_number, status_timestamp=status_timestamp, environment=environment)

Get Order Status

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
api_instance = psrestful.OrderStatusApi(psrestful.ApiClient(configuration))
query_type = psrestful.PsDomainModelOrderStatusV100QueryType()  # PsDomainModelOrderStatusV100QueryType | 
supplier_code = NULL  # object | 
body = NULL  # object |  (optional)
x_forwarded_for = NULL  # object |  (optional)
x_account_id = NULL  # object |  (optional)
reference_number = NULL  # object |  (optional)
status_timestamp = NULL  # object |  (optional)
environment = PROD  # object |  (optional) (default to PROD)

try:
    # Get Order Status
    api_response = api_instance.get_order_status_v200(query_type, supplier_code, body=body,
                                                      x_forwarded_for=x_forwarded_for, x_account_id=x_account_id,
                                                      reference_number=reference_number,
                                                      status_timestamp=status_timestamp, environment=environment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderStatusApi->get_order_status_v200: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_type** | [**PsDomainModelOrderStatusV100QueryType**](.md)|  | 
 **supplier_code** | [**object**](.md)|  | 
 **body** | [**object**](object.md)|  | [optional] 
 **x_forwarded_for** | [**object**](.md)|  | [optional] 
 **x_account_id** | [**object**](.md)|  | [optional] 
 **reference_number** | [**object**](.md)|  | [optional] 
 **status_timestamp** | [**object**](.md)|  | [optional] 
 **environment** | [**object**](.md)|  | [optional] [default to PROD]

### Return type

[**GetOrderStatusResponseV200**](GetOrderStatusResponseV200.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBasic](../README.md#HTTPBasic), [OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_methods_v200**
> GetServiceMethodsResponseV200 get_service_methods_v200(supplier_code, body=body, x_forwarded_for=x_forwarded_for, x_account_id=x_account_id, environment=environment)

Get Service Methods

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
api_instance = psrestful.OrderStatusApi(psrestful.ApiClient(configuration))
supplier_code = NULL  # object | 
body = NULL  # object |  (optional)
x_forwarded_for = NULL  # object |  (optional)
x_account_id = NULL  # object |  (optional)
environment = PROD  # object |  (optional) (default to PROD)

try:
    # Get Service Methods
    api_response = api_instance.get_service_methods_v200(supplier_code, body=body, x_forwarded_for=x_forwarded_for,
                                                         x_account_id=x_account_id, environment=environment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderStatusApi->get_service_methods_v200: %s\n" % e)
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

[**GetServiceMethodsResponseV200**](GetServiceMethodsResponseV200.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBasic](../README.md#HTTPBasic), [OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

