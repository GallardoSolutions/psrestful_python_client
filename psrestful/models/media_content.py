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

class MediaContent(object):
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
        'product_id': 'object',
        'part_id': 'object',
        'url': 'object',
        'media_type': 'object',
        'file_size': 'object',
        'width': 'object',
        'height': 'object',
        'dpi': 'object',
        'color': 'object',
        'description': 'object',
        'single_part': 'object',
        'change_time_stamp': 'object',
        'class_type_array': 'ClassTypeArray',
        'decoration_array': 'object',
        'location_array': 'object'
    }

    attribute_map = {
        'product_id': 'productId',
        'part_id': 'partId',
        'url': 'url',
        'media_type': 'mediaType',
        'file_size': 'fileSize',
        'width': 'width',
        'height': 'height',
        'dpi': 'dpi',
        'color': 'color',
        'description': 'description',
        'single_part': 'singlePart',
        'change_time_stamp': 'changeTimeStamp',
        'class_type_array': 'ClassTypeArray',
        'decoration_array': 'DecorationArray',
        'location_array': 'LocationArray'
    }

    def __init__(self, product_id=None, part_id=None, url=None, media_type=None, file_size=None, width=None, height=None, dpi=None, color=None, description=None, single_part=None, change_time_stamp=None, class_type_array=None, decoration_array=None, location_array=None):  # noqa: E501
        """MediaContent - a model defined in Swagger"""  # noqa: E501
        self._product_id = None
        self._part_id = None
        self._url = None
        self._media_type = None
        self._file_size = None
        self._width = None
        self._height = None
        self._dpi = None
        self._color = None
        self._description = None
        self._single_part = None
        self._change_time_stamp = None
        self._class_type_array = None
        self._decoration_array = None
        self._location_array = None
        self.discriminator = None
        self.product_id = product_id
        self.part_id = part_id
        self.url = url
        self.media_type = media_type
        self.file_size = file_size
        self.width = width
        self.height = height
        self.dpi = dpi
        self.color = color
        self.description = description
        self.single_part = single_part
        self.change_time_stamp = change_time_stamp
        self.class_type_array = class_type_array
        self.decoration_array = decoration_array
        self.location_array = location_array

    @property
    def product_id(self):
        """Gets the product_id of this MediaContent.  # noqa: E501


        :return: The product_id of this MediaContent.  # noqa: E501
        :rtype: object
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this MediaContent.


        :param product_id: The product_id of this MediaContent.  # noqa: E501
        :type: object
        """
        if product_id is None:
            raise ValueError("Invalid value for `product_id`, must not be `None`")  # noqa: E501

        self._product_id = product_id

    @property
    def part_id(self):
        """Gets the part_id of this MediaContent.  # noqa: E501


        :return: The part_id of this MediaContent.  # noqa: E501
        :rtype: object
        """
        return self._part_id

    @part_id.setter
    def part_id(self, part_id):
        """Sets the part_id of this MediaContent.


        :param part_id: The part_id of this MediaContent.  # noqa: E501
        :type: object
        """
        if part_id is None:
            raise ValueError("Invalid value for `part_id`, must not be `None`")  # noqa: E501

        self._part_id = part_id

    @property
    def url(self):
        """Gets the url of this MediaContent.  # noqa: E501


        :return: The url of this MediaContent.  # noqa: E501
        :rtype: object
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this MediaContent.


        :param url: The url of this MediaContent.  # noqa: E501
        :type: object
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def media_type(self):
        """Gets the media_type of this MediaContent.  # noqa: E501


        :return: The media_type of this MediaContent.  # noqa: E501
        :rtype: object
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        """Sets the media_type of this MediaContent.


        :param media_type: The media_type of this MediaContent.  # noqa: E501
        :type: object
        """
        if media_type is None:
            raise ValueError("Invalid value for `media_type`, must not be `None`")  # noqa: E501

        self._media_type = media_type

    @property
    def file_size(self):
        """Gets the file_size of this MediaContent.  # noqa: E501


        :return: The file_size of this MediaContent.  # noqa: E501
        :rtype: object
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        """Sets the file_size of this MediaContent.


        :param file_size: The file_size of this MediaContent.  # noqa: E501
        :type: object
        """
        if file_size is None:
            raise ValueError("Invalid value for `file_size`, must not be `None`")  # noqa: E501

        self._file_size = file_size

    @property
    def width(self):
        """Gets the width of this MediaContent.  # noqa: E501


        :return: The width of this MediaContent.  # noqa: E501
        :rtype: object
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this MediaContent.


        :param width: The width of this MediaContent.  # noqa: E501
        :type: object
        """
        if width is None:
            raise ValueError("Invalid value for `width`, must not be `None`")  # noqa: E501

        self._width = width

    @property
    def height(self):
        """Gets the height of this MediaContent.  # noqa: E501


        :return: The height of this MediaContent.  # noqa: E501
        :rtype: object
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this MediaContent.


        :param height: The height of this MediaContent.  # noqa: E501
        :type: object
        """
        if height is None:
            raise ValueError("Invalid value for `height`, must not be `None`")  # noqa: E501

        self._height = height

    @property
    def dpi(self):
        """Gets the dpi of this MediaContent.  # noqa: E501


        :return: The dpi of this MediaContent.  # noqa: E501
        :rtype: object
        """
        return self._dpi

    @dpi.setter
    def dpi(self, dpi):
        """Sets the dpi of this MediaContent.


        :param dpi: The dpi of this MediaContent.  # noqa: E501
        :type: object
        """
        if dpi is None:
            raise ValueError("Invalid value for `dpi`, must not be `None`")  # noqa: E501

        self._dpi = dpi

    @property
    def color(self):
        """Gets the color of this MediaContent.  # noqa: E501


        :return: The color of this MediaContent.  # noqa: E501
        :rtype: object
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this MediaContent.


        :param color: The color of this MediaContent.  # noqa: E501
        :type: object
        """
        if color is None:
            raise ValueError("Invalid value for `color`, must not be `None`")  # noqa: E501

        self._color = color

    @property
    def description(self):
        """Gets the description of this MediaContent.  # noqa: E501


        :return: The description of this MediaContent.  # noqa: E501
        :rtype: object
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this MediaContent.


        :param description: The description of this MediaContent.  # noqa: E501
        :type: object
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def single_part(self):
        """Gets the single_part of this MediaContent.  # noqa: E501


        :return: The single_part of this MediaContent.  # noqa: E501
        :rtype: object
        """
        return self._single_part

    @single_part.setter
    def single_part(self, single_part):
        """Sets the single_part of this MediaContent.


        :param single_part: The single_part of this MediaContent.  # noqa: E501
        :type: object
        """
        if single_part is None:
            raise ValueError("Invalid value for `single_part`, must not be `None`")  # noqa: E501

        self._single_part = single_part

    @property
    def change_time_stamp(self):
        """Gets the change_time_stamp of this MediaContent.  # noqa: E501


        :return: The change_time_stamp of this MediaContent.  # noqa: E501
        :rtype: object
        """
        return self._change_time_stamp

    @change_time_stamp.setter
    def change_time_stamp(self, change_time_stamp):
        """Sets the change_time_stamp of this MediaContent.


        :param change_time_stamp: The change_time_stamp of this MediaContent.  # noqa: E501
        :type: object
        """
        if change_time_stamp is None:
            raise ValueError("Invalid value for `change_time_stamp`, must not be `None`")  # noqa: E501

        self._change_time_stamp = change_time_stamp

    @property
    def class_type_array(self):
        """Gets the class_type_array of this MediaContent.  # noqa: E501


        :return: The class_type_array of this MediaContent.  # noqa: E501
        :rtype: ClassTypeArray
        """
        return self._class_type_array

    @class_type_array.setter
    def class_type_array(self, class_type_array):
        """Sets the class_type_array of this MediaContent.


        :param class_type_array: The class_type_array of this MediaContent.  # noqa: E501
        :type: ClassTypeArray
        """
        if class_type_array is None:
            raise ValueError("Invalid value for `class_type_array`, must not be `None`")  # noqa: E501

        self._class_type_array = class_type_array

    @property
    def decoration_array(self):
        """Gets the decoration_array of this MediaContent.  # noqa: E501


        :return: The decoration_array of this MediaContent.  # noqa: E501
        :rtype: object
        """
        return self._decoration_array

    @decoration_array.setter
    def decoration_array(self, decoration_array):
        """Sets the decoration_array of this MediaContent.


        :param decoration_array: The decoration_array of this MediaContent.  # noqa: E501
        :type: object
        """
        if decoration_array is None:
            raise ValueError("Invalid value for `decoration_array`, must not be `None`")  # noqa: E501

        self._decoration_array = decoration_array

    @property
    def location_array(self):
        """Gets the location_array of this MediaContent.  # noqa: E501


        :return: The location_array of this MediaContent.  # noqa: E501
        :rtype: object
        """
        return self._location_array

    @location_array.setter
    def location_array(self, location_array):
        """Sets the location_array of this MediaContent.


        :param location_array: The location_array of this MediaContent.  # noqa: E501
        :type: object
        """
        if location_array is None:
            raise ValueError("Invalid value for `location_array`, must not be `None`")  # noqa: E501

        self._location_array = location_array

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
        if issubclass(MediaContent, dict):
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
        if not isinstance(other, MediaContent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
