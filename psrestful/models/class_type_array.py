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

class ClassTypeArray(object):
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
        'class_type': 'object'
    }

    attribute_map = {
        'class_type': 'ClassType'
    }

    def __init__(self, class_type=None):  # noqa: E501
        """ClassTypeArray - a model defined in Swagger"""  # noqa: E501
        self._class_type = None
        self.discriminator = None
        self.class_type = class_type

    @property
    def class_type(self):
        """Gets the class_type of this ClassTypeArray.  # noqa: E501


        :return: The class_type of this ClassTypeArray.  # noqa: E501
        :rtype: object
        """
        return self._class_type

    @class_type.setter
    def class_type(self, class_type):
        """Sets the class_type of this ClassTypeArray.


        :param class_type: The class_type of this ClassTypeArray.  # noqa: E501
        :type: object
        """
        if class_type is None:
            raise ValueError("Invalid value for `class_type`, must not be `None`")  # noqa: E501

        self._class_type = class_type

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
        if issubclass(ClassTypeArray, dict):
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
        if not isinstance(other, ClassTypeArray):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other