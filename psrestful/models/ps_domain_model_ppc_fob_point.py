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

class PsDomainModelPpcFobPoint(object):
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
        'fob_id': 'object',
        'fob_postal_code': 'object',
        'fob_city': 'object',
        'fob_state': 'object',
        'fob_country': 'object',
        'currency_supported_array': 'object',
        'product_array': 'object'
    }

    attribute_map = {
        'fob_id': 'fobId',
        'fob_postal_code': 'fobPostalCode',
        'fob_city': 'fobCity',
        'fob_state': 'fobState',
        'fob_country': 'fobCountry',
        'currency_supported_array': 'CurrencySupportedArray',
        'product_array': 'ProductArray'
    }

    def __init__(self, fob_id=None, fob_postal_code=None, fob_city=None, fob_state=None, fob_country=None, currency_supported_array=None, product_array=None):  # noqa: E501
        """PsDomainModelPpcFobPoint - a model defined in Swagger"""  # noqa: E501
        self._fob_id = None
        self._fob_postal_code = None
        self._fob_city = None
        self._fob_state = None
        self._fob_country = None
        self._currency_supported_array = None
        self._product_array = None
        self.discriminator = None
        self.fob_id = fob_id
        self.fob_postal_code = fob_postal_code
        self.fob_city = fob_city
        self.fob_state = fob_state
        self.fob_country = fob_country
        self.currency_supported_array = currency_supported_array
        self.product_array = product_array

    @property
    def fob_id(self):
        """Gets the fob_id of this PsDomainModelPpcFobPoint.  # noqa: E501


        :return: The fob_id of this PsDomainModelPpcFobPoint.  # noqa: E501
        :rtype: object
        """
        return self._fob_id

    @fob_id.setter
    def fob_id(self, fob_id):
        """Sets the fob_id of this PsDomainModelPpcFobPoint.


        :param fob_id: The fob_id of this PsDomainModelPpcFobPoint.  # noqa: E501
        :type: object
        """
        if fob_id is None:
            raise ValueError("Invalid value for `fob_id`, must not be `None`")  # noqa: E501

        self._fob_id = fob_id

    @property
    def fob_postal_code(self):
        """Gets the fob_postal_code of this PsDomainModelPpcFobPoint.  # noqa: E501


        :return: The fob_postal_code of this PsDomainModelPpcFobPoint.  # noqa: E501
        :rtype: object
        """
        return self._fob_postal_code

    @fob_postal_code.setter
    def fob_postal_code(self, fob_postal_code):
        """Sets the fob_postal_code of this PsDomainModelPpcFobPoint.


        :param fob_postal_code: The fob_postal_code of this PsDomainModelPpcFobPoint.  # noqa: E501
        :type: object
        """
        if fob_postal_code is None:
            raise ValueError("Invalid value for `fob_postal_code`, must not be `None`")  # noqa: E501

        self._fob_postal_code = fob_postal_code

    @property
    def fob_city(self):
        """Gets the fob_city of this PsDomainModelPpcFobPoint.  # noqa: E501


        :return: The fob_city of this PsDomainModelPpcFobPoint.  # noqa: E501
        :rtype: object
        """
        return self._fob_city

    @fob_city.setter
    def fob_city(self, fob_city):
        """Sets the fob_city of this PsDomainModelPpcFobPoint.


        :param fob_city: The fob_city of this PsDomainModelPpcFobPoint.  # noqa: E501
        :type: object
        """
        if fob_city is None:
            raise ValueError("Invalid value for `fob_city`, must not be `None`")  # noqa: E501

        self._fob_city = fob_city

    @property
    def fob_state(self):
        """Gets the fob_state of this PsDomainModelPpcFobPoint.  # noqa: E501


        :return: The fob_state of this PsDomainModelPpcFobPoint.  # noqa: E501
        :rtype: object
        """
        return self._fob_state

    @fob_state.setter
    def fob_state(self, fob_state):
        """Sets the fob_state of this PsDomainModelPpcFobPoint.


        :param fob_state: The fob_state of this PsDomainModelPpcFobPoint.  # noqa: E501
        :type: object
        """
        if fob_state is None:
            raise ValueError("Invalid value for `fob_state`, must not be `None`")  # noqa: E501

        self._fob_state = fob_state

    @property
    def fob_country(self):
        """Gets the fob_country of this PsDomainModelPpcFobPoint.  # noqa: E501


        :return: The fob_country of this PsDomainModelPpcFobPoint.  # noqa: E501
        :rtype: object
        """
        return self._fob_country

    @fob_country.setter
    def fob_country(self, fob_country):
        """Sets the fob_country of this PsDomainModelPpcFobPoint.


        :param fob_country: The fob_country of this PsDomainModelPpcFobPoint.  # noqa: E501
        :type: object
        """
        if fob_country is None:
            raise ValueError("Invalid value for `fob_country`, must not be `None`")  # noqa: E501

        self._fob_country = fob_country

    @property
    def currency_supported_array(self):
        """Gets the currency_supported_array of this PsDomainModelPpcFobPoint.  # noqa: E501


        :return: The currency_supported_array of this PsDomainModelPpcFobPoint.  # noqa: E501
        :rtype: object
        """
        return self._currency_supported_array

    @currency_supported_array.setter
    def currency_supported_array(self, currency_supported_array):
        """Sets the currency_supported_array of this PsDomainModelPpcFobPoint.


        :param currency_supported_array: The currency_supported_array of this PsDomainModelPpcFobPoint.  # noqa: E501
        :type: object
        """
        if currency_supported_array is None:
            raise ValueError("Invalid value for `currency_supported_array`, must not be `None`")  # noqa: E501

        self._currency_supported_array = currency_supported_array

    @property
    def product_array(self):
        """Gets the product_array of this PsDomainModelPpcFobPoint.  # noqa: E501


        :return: The product_array of this PsDomainModelPpcFobPoint.  # noqa: E501
        :rtype: object
        """
        return self._product_array

    @product_array.setter
    def product_array(self, product_array):
        """Sets the product_array of this PsDomainModelPpcFobPoint.


        :param product_array: The product_array of this PsDomainModelPpcFobPoint.  # noqa: E501
        :type: object
        """
        if product_array is None:
            raise ValueError("Invalid value for `product_array`, must not be `None`")  # noqa: E501

        self._product_array = product_array

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
        if issubclass(PsDomainModelPpcFobPoint, dict):
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
        if not isinstance(other, PsDomainModelPpcFobPoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other