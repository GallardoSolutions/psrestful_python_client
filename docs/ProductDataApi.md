# swagger_client.ProductDataApi

All URIs are relative to *https://api.psrestful.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_product_closeout_v100**](ProductDataApi.md#get_product_closeout_v100) | **GET** /v1.0.0/suppliers/{supplier_code}/products-closeout | Get Product Closeout V100
[**get_product_closeout_v200**](ProductDataApi.md#get_product_closeout_v200) | **GET** /v2.0.0/suppliers/{supplier_code}/products-closeout | Get Product Closeout V200
[**get_product_date_modified_v100**](ProductDataApi.md#get_product_date_modified_v100) | **GET** /v1.0.0/suppliers/{supplier_code}/products-modified-since | Get Product Date Modified V100
[**get_product_date_modified_v200**](ProductDataApi.md#get_product_date_modified_v200) | **GET** /v2.0.0/suppliers/{supplier_code}/products-modified-since | Get Product Date Modified V200
[**get_product_v200**](ProductDataApi.md#get_product_v200) | **GET** /v2.0.0/suppliers/{supplier_code}/products/{product_id} | Get Product V200

# **get_product_closeout_v100**
> ProductCloseOutResponseV100 get_product_closeout_v100(supplier_code, body=body, x_forwarded_for=x_forwarded_for, x_account_id=x_account_id, environment=environment)

Get Product Closeout V100

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
api_instance = psrestful.ProductDataApi(psrestful.ApiClient(configuration))
supplier_code = NULL  # object | 
body = NULL  # object |  (optional)
x_forwarded_for = NULL  # object |  (optional)
x_account_id = NULL  # object |  (optional)
environment = PROD  # object |  (optional) (default to PROD)

try:
    # Get Product Closeout V100
    api_response = api_instance.get_product_closeout_v100(supplier_code, body=body, x_forwarded_for=x_forwarded_for,
                                                          x_account_id=x_account_id, environment=environment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductDataApi->get_product_closeout_v100: %s\n" % e)
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

[**ProductCloseOutResponseV100**](ProductCloseOutResponseV100.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBasic](../README.md#HTTPBasic), [OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_closeout_v200**
> ProductCloseOutResponseV200 get_product_closeout_v200(supplier_code, body=body, x_forwarded_for=x_forwarded_for, x_account_id=x_account_id, environment=environment)

Get Product Closeout V200

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
api_instance = psrestful.ProductDataApi(psrestful.ApiClient(configuration))
supplier_code = NULL  # object | 
body = NULL  # object |  (optional)
x_forwarded_for = NULL  # object |  (optional)
x_account_id = NULL  # object |  (optional)
environment = PROD  # object |  (optional) (default to PROD)

try:
    # Get Product Closeout V200
    api_response = api_instance.get_product_closeout_v200(supplier_code, body=body, x_forwarded_for=x_forwarded_for,
                                                          x_account_id=x_account_id, environment=environment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductDataApi->get_product_closeout_v200: %s\n" % e)
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

[**ProductCloseOutResponseV200**](ProductCloseOutResponseV200.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBasic](../README.md#HTTPBasic), [OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_date_modified_v100**
> ProductDateModifiedResponseV100 get_product_date_modified_v100(since, supplier_code, body=body, x_forwarded_for=x_forwarded_for, x_account_id=x_account_id, environment=environment)

Get Product Date Modified V100

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
api_instance = psrestful.ProductDataApi(psrestful.ApiClient(configuration))
since = NULL  # object | 
supplier_code = NULL  # object | 
body = NULL  # object |  (optional)
x_forwarded_for = NULL  # object |  (optional)
x_account_id = NULL  # object |  (optional)
environment = PROD  # object |  (optional) (default to PROD)

try:
    # Get Product Date Modified V100
    api_response = api_instance.get_product_date_modified_v100(since, supplier_code, body=body,
                                                               x_forwarded_for=x_forwarded_for,
                                                               x_account_id=x_account_id, environment=environment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductDataApi->get_product_date_modified_v100: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **since** | [**object**](.md)|  | 
 **supplier_code** | [**object**](.md)|  | 
 **body** | [**object**](object.md)|  | [optional] 
 **x_forwarded_for** | [**object**](.md)|  | [optional] 
 **x_account_id** | [**object**](.md)|  | [optional] 
 **environment** | [**object**](.md)|  | [optional] [default to PROD]

### Return type

[**ProductDateModifiedResponseV100**](ProductDateModifiedResponseV100.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBasic](../README.md#HTTPBasic), [OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_date_modified_v200**
> ProductDateModifiedResponseV200 get_product_date_modified_v200(since, supplier_code, body=body, x_forwarded_for=x_forwarded_for, x_account_id=x_account_id, environment=environment)

Get Product Date Modified V200

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
api_instance = psrestful.ProductDataApi(psrestful.ApiClient(configuration))
since = NULL  # object | 
supplier_code = NULL  # object | 
body = NULL  # object |  (optional)
x_forwarded_for = NULL  # object |  (optional)
x_account_id = NULL  # object |  (optional)
environment = PROD  # object |  (optional) (default to PROD)

try:
    # Get Product Date Modified V200
    api_response = api_instance.get_product_date_modified_v200(since, supplier_code, body=body,
                                                               x_forwarded_for=x_forwarded_for,
                                                               x_account_id=x_account_id, environment=environment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductDataApi->get_product_date_modified_v200: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **since** | [**object**](.md)|  | 
 **supplier_code** | [**object**](.md)|  | 
 **body** | [**object**](object.md)|  | [optional] 
 **x_forwarded_for** | [**object**](.md)|  | [optional] 
 **x_account_id** | [**object**](.md)|  | [optional] 
 **environment** | [**object**](.md)|  | [optional] [default to PROD]

### Return type

[**ProductDateModifiedResponseV200**](ProductDateModifiedResponseV200.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBasic](../README.md#HTTPBasic), [OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_v200**
> ProductResponseV200 get_product_v200(supplier_code, product_id, body=body, x_forwarded_for=x_forwarded_for, x_account_id=x_account_id, localization_country=localization_country, localization_language=localization_language, environment=environment)

Get Product V200

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
api_instance = psrestful.ProductDataApi(psrestful.ApiClient(configuration))
supplier_code = NULL  # object | 
product_id = NULL  # object | 
body = NULL  # object |  (optional)
x_forwarded_for = NULL  # object |  (optional)
x_account_id = NULL  # object |  (optional)
localization_country = US  # object |  (optional) (default to US)
localization_language = en  # object |  (optional) (default to en)
environment = PROD  # object |  (optional) (default to PROD)

try:
    # Get Product V200
    api_response = api_instance.get_product_v200(supplier_code, product_id, body=body, x_forwarded_for=x_forwarded_for,
                                                 x_account_id=x_account_id, localization_country=localization_country,
                                                 localization_language=localization_language, environment=environment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductDataApi->get_product_v200: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_code** | [**object**](.md)|  | 
 **product_id** | [**object**](.md)|  | 
 **body** | [**object**](object.md)|  | [optional] 
 **x_forwarded_for** | [**object**](.md)|  | [optional] 
 **x_account_id** | [**object**](.md)|  | [optional] 
 **localization_country** | [**object**](.md)|  | [optional] [default to US]
 **localization_language** | [**object**](.md)|  | [optional] [default to en]
 **environment** | [**object**](.md)|  | [optional] [default to PROD]

### Return type

[**ProductResponseV200**](ProductResponseV200.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBasic](../README.md#HTTPBasic), [OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

