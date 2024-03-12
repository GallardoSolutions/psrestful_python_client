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

class AvailableCharge(object):
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
        'charge_type': 'ChargeTypeOutput',
        'charge_description': 'object'
    }

    attribute_map = {
        'charge_id': 'chargeId',
        'charge_name': 'chargeName',
        'charge_type': 'chargeType',
        'charge_description': 'chargeDescription'
    }

    def __init__(self, charge_id=None, charge_name=None, charge_type=None, charge_description=None):  # noqa: E501
        """AvailableCharge - a model defined in Swagger"""  # noqa: E501
        self._charge_id = None
        self._charge_name = None
        self._charge_type = None
        self._charge_description = None
        self.discriminator = None
        self.charge_id = charge_id
        self.charge_name = charge_name
        self.charge_type = charge_type
        self.charge_description = charge_description

    @property
    def charge_id(self):
        """Gets the charge_id of this AvailableCharge.  # noqa: E501


        :return: The charge_id of this AvailableCharge.  # noqa: E501
        :rtype: object
        """
        return self._charge_id

    @charge_id.setter
    def charge_id(self, charge_id):
        """Sets the charge_id of this AvailableCharge.


        :param charge_id: The charge_id of this AvailableCharge.  # noqa: E501
        :type: object
        """
        if charge_id is None:
            raise ValueError("Invalid value for `charge_id`, must not be `None`")  # noqa: E501

        self._charge_id = charge_id

    @property
    def charge_name(self):
        """Gets the charge_name of this AvailableCharge.  # noqa: E501


        :return: The charge_name of this AvailableCharge.  # noqa: E501
        :rtype: object
        """
        return self._charge_name

    @charge_name.setter
    def charge_name(self, charge_name):
        """Sets the charge_name of this AvailableCharge.


        :param charge_name: The charge_name of this AvailableCharge.  # noqa: E501
        :type: object
        """
        if charge_name is None:
            raise ValueError("Invalid value for `charge_name`, must not be `None`")  # noqa: E501

        self._charge_name = charge_name

    @property
    def charge_type(self):
        """Gets the charge_type of this AvailableCharge.  # noqa: E501


        :return: The charge_type of this AvailableCharge.  # noqa: E501
        :rtype: ChargeTypeOutput
        """
        return self._charge_type

    @charge_type.setter
    def charge_type(self, charge_type):
        """Sets the charge_type of this AvailableCharge.


        :param charge_type: The charge_type of this AvailableCharge.  # noqa: E501
        :type: ChargeTypeOutput
        """
        if charge_type is None:
            raise ValueError("Invalid value for `charge_type`, must not be `None`")  # noqa: E501

        self._charge_type = charge_type

    @property
    def charge_description(self):
        """Gets the charge_description of this AvailableCharge.  # noqa: E501


        :return: The charge_description of this AvailableCharge.  # noqa: E501
        :rtype: object
        """
        return self._charge_description

    @charge_description.setter
    def charge_description(self, charge_description):
        """Sets the charge_description of this AvailableCharge.


        :param charge_description: The charge_description of this AvailableCharge.  # noqa: E501
        :type: object
        """
        if charge_description is None:
            raise ValueError("Invalid value for `charge_description`, must not be `None`")  # noqa: E501

        self._charge_description = charge_description

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
        if issubclass(AvailableCharge, dict):
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
        if not isinstance(other, AvailableCharge):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
