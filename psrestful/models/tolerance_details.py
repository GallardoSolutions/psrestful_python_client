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

class ToleranceDetails(object):
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
        'tolerance': 'ToleranceType',
        'value': 'object',
        'uom': 'ToleranceUoM'
    }

    attribute_map = {
        'tolerance': 'tolerance',
        'value': 'value',
        'uom': 'uom'
    }

    def __init__(self, tolerance=None, value=None, uom=None):  # noqa: E501
        """ToleranceDetails - a model defined in Swagger"""  # noqa: E501
        self._tolerance = None
        self._value = None
        self._uom = None
        self.discriminator = None
        self.tolerance = tolerance
        self.value = value
        self.uom = uom

    @property
    def tolerance(self):
        """Gets the tolerance of this ToleranceDetails.  # noqa: E501


        :return: The tolerance of this ToleranceDetails.  # noqa: E501
        :rtype: ToleranceType
        """
        return self._tolerance

    @tolerance.setter
    def tolerance(self, tolerance):
        """Sets the tolerance of this ToleranceDetails.


        :param tolerance: The tolerance of this ToleranceDetails.  # noqa: E501
        :type: ToleranceType
        """
        if tolerance is None:
            raise ValueError("Invalid value for `tolerance`, must not be `None`")  # noqa: E501

        self._tolerance = tolerance

    @property
    def value(self):
        """Gets the value of this ToleranceDetails.  # noqa: E501


        :return: The value of this ToleranceDetails.  # noqa: E501
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ToleranceDetails.


        :param value: The value of this ToleranceDetails.  # noqa: E501
        :type: object
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def uom(self):
        """Gets the uom of this ToleranceDetails.  # noqa: E501


        :return: The uom of this ToleranceDetails.  # noqa: E501
        :rtype: ToleranceUoM
        """
        return self._uom

    @uom.setter
    def uom(self, uom):
        """Sets the uom of this ToleranceDetails.


        :param uom: The uom of this ToleranceDetails.  # noqa: E501
        :type: ToleranceUoM
        """
        if uom is None:
            raise ValueError("Invalid value for `uom`, must not be `None`")  # noqa: E501

        self._uom = uom

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
        if issubclass(ToleranceDetails, dict):
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
        if not isinstance(other, ToleranceDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other