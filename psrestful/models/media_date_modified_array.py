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

class MediaDateModifiedArray(object):
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
        'media_date_modified': 'object'
    }

    attribute_map = {
        'media_date_modified': 'MediaDateModified'
    }

    def __init__(self, media_date_modified=None):  # noqa: E501
        """MediaDateModifiedArray - a model defined in Swagger"""  # noqa: E501
        self._media_date_modified = None
        self.discriminator = None
        self.media_date_modified = media_date_modified

    @property
    def media_date_modified(self):
        """Gets the media_date_modified of this MediaDateModifiedArray.  # noqa: E501


        :return: The media_date_modified of this MediaDateModifiedArray.  # noqa: E501
        :rtype: object
        """
        return self._media_date_modified

    @media_date_modified.setter
    def media_date_modified(self, media_date_modified):
        """Sets the media_date_modified of this MediaDateModifiedArray.


        :param media_date_modified: The media_date_modified of this MediaDateModifiedArray.  # noqa: E501
        :type: object
        """
        if media_date_modified is None:
            raise ValueError("Invalid value for `media_date_modified`, must not be `None`")  # noqa: E501

        self._media_date_modified = media_date_modified

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
        if issubclass(MediaDateModifiedArray, dict):
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
        if not isinstance(other, MediaDateModifiedArray):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
