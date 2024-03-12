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

class DecorationMethodArray(object):
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
        'decoration_method': 'object'
    }

    attribute_map = {
        'decoration_method': 'DecorationMethod'
    }

    def __init__(self, decoration_method=None):  # noqa: E501
        """DecorationMethodArray - a model defined in Swagger"""  # noqa: E501
        self._decoration_method = None
        self.discriminator = None
        self.decoration_method = decoration_method

    @property
    def decoration_method(self):
        """Gets the decoration_method of this DecorationMethodArray.  # noqa: E501


        :return: The decoration_method of this DecorationMethodArray.  # noqa: E501
        :rtype: object
        """
        return self._decoration_method

    @decoration_method.setter
    def decoration_method(self, decoration_method):
        """Sets the decoration_method of this DecorationMethodArray.


        :param decoration_method: The decoration_method of this DecorationMethodArray.  # noqa: E501
        :type: object
        """
        if decoration_method is None:
            raise ValueError("Invalid value for `decoration_method`, must not be `None`")  # noqa: E501

        self._decoration_method = decoration_method

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
        if issubclass(DecorationMethodArray, dict):
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
        if not isinstance(other, DecorationMethodArray):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
