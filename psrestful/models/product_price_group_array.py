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

class ProductPriceGroupArray(object):
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
        'product_price_group': 'object'
    }

    attribute_map = {
        'product_price_group': 'ProductPriceGroup'
    }

    def __init__(self, product_price_group=None):  # noqa: E501
        """ProductPriceGroupArray - a model defined in Swagger"""  # noqa: E501
        self._product_price_group = None
        self.discriminator = None
        self.product_price_group = product_price_group

    @property
    def product_price_group(self):
        """Gets the product_price_group of this ProductPriceGroupArray.  # noqa: E501


        :return: The product_price_group of this ProductPriceGroupArray.  # noqa: E501
        :rtype: object
        """
        return self._product_price_group

    @product_price_group.setter
    def product_price_group(self, product_price_group):
        """Sets the product_price_group of this ProductPriceGroupArray.


        :param product_price_group: The product_price_group of this ProductPriceGroupArray.  # noqa: E501
        :type: object
        """
        if product_price_group is None:
            raise ValueError("Invalid value for `product_price_group`, must not be `None`")  # noqa: E501

        self._product_price_group = product_price_group

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
        if issubclass(ProductPriceGroupArray, dict):
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
        if not isinstance(other, ProductPriceGroupArray):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other