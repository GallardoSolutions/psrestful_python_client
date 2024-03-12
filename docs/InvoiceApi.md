# swagger_client.InvoiceApi

All URIs are relative to *https://api.psrestful.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_invoices**](InvoiceApi.md#get_invoices) | **GET** /v1.0.0/suppliers/{supplier_code}/invoices/ | Get Invoices
[**get_voided_invoices**](InvoiceApi.md#get_voided_invoices) | **GET** /v1.0.0/suppliers/{supplier_code}/voided-invoices/ | Get Voided Invoices

# **get_invoices**
> GetInvoiceResponse get_invoices(query_type, supplier_code, body=body, x_forwarded_for=x_forwarded_for, x_account_id=x_account_id, reference_number=reference_number, requested_date=requested_date, available_timestamp=available_timestamp, environment=environment)

Get Invoices

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
api_instance = psrestful.InvoiceApi(psrestful.ApiClient(configuration))
query_type = psrestful.PsDomainModelInvoiceQueryType()  # PsDomainModelInvoiceQueryType | 
supplier_code = NULL  # object | 
body = NULL  # object |  (optional)
x_forwarded_for = NULL  # object |  (optional)
x_account_id = NULL  # object |  (optional)
reference_number = NULL  # object |  (optional)
requested_date = NULL  # object |  (optional)
available_timestamp = NULL  # object |  (optional)
environment = PROD  # object |  (optional) (default to PROD)

try:
    # Get Invoices
    api_response = api_instance.get_invoices(query_type, supplier_code, body=body, x_forwarded_for=x_forwarded_for,
                                             x_account_id=x_account_id, reference_number=reference_number,
                                             requested_date=requested_date, available_timestamp=available_timestamp,
                                             environment=environment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoiceApi->get_invoices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_type** | [**PsDomainModelInvoiceQueryType**](.md)|  | 
 **supplier_code** | [**object**](.md)|  | 
 **body** | [**object**](object.md)|  | [optional] 
 **x_forwarded_for** | [**object**](.md)|  | [optional] 
 **x_account_id** | [**object**](.md)|  | [optional] 
 **reference_number** | [**object**](.md)|  | [optional] 
 **requested_date** | [**object**](.md)|  | [optional] 
 **available_timestamp** | [**object**](.md)|  | [optional] 
 **environment** | [**object**](.md)|  | [optional] [default to PROD]

### Return type

[**GetInvoiceResponse**](GetInvoiceResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBasic](../README.md#HTTPBasic), [OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_voided_invoices**
> GetVoidedResponse get_voided_invoices(query_type, supplier_code, body=body, x_forwarded_for=x_forwarded_for, x_account_id=x_account_id, reference_number=reference_number, requested_date=requested_date, available_timestamp=available_timestamp, environment=environment)

Get Voided Invoices

This endpoint is used to retrieve a list of voided invoices. When QueryType=1(PO_NUMBER_SEARCH) or 2(INVOICE_NUMBER_SEARCH) reference_number must be filled in.

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
api_instance = psrestful.InvoiceApi(psrestful.ApiClient(configuration))
query_type = psrestful.PsDomainModelInvoiceQueryType()  # PsDomainModelInvoiceQueryType | 
supplier_code = NULL  # object | 
body = NULL  # object |  (optional)
x_forwarded_for = NULL  # object |  (optional)
x_account_id = NULL  # object |  (optional)
reference_number = NULL  # object |  (optional)
requested_date = NULL  # object |  (optional)
available_timestamp = NULL  # object |  (optional)
environment = PROD  # object |  (optional) (default to PROD)

try:
    # Get Voided Invoices
    api_response = api_instance.get_voided_invoices(query_type, supplier_code, body=body,
                                                    x_forwarded_for=x_forwarded_for, x_account_id=x_account_id,
                                                    reference_number=reference_number, requested_date=requested_date,
                                                    available_timestamp=available_timestamp, environment=environment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoiceApi->get_voided_invoices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_type** | [**PsDomainModelInvoiceQueryType**](.md)|  | 
 **supplier_code** | [**object**](.md)|  | 
 **body** | [**object**](object.md)|  | [optional] 
 **x_forwarded_for** | [**object**](.md)|  | [optional] 
 **x_account_id** | [**object**](.md)|  | [optional] 
 **reference_number** | [**object**](.md)|  | [optional] 
 **requested_date** | [**object**](.md)|  | [optional] 
 **available_timestamp** | [**object**](.md)|  | [optional] 
 **environment** | [**object**](.md)|  | [optional] [default to PROD]

### Return type

[**GetVoidedResponse**](GetVoidedResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBasic](../README.md#HTTPBasic), [OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

