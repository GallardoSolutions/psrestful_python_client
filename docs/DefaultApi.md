# swagger_client.DefaultApi

All URIs are relative to *https://api.psrestful.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_service_codes**](DefaultApi.md#get_service_codes) | **GET** /service-codes | Get Service Codes
[**get_services**](DefaultApi.md#get_services) | **GET** /services/{supplier_code} | Get Services

# **get_service_codes**
> object get_service_codes()

Get Service Codes

### Example

```python
from __future__ import print_function
import time
import psrestful
from psrestful.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = psrestful.DefaultApi()

try:
    # Get Service Codes
    api_response = api_instance.get_service_codes()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_service_codes: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_services**
> object get_services(supplier_code)

Get Services

### Example

```python
from __future__ import print_function
import time
import psrestful
from psrestful.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = psrestful.DefaultApi()
supplier_code = NULL  # object | 

try:
    # Get Services
    api_response = api_instance.get_services(supplier_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_services: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_code** | [**object**](.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

