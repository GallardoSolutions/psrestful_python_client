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

class ConfigurationOutput(object):
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
        'part_array': 'object',
        'location_array': 'object',
        'product_id': 'object',
        'currency': 'object',
        'fob_array': 'object',
        'fob_postal_code': 'object',
        'price_type': 'PriceType'
    }

    attribute_map = {
        'part_array': 'PartArray',
        'location_array': 'LocationArray',
        'product_id': 'productId',
        'currency': 'currency',
        'fob_array': 'FobArray',
        'fob_postal_code': 'fobPostalCode',
        'price_type': 'priceType'
    }

    def __init__(self, part_array=None, location_array=None, product_id=None, currency=None, fob_array=None, fob_postal_code=None, price_type=None):  # noqa: E501
        """ConfigurationOutput - a model defined in Swagger"""  # noqa: E501
        self._part_array = None
        self._location_array = None
        self._product_id = None
        self._currency = None
        self._fob_array = None
        self._fob_postal_code = None
        self._price_type = None
        self.discriminator = None
        self.part_array = part_array
        self.location_array = location_array
        if product_id is not None:
            self.product_id = product_id
        self.currency = currency
        self.fob_array = fob_array
        if fob_postal_code is not None:
            self.fob_postal_code = fob_postal_code
        self.price_type = price_type

    @property
    def part_array(self):
        """Gets the part_array of this ConfigurationOutput.  # noqa: E501


        :return: The part_array of this ConfigurationOutput.  # noqa: E501
        :rtype: object
        """
        return self._part_array

    @part_array.setter
    def part_array(self, part_array):
        """Sets the part_array of this ConfigurationOutput.


        :param part_array: The part_array of this ConfigurationOutput.  # noqa: E501
        :type: object
        """
        if part_array is None:
            raise ValueError("Invalid value for `part_array`, must not be `None`")  # noqa: E501

        self._part_array = part_array

    @property
    def location_array(self):
        """Gets the location_array of this ConfigurationOutput.  # noqa: E501


        :return: The location_array of this ConfigurationOutput.  # noqa: E501
        :rtype: object
        """
        return self._location_array

    @location_array.setter
    def location_array(self, location_array):
        """Sets the location_array of this ConfigurationOutput.


        :param location_array: The location_array of this ConfigurationOutput.  # noqa: E501
        :type: object
        """
        if location_array is None:
            raise ValueError("Invalid value for `location_array`, must not be `None`")  # noqa: E501

        self._location_array = location_array

    @property
    def product_id(self):
        """Gets the product_id of this ConfigurationOutput.  # noqa: E501


        :return: The product_id of this ConfigurationOutput.  # noqa: E501
        :rtype: object
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this ConfigurationOutput.


        :param product_id: The product_id of this ConfigurationOutput.  # noqa: E501
        :type: object
        """

        self._product_id = product_id

    @property
    def currency(self):
        """Gets the currency of this ConfigurationOutput.  # noqa: E501


        :return: The currency of this ConfigurationOutput.  # noqa: E501
        :rtype: object
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this ConfigurationOutput.


        :param currency: The currency of this ConfigurationOutput.  # noqa: E501
        :type: object
        """
        if currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def fob_array(self):
        """Gets the fob_array of this ConfigurationOutput.  # noqa: E501


        :return: The fob_array of this ConfigurationOutput.  # noqa: E501
        :rtype: object
        """
        return self._fob_array

    @fob_array.setter
    def fob_array(self, fob_array):
        """Sets the fob_array of this ConfigurationOutput.


        :param fob_array: The fob_array of this ConfigurationOutput.  # noqa: E501
        :type: object
        """
        if fob_array is None:
            raise ValueError("Invalid value for `fob_array`, must not be `None`")  # noqa: E501

        self._fob_array = fob_array

    @property
    def fob_postal_code(self):
        """Gets the fob_postal_code of this ConfigurationOutput.  # noqa: E501


        :return: The fob_postal_code of this ConfigurationOutput.  # noqa: E501
        :rtype: object
        """
        return self._fob_postal_code

    @fob_postal_code.setter
    def fob_postal_code(self, fob_postal_code):
        """Sets the fob_postal_code of this ConfigurationOutput.


        :param fob_postal_code: The fob_postal_code of this ConfigurationOutput.  # noqa: E501
        :type: object
        """

        self._fob_postal_code = fob_postal_code

    @property
    def price_type(self):
        """Gets the price_type of this ConfigurationOutput.  # noqa: E501


        :return: The price_type of this ConfigurationOutput.  # noqa: E501
        :rtype: PriceType
        """
        return self._price_type

    @price_type.setter
    def price_type(self, price_type):
        """Sets the price_type of this ConfigurationOutput.


        :param price_type: The price_type of this ConfigurationOutput.  # noqa: E501
        :type: PriceType
        """
        if price_type is None:
            raise ValueError("Invalid value for `price_type`, must not be `None`")  # noqa: E501

        self._price_type = price_type

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
        if issubclass(ConfigurationOutput, dict):
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
        if not isinstance(other, ConfigurationOutput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
