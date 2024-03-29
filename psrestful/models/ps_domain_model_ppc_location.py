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

class PsDomainModelPpcLocation(object):
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
        'location_id': 'object',
        'location_name': 'object',
        'decoration_array': 'PsDomainModelPpcDecorationArray',
        'decorations_included': 'object',
        'default_location': 'object',
        'max_decoration': 'object',
        'min_decoration': 'object',
        'location_rank': 'object'
    }

    attribute_map = {
        'location_id': 'locationId',
        'location_name': 'locationName',
        'decoration_array': 'DecorationArray',
        'decorations_included': 'decorationsIncluded',
        'default_location': 'defaultLocation',
        'max_decoration': 'maxDecoration',
        'min_decoration': 'minDecoration',
        'location_rank': 'locationRank'
    }

    def __init__(self, location_id=None, location_name=None, decoration_array=None, decorations_included=None, default_location=None, max_decoration=None, min_decoration=None, location_rank=None):  # noqa: E501
        """PsDomainModelPpcLocation - a model defined in Swagger"""  # noqa: E501
        self._location_id = None
        self._location_name = None
        self._decoration_array = None
        self._decorations_included = None
        self._default_location = None
        self._max_decoration = None
        self._min_decoration = None
        self._location_rank = None
        self.discriminator = None
        self.location_id = location_id
        self.location_name = location_name
        self.decoration_array = decoration_array
        self.decorations_included = decorations_included
        self.default_location = default_location
        self.max_decoration = max_decoration
        self.min_decoration = min_decoration
        self.location_rank = location_rank

    @property
    def location_id(self):
        """Gets the location_id of this PsDomainModelPpcLocation.  # noqa: E501


        :return: The location_id of this PsDomainModelPpcLocation.  # noqa: E501
        :rtype: object
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        """Sets the location_id of this PsDomainModelPpcLocation.


        :param location_id: The location_id of this PsDomainModelPpcLocation.  # noqa: E501
        :type: object
        """
        if location_id is None:
            raise ValueError("Invalid value for `location_id`, must not be `None`")  # noqa: E501

        self._location_id = location_id

    @property
    def location_name(self):
        """Gets the location_name of this PsDomainModelPpcLocation.  # noqa: E501


        :return: The location_name of this PsDomainModelPpcLocation.  # noqa: E501
        :rtype: object
        """
        return self._location_name

    @location_name.setter
    def location_name(self, location_name):
        """Sets the location_name of this PsDomainModelPpcLocation.


        :param location_name: The location_name of this PsDomainModelPpcLocation.  # noqa: E501
        :type: object
        """
        if location_name is None:
            raise ValueError("Invalid value for `location_name`, must not be `None`")  # noqa: E501

        self._location_name = location_name

    @property
    def decoration_array(self):
        """Gets the decoration_array of this PsDomainModelPpcLocation.  # noqa: E501


        :return: The decoration_array of this PsDomainModelPpcLocation.  # noqa: E501
        :rtype: PsDomainModelPpcDecorationArray
        """
        return self._decoration_array

    @decoration_array.setter
    def decoration_array(self, decoration_array):
        """Sets the decoration_array of this PsDomainModelPpcLocation.


        :param decoration_array: The decoration_array of this PsDomainModelPpcLocation.  # noqa: E501
        :type: PsDomainModelPpcDecorationArray
        """
        if decoration_array is None:
            raise ValueError("Invalid value for `decoration_array`, must not be `None`")  # noqa: E501

        self._decoration_array = decoration_array

    @property
    def decorations_included(self):
        """Gets the decorations_included of this PsDomainModelPpcLocation.  # noqa: E501


        :return: The decorations_included of this PsDomainModelPpcLocation.  # noqa: E501
        :rtype: object
        """
        return self._decorations_included

    @decorations_included.setter
    def decorations_included(self, decorations_included):
        """Sets the decorations_included of this PsDomainModelPpcLocation.


        :param decorations_included: The decorations_included of this PsDomainModelPpcLocation.  # noqa: E501
        :type: object
        """
        if decorations_included is None:
            raise ValueError("Invalid value for `decorations_included`, must not be `None`")  # noqa: E501

        self._decorations_included = decorations_included

    @property
    def default_location(self):
        """Gets the default_location of this PsDomainModelPpcLocation.  # noqa: E501


        :return: The default_location of this PsDomainModelPpcLocation.  # noqa: E501
        :rtype: object
        """
        return self._default_location

    @default_location.setter
    def default_location(self, default_location):
        """Sets the default_location of this PsDomainModelPpcLocation.


        :param default_location: The default_location of this PsDomainModelPpcLocation.  # noqa: E501
        :type: object
        """
        if default_location is None:
            raise ValueError("Invalid value for `default_location`, must not be `None`")  # noqa: E501

        self._default_location = default_location

    @property
    def max_decoration(self):
        """Gets the max_decoration of this PsDomainModelPpcLocation.  # noqa: E501


        :return: The max_decoration of this PsDomainModelPpcLocation.  # noqa: E501
        :rtype: object
        """
        return self._max_decoration

    @max_decoration.setter
    def max_decoration(self, max_decoration):
        """Sets the max_decoration of this PsDomainModelPpcLocation.


        :param max_decoration: The max_decoration of this PsDomainModelPpcLocation.  # noqa: E501
        :type: object
        """
        if max_decoration is None:
            raise ValueError("Invalid value for `max_decoration`, must not be `None`")  # noqa: E501

        self._max_decoration = max_decoration

    @property
    def min_decoration(self):
        """Gets the min_decoration of this PsDomainModelPpcLocation.  # noqa: E501


        :return: The min_decoration of this PsDomainModelPpcLocation.  # noqa: E501
        :rtype: object
        """
        return self._min_decoration

    @min_decoration.setter
    def min_decoration(self, min_decoration):
        """Sets the min_decoration of this PsDomainModelPpcLocation.


        :param min_decoration: The min_decoration of this PsDomainModelPpcLocation.  # noqa: E501
        :type: object
        """
        if min_decoration is None:
            raise ValueError("Invalid value for `min_decoration`, must not be `None`")  # noqa: E501

        self._min_decoration = min_decoration

    @property
    def location_rank(self):
        """Gets the location_rank of this PsDomainModelPpcLocation.  # noqa: E501

        Popularity of location based on supplier experience  # noqa: E501

        :return: The location_rank of this PsDomainModelPpcLocation.  # noqa: E501
        :rtype: object
        """
        return self._location_rank

    @location_rank.setter
    def location_rank(self, location_rank):
        """Sets the location_rank of this PsDomainModelPpcLocation.

        Popularity of location based on supplier experience  # noqa: E501

        :param location_rank: The location_rank of this PsDomainModelPpcLocation.  # noqa: E501
        :type: object
        """
        if location_rank is None:
            raise ValueError("Invalid value for `location_rank`, must not be `None`")  # noqa: E501

        self._location_rank = location_rank

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
        if issubclass(PsDomainModelPpcLocation, dict):
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
        if not isinstance(other, PsDomainModelPpcLocation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
