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

class ShipmentLocation(object):
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
        'id': 'object',
        'complete': 'object',
        'ship_from_address': 'Address',
        'ship_to_address': 'Address',
        'shipment_destination_type': 'object',
        'package_array': 'object'
    }

    attribute_map = {
        'id': 'id',
        'complete': 'complete',
        'ship_from_address': 'ShipFromAddress',
        'ship_to_address': 'ShipToAddress',
        'shipment_destination_type': 'shipmentDestinationType',
        'package_array': 'PackageArray'
    }

    def __init__(self, id=None, complete=None, ship_from_address=None, ship_to_address=None, shipment_destination_type=None, package_array=None):  # noqa: E501
        """ShipmentLocation - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._complete = None
        self._ship_from_address = None
        self._ship_to_address = None
        self._shipment_destination_type = None
        self._package_array = None
        self.discriminator = None
        self.id = id
        self.complete = complete
        self.ship_from_address = ship_from_address
        self.ship_to_address = ship_to_address
        self.shipment_destination_type = shipment_destination_type
        self.package_array = package_array

    @property
    def id(self):
        """Gets the id of this ShipmentLocation.  # noqa: E501


        :return: The id of this ShipmentLocation.  # noqa: E501
        :rtype: object
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShipmentLocation.


        :param id: The id of this ShipmentLocation.  # noqa: E501
        :type: object
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def complete(self):
        """Gets the complete of this ShipmentLocation.  # noqa: E501


        :return: The complete of this ShipmentLocation.  # noqa: E501
        :rtype: object
        """
        return self._complete

    @complete.setter
    def complete(self, complete):
        """Sets the complete of this ShipmentLocation.


        :param complete: The complete of this ShipmentLocation.  # noqa: E501
        :type: object
        """
        if complete is None:
            raise ValueError("Invalid value for `complete`, must not be `None`")  # noqa: E501

        self._complete = complete

    @property
    def ship_from_address(self):
        """Gets the ship_from_address of this ShipmentLocation.  # noqa: E501


        :return: The ship_from_address of this ShipmentLocation.  # noqa: E501
        :rtype: Address
        """
        return self._ship_from_address

    @ship_from_address.setter
    def ship_from_address(self, ship_from_address):
        """Sets the ship_from_address of this ShipmentLocation.


        :param ship_from_address: The ship_from_address of this ShipmentLocation.  # noqa: E501
        :type: Address
        """
        if ship_from_address is None:
            raise ValueError("Invalid value for `ship_from_address`, must not be `None`")  # noqa: E501

        self._ship_from_address = ship_from_address

    @property
    def ship_to_address(self):
        """Gets the ship_to_address of this ShipmentLocation.  # noqa: E501


        :return: The ship_to_address of this ShipmentLocation.  # noqa: E501
        :rtype: Address
        """
        return self._ship_to_address

    @ship_to_address.setter
    def ship_to_address(self, ship_to_address):
        """Sets the ship_to_address of this ShipmentLocation.


        :param ship_to_address: The ship_to_address of this ShipmentLocation.  # noqa: E501
        :type: Address
        """
        if ship_to_address is None:
            raise ValueError("Invalid value for `ship_to_address`, must not be `None`")  # noqa: E501

        self._ship_to_address = ship_to_address

    @property
    def shipment_destination_type(self):
        """Gets the shipment_destination_type of this ShipmentLocation.  # noqa: E501


        :return: The shipment_destination_type of this ShipmentLocation.  # noqa: E501
        :rtype: object
        """
        return self._shipment_destination_type

    @shipment_destination_type.setter
    def shipment_destination_type(self, shipment_destination_type):
        """Sets the shipment_destination_type of this ShipmentLocation.


        :param shipment_destination_type: The shipment_destination_type of this ShipmentLocation.  # noqa: E501
        :type: object
        """
        if shipment_destination_type is None:
            raise ValueError("Invalid value for `shipment_destination_type`, must not be `None`")  # noqa: E501

        self._shipment_destination_type = shipment_destination_type

    @property
    def package_array(self):
        """Gets the package_array of this ShipmentLocation.  # noqa: E501


        :return: The package_array of this ShipmentLocation.  # noqa: E501
        :rtype: object
        """
        return self._package_array

    @package_array.setter
    def package_array(self, package_array):
        """Sets the package_array of this ShipmentLocation.


        :param package_array: The package_array of this ShipmentLocation.  # noqa: E501
        :type: object
        """
        if package_array is None:
            raise ValueError("Invalid value for `package_array`, must not be `None`")  # noqa: E501

        self._package_array = package_array

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
        if issubclass(ShipmentLocation, dict):
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
        if not isinstance(other, ShipmentLocation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
