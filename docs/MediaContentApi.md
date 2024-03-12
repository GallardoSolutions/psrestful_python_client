# swagger_client.MediaContentApi

All URIs are relative to *https://api.psrestful.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_media_content**](MediaContentApi.md#get_media_content) | **GET** /v1.1.0/suppliers/{supplier_code}/medias/{product_id} | Get Media Content
[**get_media_date_modified**](MediaContentApi.md#get_media_date_modified) | **GET** /v1.1.0/suppliers/{supplier_code}/media-modified-since/ | Get Media Date Modified

# **get_media_content**
> MediaContentDetailsResponse get_media_content(supplier_code, product_id, body=body, x_forwarded_for=x_forwarded_for, x_account_id=x_account_id, culture_name=culture_name, media_type=media_type, part_id=part_id, class_type=class_type, environment=environment)

Get Media Content

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
api_instance = psrestful.MediaContentApi(psrestful.ApiClient(configuration))
supplier_code = NULL  # object | 
product_id = NULL  # object | 
body = NULL  # object |  (optional)
x_forwarded_for = NULL  # object |  (optional)
x_account_id = NULL  # object |  (optional)
culture_name = NULL  # object | The language culture name.  This tailors the response to a specific culture. i.e. language, units of measure, etc. Null assumes en-US. Valid values follows `ISO 639x`, ex: en-US, en-GB, fr-FR, etc. (optional)
media_type = Image  # object |  (optional) (default to Image)
part_id = NULL  # object |  (optional)
class_type = NULL  # object |  (optional)
environment = PROD  # object |  (optional) (default to PROD)

try:
    # Get Media Content
    api_response = api_instance.get_media_content(supplier_code, product_id, body=body, x_forwarded_for=x_forwarded_for,
                                                  x_account_id=x_account_id, culture_name=culture_name,
                                                  media_type=media_type, part_id=part_id, class_type=class_type,
                                                  environment=environment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaContentApi->get_media_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_code** | [**object**](.md)|  | 
 **product_id** | [**object**](.md)|  | 
 **body** | [**object**](object.md)|  | [optional] 
 **x_forwarded_for** | [**object**](.md)|  | [optional] 
 **x_account_id** | [**object**](.md)|  | [optional] 
 **culture_name** | [**object**](.md)| The language culture name.  This tailors the response to a specific culture. i.e. language, units of measure, etc. Null assumes en-US. Valid values follows &#x60;ISO 639x&#x60;, ex: en-US, en-GB, fr-FR, etc. | [optional] 
 **media_type** | [**object**](.md)|  | [optional] [default to Image]
 **part_id** | [**object**](.md)|  | [optional] 
 **class_type** | [**object**](.md)|  | [optional] 
 **environment** | [**object**](.md)|  | [optional] [default to PROD]

### Return type

[**MediaContentDetailsResponse**](MediaContentDetailsResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBasic](../README.md#HTTPBasic), [OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_media_date_modified**
> GetMediaDateModifiedResponse get_media_date_modified(supplier_code, body=body, x_forwarded_for=x_forwarded_for, x_account_id=x_account_id, culture_name=culture_name, since=since, environment=environment)

Get Media Date Modified

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
api_instance = psrestful.MediaContentApi(psrestful.ApiClient(configuration))
supplier_code = NULL  # object | 
body = NULL  # object |  (optional)
x_forwarded_for = NULL  # object |  (optional)
x_account_id = NULL  # object |  (optional)
culture_name = us_en  # object | The language culture name. (optional) (default to us_en)
since = NULL  # object |  (optional)
environment = PROD  # object |  (optional) (default to PROD)

try:
    # Get Media Date Modified
    api_response = api_instance.get_media_date_modified(supplier_code, body=body, x_forwarded_for=x_forwarded_for,
                                                        x_account_id=x_account_id, culture_name=culture_name,
                                                        since=since, environment=environment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaContentApi->get_media_date_modified: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_code** | [**object**](.md)|  | 
 **body** | [**object**](object.md)|  | [optional] 
 **x_forwarded_for** | [**object**](.md)|  | [optional] 
 **x_account_id** | [**object**](.md)|  | [optional] 
 **culture_name** | [**object**](.md)| The language culture name. | [optional] [default to us_en]
 **since** | [**object**](.md)|  | [optional] 
 **environment** | [**object**](.md)|  | [optional] [default to PROD]

### Return type

[**GetMediaDateModifiedResponse**](GetMediaDateModifiedResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBasic](../README.md#HTTPBasic), [OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

