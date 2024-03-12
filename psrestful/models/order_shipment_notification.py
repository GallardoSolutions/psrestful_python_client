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

class OrderShipmentNotification(object):
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
        'purchase_order_number': 'object',
        'complete': 'object',
        'sales_order_array': 'object'
    }

    attribute_map = {
        'purchase_order_number': 'purchaseOrderNumber',
        'complete': 'complete',
        'sales_order_array': 'SalesOrderArray'
    }

    def __init__(self, purchase_order_number=None, complete=None, sales_order_array=None):  # noqa: E501
        """OrderShipmentNotification - a model defined in Swagger"""  # noqa: E501
        self._purchase_order_number = None
        self._complete = None
        self._sales_order_array = None
        self.discriminator = None
        self.purchase_order_number = purchase_order_number
        self.complete = complete
        self.sales_order_array = sales_order_array

    @property
    def purchase_order_number(self):
        """Gets the purchase_order_number of this OrderShipmentNotification.  # noqa: E501


        :return: The purchase_order_number of this OrderShipmentNotification.  # noqa: E501
        :rtype: object
        """
        return self._purchase_order_number

    @purchase_order_number.setter
    def purchase_order_number(self, purchase_order_number):
        """Sets the purchase_order_number of this OrderShipmentNotification.


        :param purchase_order_number: The purchase_order_number of this OrderShipmentNotification.  # noqa: E501
        :type: object
        """
        if purchase_order_number is None:
            raise ValueError("Invalid value for `purchase_order_number`, must not be `None`")  # noqa: E501

        self._purchase_order_number = purchase_order_number

    @property
    def complete(self):
        """Gets the complete of this OrderShipmentNotification.  # noqa: E501


        :return: The complete of this OrderShipmentNotification.  # noqa: E501
        :rtype: object
        """
        return self._complete

    @complete.setter
    def complete(self, complete):
        """Sets the complete of this OrderShipmentNotification.


        :param complete: The complete of this OrderShipmentNotification.  # noqa: E501
        :type: object
        """
        if complete is None:
            raise ValueError("Invalid value for `complete`, must not be `None`")  # noqa: E501

        self._complete = complete

    @property
    def sales_order_array(self):
        """Gets the sales_order_array of this OrderShipmentNotification.  # noqa: E501


        :return: The sales_order_array of this OrderShipmentNotification.  # noqa: E501
        :rtype: object
        """
        return self._sales_order_array

    @sales_order_array.setter
    def sales_order_array(self, sales_order_array):
        """Sets the sales_order_array of this OrderShipmentNotification.


        :param sales_order_array: The sales_order_array of this OrderShipmentNotification.  # noqa: E501
        :type: object
        """
        if sales_order_array is None:
            raise ValueError("Invalid value for `sales_order_array`, must not be `None`")  # noqa: E501

        self._sales_order_array = sales_order_array

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
        if issubclass(OrderShipmentNotification, dict):
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
        if not isinstance(other, OrderShipmentNotification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
