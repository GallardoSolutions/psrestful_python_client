# swagger_client.ProductPriceAndConfigurationApi

All URIs are relative to *https://api.psrestful.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_available_charges**](ProductPriceAndConfigurationApi.md#get_available_charges) | **GET** /v1.0.0/suppliers/{supplier_code}/available-charges/{product_id} | Get Available Charges
[**get_available_locations**](ProductPriceAndConfigurationApi.md#get_available_locations) | **GET** /v1.0.0/suppliers/{supplier_code}/available-locations/{product_id} | Get Available Locations
[**get_configuration_and_pricing**](ProductPriceAndConfigurationApi.md#get_configuration_and_pricing) | **GET** /v1.0.0/suppliers/{supplier_code}/pricing-and-configuration/{product_id} | Get Configuration And Pricing
[**get_decoration_colors**](ProductPriceAndConfigurationApi.md#get_decoration_colors) | **GET** /v1.0.0/suppliers/{supplier_code}/decoration-colors/{product_id} | Get Decoration Colors
[**get_fob_points**](ProductPriceAndConfigurationApi.md#get_fob_points) | **GET** /v1.0.0/suppliers/{supplier_code}/fob-points/{product_id} | Get Fob Points

# **get_available_charges**
> AvailableChargesResponse get_available_charges(supplier_code, product_id, body=body, x_forwarded_for=x_forwarded_for, x_account_id=x_account_id, localization_country=localization_country, localization_language=localization_language, environment=environment)

Get Available Charges

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
api_instance = psrestful.ProductPriceAndConfigurationApi(psrestful.ApiClient(configuration))
supplier_code = NULL  # object | 
product_id = NULL  # object | 
body = NULL  # object |  (optional)
x_forwarded_for = NULL  # object |  (optional)
x_account_id = NULL  # object |  (optional)
localization_country = US  # object |  (optional) (default to US)
localization_language = en  # object |  (optional) (default to en)
environment = PROD  # object |  (optional) (default to PROD)

try:
    # Get Available Charges
    api_response = api_instance.get_available_charges(supplier_code, product_id, body=body,
                                                      x_forwarded_for=x_forwarded_for, x_account_id=x_account_id,
                                                      localization_country=localization_country,
                                                      localization_language=localization_language,
                                                      environment=environment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductPriceAndConfigurationApi->get_available_charges: %s\n" % e)
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

[**AvailableChargesResponse**](AvailableChargesResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBasic](../README.md#HTTPBasic), [OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_locations**
> AvailableLocationsResponse get_available_locations(supplier_code, product_id, body=body, x_forwarded_for=x_forwarded_for, x_account_id=x_account_id, localization_country=localization_country, localization_language=localization_language, environment=environment)

Get Available Locations

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
api_instance = psrestful.ProductPriceAndConfigurationApi(psrestful.ApiClient(configuration))
supplier_code = NULL  # object | 
product_id = NULL  # object | 
body = NULL  # object |  (optional)
x_forwarded_for = NULL  # object |  (optional)
x_account_id = NULL  # object |  (optional)
localization_country = US  # object |  (optional) (default to US)
localization_language = en  # object |  (optional) (default to en)
environment = PROD  # object |  (optional) (default to PROD)

try:
    # Get Available Locations
    api_response = api_instance.get_available_locations(supplier_code, product_id, body=body,
                                                        x_forwarded_for=x_forwarded_for, x_account_id=x_account_id,
                                                        localization_country=localization_country,
                                                        localization_language=localization_language,
                                                        environment=environment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductPriceAndConfigurationApi->get_available_locations: %s\n" % e)
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

[**AvailableLocationsResponse**](AvailableLocationsResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBasic](../README.md#HTTPBasic), [OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_configuration_and_pricing**
> ConfigurationAndPricingResponse get_configuration_and_pricing(currency, fob_id, price_type, supplier_code, product_id, body=body, x_forwarded_for=x_forwarded_for, x_account_id=x_account_id, configuration_type=configuration_type, part_id=part_id, localization_country=localization_country, localization_language=localization_language, environment=environment)

Get Configuration And Pricing

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
api_instance = psrestful.ProductPriceAndConfigurationApi(psrestful.ApiClient(configuration))
currency = NULL  # object | 
fob_id = NULL  # object | 
price_type = psrestful.PriceType()  # PriceType | 
supplier_code = NULL  # object | 
product_id = NULL  # object | 
body = NULL  # object |  (optional)
x_forwarded_for = NULL  # object |  (optional)
x_account_id = NULL  # object |  (optional)
configuration_type = Decorated  # object |  (optional) (default to Decorated)
part_id = NULL  # object |  (optional)
localization_country = US  # object |  (optional) (default to US)
localization_language = en  # object |  (optional) (default to en)
environment = PROD  # object |  (optional) (default to PROD)

try:
    # Get Configuration And Pricing
    api_response = api_instance.get_configuration_and_pricing(currency, fob_id, price_type, supplier_code, product_id,
                                                              body=body, x_forwarded_for=x_forwarded_for,
                                                              x_account_id=x_account_id,
                                                              configuration_type=configuration_type, part_id=part_id,
                                                              localization_country=localization_country,
                                                              localization_language=localization_language,
                                                              environment=environment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductPriceAndConfigurationApi->get_configuration_and_pricing: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | [**object**](.md)|  | 
 **fob_id** | [**object**](.md)|  | 
 **price_type** | [**PriceType**](.md)|  | 
 **supplier_code** | [**object**](.md)|  | 
 **product_id** | [**object**](.md)|  | 
 **body** | [**object**](object.md)|  | [optional] 
 **x_forwarded_for** | [**object**](.md)|  | [optional] 
 **x_account_id** | [**object**](.md)|  | [optional] 
 **configuration_type** | [**object**](.md)|  | [optional] [default to Decorated]
 **part_id** | [**object**](.md)|  | [optional] 
 **localization_country** | [**object**](.md)|  | [optional] [default to US]
 **localization_language** | [**object**](.md)|  | [optional] [default to en]
 **environment** | [**object**](.md)|  | [optional] [default to PROD]

### Return type

[**ConfigurationAndPricingResponse**](ConfigurationAndPricingResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBasic](../README.md#HTTPBasic), [OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_decoration_colors**
> DecorationColorResponse get_decoration_colors(location_id, supplier_code, product_id, body=body, x_forwarded_for=x_forwarded_for, x_account_id=x_account_id, decoration_id=decoration_id, localization_country=localization_country, localization_language=localization_language, environment=environment)

Get Decoration Colors

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
api_instance = psrestful.ProductPriceAndConfigurationApi(psrestful.ApiClient(configuration))
location_id = NULL  # object | 
supplier_code = NULL  # object | 
product_id = NULL  # object | 
body = NULL  # object |  (optional)
x_forwarded_for = NULL  # object |  (optional)
x_account_id = NULL  # object |  (optional)
decoration_id = NULL  # object |  (optional)
localization_country = US  # object |  (optional) (default to US)
localization_language = en  # object |  (optional) (default to en)
environment = PROD  # object |  (optional) (default to PROD)

try:
    # Get Decoration Colors
    api_response = api_instance.get_decoration_colors(location_id, supplier_code, product_id, body=body,
                                                      x_forwarded_for=x_forwarded_for, x_account_id=x_account_id,
                                                      decoration_id=decoration_id,
                                                      localization_country=localization_country,
                                                      localization_language=localization_language,
                                                      environment=environment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductPriceAndConfigurationApi->get_decoration_colors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | [**object**](.md)|  | 
 **supplier_code** | [**object**](.md)|  | 
 **product_id** | [**object**](.md)|  | 
 **body** | [**object**](object.md)|  | [optional] 
 **x_forwarded_for** | [**object**](.md)|  | [optional] 
 **x_account_id** | [**object**](.md)|  | [optional] 
 **decoration_id** | [**object**](.md)|  | [optional] 
 **localization_country** | [**object**](.md)|  | [optional] [default to US]
 **localization_language** | [**object**](.md)|  | [optional] [default to en]
 **environment** | [**object**](.md)|  | [optional] [default to PROD]

### Return type

[**DecorationColorResponse**](DecorationColorResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBasic](../README.md#HTTPBasic), [OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fob_points**
> FobPointsResponse get_fob_points(supplier_code, product_id, body=body, x_forwarded_for=x_forwarded_for, x_account_id=x_account_id, localization_country=localization_country, localization_language=localization_language, environment=environment)

Get Fob Points

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
api_instance = psrestful.ProductPriceAndConfigurationApi(psrestful.ApiClient(configuration))
supplier_code = NULL  # object | 
product_id = NULL  # object | 
body = NULL  # object |  (optional)
x_forwarded_for = NULL  # object |  (optional)
x_account_id = NULL  # object |  (optional)
localization_country = US  # object |  (optional) (default to US)
localization_language = en  # object |  (optional) (default to en)
environment = PROD  # object |  (optional) (default to PROD)

try:
    # Get Fob Points
    api_response = api_instance.get_fob_points(supplier_code, product_id, body=body, x_forwarded_for=x_forwarded_for,
                                               x_account_id=x_account_id, localization_country=localization_country,
                                               localization_language=localization_language, environment=environment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductPriceAndConfigurationApi->get_fob_points: %s\n" % e)
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

[**FobPointsResponse**](FobPointsResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBasic](../README.md#HTTPBasic), [OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

