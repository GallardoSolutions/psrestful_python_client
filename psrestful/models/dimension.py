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

class Dimension(object):
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
        'dimension_uom': 'object',
        'depth': 'object',
        'height': 'object',
        'width': 'object',
        'weight_uom': 'object',
        'weight': 'object'
    }

    attribute_map = {
        'dimension_uom': 'dimensionUom',
        'depth': 'depth',
        'height': 'height',
        'width': 'width',
        'weight_uom': 'weightUom',
        'weight': 'weight'
    }

    def __init__(self, dimension_uom=None, depth=None, height=None, width=None, weight_uom=None, weight=None):  # noqa: E501
        """Dimension - a model defined in Swagger"""  # noqa: E501
        self._dimension_uom = None
        self._depth = None
        self._height = None
        self._width = None
        self._weight_uom = None
        self._weight = None
        self.discriminator = None
        self.dimension_uom = dimension_uom
        self.depth = depth
        self.height = height
        self.width = width
        self.weight_uom = weight_uom
        self.weight = weight

    @property
    def dimension_uom(self):
        """Gets the dimension_uom of this Dimension.  # noqa: E501


        :return: The dimension_uom of this Dimension.  # noqa: E501
        :rtype: object
        """
        return self._dimension_uom

    @dimension_uom.setter
    def dimension_uom(self, dimension_uom):
        """Sets the dimension_uom of this Dimension.


        :param dimension_uom: The dimension_uom of this Dimension.  # noqa: E501
        :type: object
        """
        if dimension_uom is None:
            raise ValueError("Invalid value for `dimension_uom`, must not be `None`")  # noqa: E501

        self._dimension_uom = dimension_uom

    @property
    def depth(self):
        """Gets the depth of this Dimension.  # noqa: E501


        :return: The depth of this Dimension.  # noqa: E501
        :rtype: object
        """
        return self._depth

    @depth.setter
    def depth(self, depth):
        """Sets the depth of this Dimension.


        :param depth: The depth of this Dimension.  # noqa: E501
        :type: object
        """
        if depth is None:
            raise ValueError("Invalid value for `depth`, must not be `None`")  # noqa: E501

        self._depth = depth

    @property
    def height(self):
        """Gets the height of this Dimension.  # noqa: E501


        :return: The height of this Dimension.  # noqa: E501
        :rtype: object
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this Dimension.


        :param height: The height of this Dimension.  # noqa: E501
        :type: object
        """
        if height is None:
            raise ValueError("Invalid value for `height`, must not be `None`")  # noqa: E501

        self._height = height

    @property
    def width(self):
        """Gets the width of this Dimension.  # noqa: E501


        :return: The width of this Dimension.  # noqa: E501
        :rtype: object
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this Dimension.


        :param width: The width of this Dimension.  # noqa: E501
        :type: object
        """
        if width is None:
            raise ValueError("Invalid value for `width`, must not be `None`")  # noqa: E501

        self._width = width

    @property
    def weight_uom(self):
        """Gets the weight_uom of this Dimension.  # noqa: E501


        :return: The weight_uom of this Dimension.  # noqa: E501
        :rtype: object
        """
        return self._weight_uom

    @weight_uom.setter
    def weight_uom(self, weight_uom):
        """Sets the weight_uom of this Dimension.


        :param weight_uom: The weight_uom of this Dimension.  # noqa: E501
        :type: object
        """
        if weight_uom is None:
            raise ValueError("Invalid value for `weight_uom`, must not be `None`")  # noqa: E501

        self._weight_uom = weight_uom

    @property
    def weight(self):
        """Gets the weight of this Dimension.  # noqa: E501


        :return: The weight of this Dimension.  # noqa: E501
        :rtype: object
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this Dimension.


        :param weight: The weight of this Dimension.  # noqa: E501
        :type: object
        """
        if weight is None:
            raise ValueError("Invalid value for `weight`, must not be `None`")  # noqa: E501

        self._weight = weight

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
        if issubclass(Dimension, dict):
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
        if not isinstance(other, Dimension):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
