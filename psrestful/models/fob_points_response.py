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

class FobPointsResponse(object):
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
        'fob_point_array': 'object',
        'error_message': 'object'
    }

    attribute_map = {
        'fob_point_array': 'FobPointArray',
        'error_message': 'ErrorMessage'
    }

    def __init__(self, fob_point_array=None, error_message=None):  # noqa: E501
        """FobPointsResponse - a model defined in Swagger"""  # noqa: E501
        self._fob_point_array = None
        self._error_message = None
        self.discriminator = None
        self.fob_point_array = fob_point_array
        self.error_message = error_message

    @property
    def fob_point_array(self):
        """Gets the fob_point_array of this FobPointsResponse.  # noqa: E501


        :return: The fob_point_array of this FobPointsResponse.  # noqa: E501
        :rtype: object
        """
        return self._fob_point_array

    @fob_point_array.setter
    def fob_point_array(self, fob_point_array):
        """Sets the fob_point_array of this FobPointsResponse.


        :param fob_point_array: The fob_point_array of this FobPointsResponse.  # noqa: E501
        :type: object
        """
        if fob_point_array is None:
            raise ValueError("Invalid value for `fob_point_array`, must not be `None`")  # noqa: E501

        self._fob_point_array = fob_point_array

    @property
    def error_message(self):
        """Gets the error_message of this FobPointsResponse.  # noqa: E501


        :return: The error_message of this FobPointsResponse.  # noqa: E501
        :rtype: object
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this FobPointsResponse.


        :param error_message: The error_message of this FobPointsResponse.  # noqa: E501
        :type: object
        """
        if error_message is None:
            raise ValueError("Invalid value for `error_message`, must not be `None`")  # noqa: E501

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
        if issubclass(FobPointsResponse, dict):
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
        if not isinstance(other, FobPointsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other