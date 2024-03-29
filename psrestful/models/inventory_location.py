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

class InventoryLocation(object):
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
        'inventory_location_id': 'object',
        'inventory_location_name': 'object',
        'postal_code': 'object',
        'country': 'object',
        'inventory_location_quantity': 'object',
        'future_availability_array': 'object'
    }

    attribute_map = {
        'inventory_location_id': 'inventoryLocationId',
        'inventory_location_name': 'inventoryLocationName',
        'postal_code': 'postalCode',
        'country': 'country',
        'inventory_location_quantity': 'inventoryLocationQuantity',
        'future_availability_array': 'FutureAvailabilityArray'
    }

    def __init__(self, inventory_location_id=None, inventory_location_name=None, postal_code=None, country=None, inventory_location_quantity=None, future_availability_array=None):  # noqa: E501
        """InventoryLocation - a model defined in Swagger"""  # noqa: E501
        self._inventory_location_id = None
        self._inventory_location_name = None
        self._postal_code = None
        self._country = None
        self._inventory_location_quantity = None
        self._future_availability_array = None
        self.discriminator = None
        self.inventory_location_id = inventory_location_id
        self.inventory_location_name = inventory_location_name
        self.postal_code = postal_code
        self.country = country
        self.inventory_location_quantity = inventory_location_quantity
        self.future_availability_array = future_availability_array

    @property
    def inventory_location_id(self):
        """Gets the inventory_location_id of this InventoryLocation.  # noqa: E501


        :return: The inventory_location_id of this InventoryLocation.  # noqa: E501
        :rtype: object
        """
        return self._inventory_location_id

    @inventory_location_id.setter
    def inventory_location_id(self, inventory_location_id):
        """Sets the inventory_location_id of this InventoryLocation.


        :param inventory_location_id: The inventory_location_id of this InventoryLocation.  # noqa: E501
        :type: object
        """
        if inventory_location_id is None:
            raise ValueError("Invalid value for `inventory_location_id`, must not be `None`")  # noqa: E501

        self._inventory_location_id = inventory_location_id

    @property
    def inventory_location_name(self):
        """Gets the inventory_location_name of this InventoryLocation.  # noqa: E501


        :return: The inventory_location_name of this InventoryLocation.  # noqa: E501
        :rtype: object
        """
        return self._inventory_location_name

    @inventory_location_name.setter
    def inventory_location_name(self, inventory_location_name):
        """Sets the inventory_location_name of this InventoryLocation.


        :param inventory_location_name: The inventory_location_name of this InventoryLocation.  # noqa: E501
        :type: object
        """
        if inventory_location_name is None:
            raise ValueError("Invalid value for `inventory_location_name`, must not be `None`")  # noqa: E501

        self._inventory_location_name = inventory_location_name

    @property
    def postal_code(self):
        """Gets the postal_code of this InventoryLocation.  # noqa: E501


        :return: The postal_code of this InventoryLocation.  # noqa: E501
        :rtype: object
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this InventoryLocation.


        :param postal_code: The postal_code of this InventoryLocation.  # noqa: E501
        :type: object
        """
        if postal_code is None:
            raise ValueError("Invalid value for `postal_code`, must not be `None`")  # noqa: E501

        self._postal_code = postal_code

    @property
    def country(self):
        """Gets the country of this InventoryLocation.  # noqa: E501


        :return: The country of this InventoryLocation.  # noqa: E501
        :rtype: object
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this InventoryLocation.


        :param country: The country of this InventoryLocation.  # noqa: E501
        :type: object
        """
        if country is None:
            raise ValueError("Invalid value for `country`, must not be `None`")  # noqa: E501

        self._country = country

    @property
    def inventory_location_quantity(self):
        """Gets the inventory_location_quantity of this InventoryLocation.  # noqa: E501


        :return: The inventory_location_quantity of this InventoryLocation.  # noqa: E501
        :rtype: object
        """
        return self._inventory_location_quantity

    @inventory_location_quantity.setter
    def inventory_location_quantity(self, inventory_location_quantity):
        """Sets the inventory_location_quantity of this InventoryLocation.


        :param inventory_location_quantity: The inventory_location_quantity of this InventoryLocation.  # noqa: E501
        :type: object
        """
        if inventory_location_quantity is None:
            raise ValueError("Invalid value for `inventory_location_quantity`, must not be `None`")  # noqa: E501

        self._inventory_location_quantity = inventory_location_quantity

    @property
    def future_availability_array(self):
        """Gets the future_availability_array of this InventoryLocation.  # noqa: E501


        :return: The future_availability_array of this InventoryLocation.  # noqa: E501
        :rtype: object
        """
        return self._future_availability_array

    @future_availability_array.setter
    def future_availability_array(self, future_availability_array):
        """Sets the future_availability_array of this InventoryLocation.


        :param future_availability_array: The future_availability_array of this InventoryLocation.  # noqa: E501
        :type: object
        """
        if future_availability_array is None:
            raise ValueError("Invalid value for `future_availability_array`, must not be `None`")  # noqa: E501

        self._future_availability_array = future_availability_array

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
        if issubclass(InventoryLocation, dict):
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
        if not isinstance(other, InventoryLocation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
