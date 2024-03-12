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

class ProductDateModifiedResponseV100(object):
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
        'product_date_modified_array': 'object',
        'error_message': 'object'
    }

    attribute_map = {
        'product_date_modified_array': 'ProductDateModifiedArray',
        'error_message': 'ErrorMessage'
    }

    def __init__(self, product_date_modified_array=None, error_message=None):  # noqa: E501
        """ProductDateModifiedResponseV100 - a model defined in Swagger"""  # noqa: E501
        self._product_date_modified_array = None
        self._error_message = None
        self.discriminator = None
        self.product_date_modified_array = product_date_modified_array
        if error_message is not None:
            self.error_message = error_message

    @property
    def product_date_modified_array(self):
        """Gets the product_date_modified_array of this ProductDateModifiedResponseV100.  # noqa: E501


        :return: The product_date_modified_array of this ProductDateModifiedResponseV100.  # noqa: E501
        :rtype: object
        """
        return self._product_date_modified_array

    @product_date_modified_array.setter
    def product_date_modified_array(self, product_date_modified_array):
        """Sets the product_date_modified_array of this ProductDateModifiedResponseV100.


        :param product_date_modified_array: The product_date_modified_array of this ProductDateModifiedResponseV100.  # noqa: E501
        :type: object
        """
        if product_date_modified_array is None:
            raise ValueError("Invalid value for `product_date_modified_array`, must not be `None`")  # noqa: E501

        self._product_date_modified_array = product_date_modified_array

    @property
    def error_message(self):
        """Gets the error_message of this ProductDateModifiedResponseV100.  # noqa: E501


        :return: The error_message of this ProductDateModifiedResponseV100.  # noqa: E501
        :rtype: object
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this ProductDateModifiedResponseV100.


        :param error_message: The error_message of this ProductDateModifiedResponseV100.  # noqa: E501
        :type: object
        """

        self._error_message = error_message

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
        if issubclass(ProductDateModifiedResponseV100, dict):
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
        if not isinstance(other, ProductDateModifiedResponseV100):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
