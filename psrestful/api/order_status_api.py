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


class OrderStatusApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_issue_v200(self, supplier_code, issue_id, **kwargs):  # noqa: E501
        """Get Issue  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_issue_v200(supplier_code, issue_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object supplier_code: (required)
        :param object issue_id: (required)
        :param object body:
        :param object x_forwarded_for:
        :param object x_account_id:
        :param object environment:
        :return: GetIssueResponseV200
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_issue_v200_with_http_info(supplier_code, issue_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_issue_v200_with_http_info(supplier_code, issue_id, **kwargs)  # noqa: E501
            return data

    def get_issue_v200_with_http_info(self, supplier_code, issue_id, **kwargs):  # noqa: E501
        """Get Issue  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_issue_v200_with_http_info(supplier_code, issue_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object supplier_code: (required)
        :param object issue_id: (required)
        :param object body:
        :param object x_forwarded_for:
        :param object x_account_id:
        :param object environment:
        :return: GetIssueResponseV200
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['supplier_code', 'issue_id', 'body', 'x_forwarded_for', 'x_account_id', 'environment']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_issue_v200" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'supplier_code' is set
        if ('supplier_code' not in params or
                params['supplier_code'] is None):
            raise ValueError("Missing the required parameter `supplier_code` when calling `get_issue_v200`")  # noqa: E501
        # verify the required parameter 'issue_id' is set
        if ('issue_id' not in params or
                params['issue_id'] is None):
            raise ValueError("Missing the required parameter `issue_id` when calling `get_issue_v200`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'supplier_code' in params:
            path_params['supplier_code'] = params['supplier_code']  # noqa: E501
        if 'issue_id' in params:
            path_params['issue_id'] = params['issue_id']  # noqa: E501

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
            '/v2.0.0/suppliers/{supplier_code}/issues/{issue_id}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetIssueResponseV200',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_order_status_details_v100(self, query_type, supplier_code, **kwargs):  # noqa: E501
        """Get Order Status Details  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_order_status_details_v100(query_type, supplier_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PsDomainModelOrderStatusV100QueryType query_type: (required)
        :param object supplier_code: (required)
        :param object body:
        :param object x_forwarded_for:
        :param object x_account_id:
        :param object reference_number:
        :param object status_timestamp:
        :param object environment:
        :return: OrderStatusDetailsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_order_status_details_v100_with_http_info(query_type, supplier_code, **kwargs)  # noqa: E501
        else:
            (data) = self.get_order_status_details_v100_with_http_info(query_type, supplier_code, **kwargs)  # noqa: E501
            return data

    def get_order_status_details_v100_with_http_info(self, query_type, supplier_code, **kwargs):  # noqa: E501
        """Get Order Status Details  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_order_status_details_v100_with_http_info(query_type, supplier_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PsDomainModelOrderStatusV100QueryType query_type: (required)
        :param object supplier_code: (required)
        :param object body:
        :param object x_forwarded_for:
        :param object x_account_id:
        :param object reference_number:
        :param object status_timestamp:
        :param object environment:
        :return: OrderStatusDetailsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query_type', 'supplier_code', 'body', 'x_forwarded_for', 'x_account_id', 'reference_number', 'status_timestamp', 'environment']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_order_status_details_v100" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'query_type' is set
        if ('query_type' not in params or
                params['query_type'] is None):
            raise ValueError("Missing the required parameter `query_type` when calling `get_order_status_details_v100`")  # noqa: E501
        # verify the required parameter 'supplier_code' is set
        if ('supplier_code' not in params or
                params['supplier_code'] is None):
            raise ValueError("Missing the required parameter `supplier_code` when calling `get_order_status_details_v100`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'supplier_code' in params:
            path_params['supplier_code'] = params['supplier_code']  # noqa: E501

        query_params = []
        if 'query_type' in params:
            query_params.append(('query_type', params['query_type']))  # noqa: E501
        if 'reference_number' in params:
            query_params.append(('reference_number', params['reference_number']))  # noqa: E501
        if 'status_timestamp' in params:
            query_params.append(('status_timestamp', params['status_timestamp']))  # noqa: E501
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
            '/v1.0.0/suppliers/{supplier_code}/order-status-details/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OrderStatusDetailsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_order_status_types_v100(self, supplier_code, **kwargs):  # noqa: E501
        """Get Order Status Types  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_order_status_types_v100(supplier_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object supplier_code: (required)
        :param object body:
        :param object x_forwarded_for:
        :param object x_account_id:
        :param object environment:
        :return: OrderStatusTypesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_order_status_types_v100_with_http_info(supplier_code, **kwargs)  # noqa: E501
        else:
            (data) = self.get_order_status_types_v100_with_http_info(supplier_code, **kwargs)  # noqa: E501
            return data

    def get_order_status_types_v100_with_http_info(self, supplier_code, **kwargs):  # noqa: E501
        """Get Order Status Types  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_order_status_types_v100_with_http_info(supplier_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object supplier_code: (required)
        :param object body:
        :param object x_forwarded_for:
        :param object x_account_id:
        :param object environment:
        :return: OrderStatusTypesResponse
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
                    " to method get_order_status_types_v100" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'supplier_code' is set
        if ('supplier_code' not in params or
                params['supplier_code'] is None):
            raise ValueError("Missing the required parameter `supplier_code` when calling `get_order_status_types_v100`")  # noqa: E501

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
            '/v1.0.0/suppliers/{supplier_code}/order-status-types/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OrderStatusTypesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_order_status_v200(self, query_type, supplier_code, **kwargs):  # noqa: E501
        """Get Order Status  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_order_status_v200(query_type, supplier_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PsDomainModelOrderStatusV100QueryType query_type: (required)
        :param object supplier_code: (required)
        :param object body:
        :param object x_forwarded_for:
        :param object x_account_id:
        :param object reference_number:
        :param object status_timestamp:
        :param object environment:
        :return: GetOrderStatusResponseV200
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_order_status_v200_with_http_info(query_type, supplier_code, **kwargs)  # noqa: E501
        else:
            (data) = self.get_order_status_v200_with_http_info(query_type, supplier_code, **kwargs)  # noqa: E501
            return data

    def get_order_status_v200_with_http_info(self, query_type, supplier_code, **kwargs):  # noqa: E501
        """Get Order Status  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_order_status_v200_with_http_info(query_type, supplier_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PsDomainModelOrderStatusV100QueryType query_type: (required)
        :param object supplier_code: (required)
        :param object body:
        :param object x_forwarded_for:
        :param object x_account_id:
        :param object reference_number:
        :param object status_timestamp:
        :param object environment:
        :return: GetOrderStatusResponseV200
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query_type', 'supplier_code', 'body', 'x_forwarded_for', 'x_account_id', 'reference_number', 'status_timestamp', 'environment']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_order_status_v200" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'query_type' is set
        if ('query_type' not in params or
                params['query_type'] is None):
            raise ValueError("Missing the required parameter `query_type` when calling `get_order_status_v200`")  # noqa: E501
        # verify the required parameter 'supplier_code' is set
        if ('supplier_code' not in params or
                params['supplier_code'] is None):
            raise ValueError("Missing the required parameter `supplier_code` when calling `get_order_status_v200`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'supplier_code' in params:
            path_params['supplier_code'] = params['supplier_code']  # noqa: E501

        query_params = []
        if 'query_type' in params:
            query_params.append(('query_type', params['query_type']))  # noqa: E501
        if 'reference_number' in params:
            query_params.append(('reference_number', params['reference_number']))  # noqa: E501
        if 'status_timestamp' in params:
            query_params.append(('status_timestamp', params['status_timestamp']))  # noqa: E501
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
            '/v2.0.0/suppliers/{supplier_code}/order-status/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetOrderStatusResponseV200',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_service_methods_v200(self, supplier_code, **kwargs):  # noqa: E501
        """Get Service Methods  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_service_methods_v200(supplier_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object supplier_code: (required)
        :param object body:
        :param object x_forwarded_for:
        :param object x_account_id:
        :param object environment:
        :return: GetServiceMethodsResponseV200
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_service_methods_v200_with_http_info(supplier_code, **kwargs)  # noqa: E501
        else:
            (data) = self.get_service_methods_v200_with_http_info(supplier_code, **kwargs)  # noqa: E501
            return data

    def get_service_methods_v200_with_http_info(self, supplier_code, **kwargs):  # noqa: E501
        """Get Service Methods  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_service_methods_v200_with_http_info(supplier_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object supplier_code: (required)
        :param object body:
        :param object x_forwarded_for:
        :param object x_account_id:
        :param object environment:
        :return: GetServiceMethodsResponseV200
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
                    " to method get_service_methods_v200" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'supplier_code' is set
        if ('supplier_code' not in params or
                params['supplier_code'] is None):
            raise ValueError("Missing the required parameter `supplier_code` when calling `get_service_methods_v200`")  # noqa: E501

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
            '/v2.0.0/suppliers/{supplier_code}/service-methods/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetServiceMethodsResponseV200',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)