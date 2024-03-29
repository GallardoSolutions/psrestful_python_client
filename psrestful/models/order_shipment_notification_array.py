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

class OrderShipmentNotificationArray(object):
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
        'order_shipment_notification': 'object'
    }

    attribute_map = {
        'order_shipment_notification': 'OrderShipmentNotification'
    }

    def __init__(self, order_shipment_notification=None):  # noqa: E501
        """OrderShipmentNotificationArray - a model defined in Swagger"""  # noqa: E501
        self._order_shipment_notification = None
        self.discriminator = None
        self.order_shipment_notification = order_shipment_notification

    @property
    def order_shipment_notification(self):
        """Gets the order_shipment_notification of this OrderShipmentNotificationArray.  # noqa: E501


        :return: The order_shipment_notification of this OrderShipmentNotificationArray.  # noqa: E501
        :rtype: object
        """
        return self._order_shipment_notification

    @order_shipment_notification.setter
    def order_shipment_notification(self, order_shipment_notification):
        """Sets the order_shipment_notification of this OrderShipmentNotificationArray.


        :param order_shipment_notification: The order_shipment_notification of this OrderShipmentNotificationArray.  # noqa: E501
        :type: object
        """
        if order_shipment_notification is None:
            raise ValueError("Invalid value for `order_shipment_notification`, must not be `None`")  # noqa: E501

        self._order_shipment_notification = order_shipment_notification

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
        if issubclass(OrderShipmentNotificationArray, dict):
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
        if not isinstance(other, OrderShipmentNotificationArray):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
