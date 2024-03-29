# coding: utf-8

"""
    PS RESTful Service API

    A proxy service for PromoStandards SOAP to a REST API  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from psrestful.api_client import ApiClient


class PurchaseOrderApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_supported_order_types(self, supplier_code, **kwargs):  # noqa: E501
        """Get Supported Order Types  # noqa: E501

        This function returns the supported Order Types the vendor accepts.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_supported_order_types(supplier_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object supplier_code: (required)
        :param object body:
        :param object x_forwarded_for:
        :param object x_account_id:
        :param object environment:
        :return: GetSupportedOrderTypesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_supported_order_types_with_http_info(supplier_code, **kwargs)  # noqa: E501
        else:
            (data) = self.get_supported_order_types_with_http_info(supplier_code, **kwargs)  # noqa: E501
            return data

    def get_supported_order_types_with_http_info(self, supplier_code, **kwargs):  # noqa: E501
        """Get Supported Order Types  # noqa: E501

        This function returns the supported Order Types the vendor accepts.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_supported_order_types_with_http_info(supplier_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object supplier_code: (required)
        :param object body:
        :param object x_forwarded_for:
        :param object x_account_id:
        :param object environment:
        :return: GetSupportedOrderTypesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['supplier_code', 'body', 'x_forwarded_for', 'x_account_id', 'environment']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_supported_order_types" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'supplier_code' is set
        if ('supplier_code' not in params or
                params['supplier_code'] is None):
            raise ValueError("Missing the required parameter `supplier_code` when calling `get_supported_order_types`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'supplier_code' in params:
            path_params['supplier_code'] = params['supplier_code']  # noqa: E501

        query_params = []
        if 'environment' in params:
            query_params.append(('environment', params['environment']))  # noqa: E501

        header_params = {}
        if 'x_forwarded_for' in params:
            header_params['X-Forwarded-For'] = params['x_forwarded_for']  # noqa: E501
        if 'x_account_id' in params:
            header_params['x-account-id'] = params['x_account_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader', 'HTTPBasic', 'OAuth2PasswordBearer']  # noqa: E501

        return self.api_client.call_api(
            '/v1.0.0/suppliers/{supplier_code}/supported-order-types/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetSupportedOrderTypesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def send_po(self, body, supplier_code, **kwargs):  # noqa: E501
        """Send Po  # noqa: E501

        This function will send blank, sample, simple or configured purchase order to a supplier. The purchase order service is designed to work in conjunction with data from PPC service  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.send_po(body, supplier_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BodySendPo body: (required)
        :param object supplier_code: (required)
        :param object x_forwarded_for:
        :param object x_account_id:
        :return: SendPOResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.send_po_with_http_info(body, supplier_code, **kwargs)  # noqa: E501
        else:
            (data) = self.send_po_with_http_info(body, supplier_code, **kwargs)  # noqa: E501
            return data

    def send_po_with_http_info(self, body, supplier_code, **kwargs):  # noqa: E501
        """Send Po  # noqa: E501

        This function will send blank, sample, simple or configured purchase order to a supplier. The purchase order service is designed to work in conjunction with data from PPC service  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.send_po_with_http_info(body, supplier_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BodySendPo body: (required)
        :param object supplier_code: (required)
        :param object x_forwarded_for:
        :param object x_account_id:
        :return: SendPOResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'supplier_code', 'x_forwarded_for', 'x_account_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method send_po" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `send_po`")  # noqa: E501
        # verify the required parameter 'supplier_code' is set
        if ('supplier_code' not in params or
                params['supplier_code'] is None):
            raise ValueError("Missing the required parameter `supplier_code` when calling `send_po`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'supplier_code' in params:
            path_params['supplier_code'] = params['supplier_code']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_forwarded_for' in params:
            header_params['X-Forwarded-For'] = params['x_forwarded_for']  # noqa: E501
        if 'x_account_id' in params:
            header_params['x-account-id'] = params['x_account_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader', 'HTTPBasic', 'OAuth2PasswordBearer']  # noqa: E501

        return self.api_client.call_api(
            '/v1.0.0/suppliers/{supplier_code}/purchase-orders/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SendPOResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
