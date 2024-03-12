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
from psrestful.api.inventory_api import InventoryApi  # noqa: E501
from psrestful.rest import ApiException


class TestInventoryApi(unittest.TestCase):
    """InventoryApi unit test stubs"""

    def setUp(self):
        self.api = InventoryApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_filter_values(self):
        """Test case for get_filter_values

        Get Filter Values  # noqa: E501
        """
        pass

    def test_get_inventory_by_product_v121(self):
        """Test case for get_inventory_by_product_v121

        Get Inventory By Product V121  # noqa: E501
        """
        pass

    def test_get_inventory_by_product_v200(self):
        """Test case for get_inventory_by_product_v200

        Get Inventory By Product V200  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()