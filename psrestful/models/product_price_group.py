# coding: utf-8

"""
    PS RESTful Service API

    A proxy service for PromoStandards SOAP to a REST API  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ProductPriceGroup(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'group_name': 'object',
        'currency': 'object',
        'description': 'object',
        'product_price_array': 'ProductPriceArray'
    }

    attribute_map = {
        'group_name': 'groupName',
        'currency': 'currency',
        'description': 'description',
        'product_price_array': 'ProductPriceArray'
    }

    def __init__(self, group_name=None, currency=None, description=None, product_price_array=None):  # noqa: E501
        """ProductPriceGroup - a model defined in Swagger"""  # noqa: E501
        self._group_name = None
        self._currency = None
        self._description = None
        self._product_price_array = None
        self.discriminator = None
        self.group_name = group_name
        self.currency = currency
        self.description = description
        self.product_price_array = product_price_array

    @property
    def group_name(self):
        """Gets the group_name of this ProductPriceGroup.  # noqa: E501


        :return: The group_name of this ProductPriceGroup.  # noqa: E501
        :rtype: object
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this ProductPriceGroup.


        :param group_name: The group_name of this ProductPriceGroup.  # noqa: E501
        :type: object
        """
        if group_name is None:
            raise ValueError("Invalid value for `group_name`, must not be `None`")  # noqa: E501

        self._group_name = group_name

    @property
    def currency(self):
        """Gets the currency of this ProductPriceGroup.  # noqa: E501


        :return: The currency of this ProductPriceGroup.  # noqa: E501
        :rtype: object
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this ProductPriceGroup.


        :param currency: The currency of this ProductPriceGroup.  # noqa: E501
        :type: object
        """
        if currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def description(self):
        """Gets the description of this ProductPriceGroup.  # noqa: E501


        :return: The description of this ProductPriceGroup.  # noqa: E501
        :rtype: object
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ProductPriceGroup.


        :param description: The description of this ProductPriceGroup.  # noqa: E501
        :type: object
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def product_price_array(self):
        """Gets the product_price_array of this ProductPriceGroup.  # noqa: E501


        :return: The product_price_array of this ProductPriceGroup.  # noqa: E501
        :rtype: ProductPriceArray
        """
        return self._product_price_array

    @product_price_array.setter
    def product_price_array(self, product_price_array):
        """Sets the product_price_array of this ProductPriceGroup.


        :param product_price_array: The product_price_array of this ProductPriceGroup.  # noqa: E501
        :type: ProductPriceArray
        """
        if product_price_array is None:
            raise ValueError("Invalid value for `product_price_array`, must not be `None`")  # noqa: E501

        self._product_price_array = product_price_array

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ProductPriceGroup, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ProductPriceGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other