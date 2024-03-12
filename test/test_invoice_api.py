# coding: utf-8

"""
    PS RESTful Service API

    A proxy service for PromoStandards SOAP to a REST API  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import psrestful
from psrestful.api.invoice_api import InvoiceApi  # noqa: E501
from psrestful.rest import ApiException


class TestInvoiceApi(unittest.TestCase):
    """InvoiceApi unit test stubs"""

    def setUp(self):
        self.api = InvoiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_invoices(self):
        """Test case for get_invoices

        Get Invoices  # noqa: E501
        """
        pass

    def test_get_voided_invoices(self):
        """Test case for get_voided_invoices

        Get Voided Invoices  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()