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

class ChargeInput(object):
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
        'charge_id': 'object',
        'charge_name': 'object',
        'description': 'object',
        'charge_type': 'ChargeTypeInput',
        'quantity': 'QuantityInput',
        'unit_price': 'object',
        'extended_price': 'object'
    }

    attribute_map = {
        'charge_id': 'chargeId',
        'charge_name': 'chargeName',
        'description': 'description',
        'charge_type': 'chargeType',
        'quantity': 'Quantity',
        'unit_price': 'unitPrice',
        'extended_price': 'extendedPrice'
    }

    def __init__(self, charge_id=None, charge_name=None, description=None, charge_type=None, quantity=None, unit_price=None, extended_price=None):  # noqa: E501
        """ChargeInput - a model defined in Swagger"""  # noqa: E501
        self._charge_id = None
        self._charge_name = None
        self._description = None
        self._charge_type = None
        self._quantity = None
        self._unit_price = None
        self._extended_price = None
        self.discriminator = None
        self.charge_id = charge_id
        self.charge_name = charge_name
        self.description = description
        self.charge_type = charge_type
        self.quantity = quantity
        self.unit_price = unit_price
        self.extended_price = extended_price

    @property
    def charge_id(self):
        """Gets the charge_id of this ChargeInput.  # noqa: E501

        The chargeId from the supplier’s PromoStandards Product Pricing and Configuration service  # noqa: E501

        :return: The charge_id of this ChargeInput.  # noqa: E501
        :rtype: object
        """
        return self._charge_id

    @charge_id.setter
    def charge_id(self, charge_id):
        """Sets the charge_id of this ChargeInput.

        The chargeId from the supplier’s PromoStandards Product Pricing and Configuration service  # noqa: E501

        :param charge_id: The charge_id of this ChargeInput.  # noqa: E501
        :type: object
        """
        if charge_id is None:
            raise ValueError("Invalid value for `charge_id`, must not be `None`")  # noqa: E501

        self._charge_id = charge_id

    @property
    def charge_name(self):
        """Gets the charge_name of this ChargeInput.  # noqa: E501


        :return: The charge_name of this ChargeInput.  # noqa: E501
        :rtype: object
        """
        return self._charge_name

    @charge_name.setter
    def charge_name(self, charge_name):
        """Sets the charge_name of this ChargeInput.


        :param charge_name: The charge_name of this ChargeInput.  # noqa: E501
        :type: object
        """
        if charge_name is None:
            raise ValueError("Invalid value for `charge_name`, must not be `None`")  # noqa: E501

        self._charge_name = charge_name

    @property
    def description(self):
        """Gets the description of this ChargeInput.  # noqa: E501


        :return: The description of this ChargeInput.  # noqa: E501
        :rtype: object
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ChargeInput.


        :param description: The description of this ChargeInput.  # noqa: E501
        :type: object
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def charge_type(self):
        """Gets the charge_type of this ChargeInput.  # noqa: E501


        :return: The charge_type of this ChargeInput.  # noqa: E501
        :rtype: ChargeTypeInput
        """
        return self._charge_type

    @charge_type.setter
    def charge_type(self, charge_type):
        """Sets the charge_type of this ChargeInput.


        :param charge_type: The charge_type of this ChargeInput.  # noqa: E501
        :type: ChargeTypeInput
        """
        if charge_type is None:
            raise ValueError("Invalid value for `charge_type`, must not be `None`")  # noqa: E501

        self._charge_type = charge_type

    @property
    def quantity(self):
        """Gets the quantity of this ChargeInput.  # noqa: E501


        :return: The quantity of this ChargeInput.  # noqa: E501
        :rtype: QuantityInput
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this ChargeInput.


        :param quantity: The quantity of this ChargeInput.  # noqa: E501
        :type: QuantityInput
        """
        if quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")  # noqa: E501

        self._quantity = quantity

    @property
    def unit_price(self):
        """Gets the unit_price of this ChargeInput.  # noqa: E501


        :return: The unit_price of this ChargeInput.  # noqa: E501
        :rtype: object
        """
        return self._unit_price

    @unit_price.setter
    def unit_price(self, unit_price):
        """Sets the unit_price of this ChargeInput.


        :param unit_price: The unit_price of this ChargeInput.  # noqa: E501
        :type: object
        """
        if unit_price is None:
            raise ValueError("Invalid value for `unit_price`, must not be `None`")  # noqa: E501

        self._unit_price = unit_price

    @property
    def extended_price(self):
        """Gets the extended_price of this ChargeInput.  # noqa: E501


        :return: The extended_price of this ChargeInput.  # noqa: E501
        :rtype: object
        """
        return self._extended_price

    @extended_price.setter
    def extended_price(self, extended_price):
        """Sets the extended_price of this ChargeInput.


        :param extended_price: The extended_price of this ChargeInput.  # noqa: E501
        :type: object
        """
        if extended_price is None:
            raise ValueError("Invalid value for `extended_price`, must not be `None`")  # noqa: E501

        self._extended_price = extended_price

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
        if issubclass(ChargeInput, dict):
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
        if not isinstance(other, ChargeInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
