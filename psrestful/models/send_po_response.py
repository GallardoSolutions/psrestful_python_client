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

class SendPOResponse(object):
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
        'transaction_id': 'object',
        'service_message_array': 'object'
    }

    attribute_map = {
        'transaction_id': 'transactionId',
        'service_message_array': 'ServiceMessageArray'
    }

    def __init__(self, transaction_id=None, service_message_array=None):  # noqa: E501
        """SendPOResponse - a model defined in Swagger"""  # noqa: E501
        self._transaction_id = None
        self._service_message_array = None
        self.discriminator = None
        self.transaction_id = transaction_id
        self.service_message_array = service_message_array

    @property
    def transaction_id(self):
        """Gets the transaction_id of this SendPOResponse.  # noqa: E501


        :return: The transaction_id of this SendPOResponse.  # noqa: E501
        :rtype: object
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """Sets the transaction_id of this SendPOResponse.


        :param transaction_id: The transaction_id of this SendPOResponse.  # noqa: E501
        :type: object
        """
        if transaction_id is None:
            raise ValueError("Invalid value for `transaction_id`, must not be `None`")  # noqa: E501

        self._transaction_id = transaction_id

    @property
    def service_message_array(self):
        """Gets the service_message_array of this SendPOResponse.  # noqa: E501


        :return: The service_message_array of this SendPOResponse.  # noqa: E501
        :rtype: object
        """
        return self._service_message_array

    @service_message_array.setter
    def service_message_array(self, service_message_array):
        """Sets the service_message_array of this SendPOResponse.


        :param service_message_array: The service_message_array of this SendPOResponse.  # noqa: E501
        :type: object
        """
        if service_message_array is None:
            raise ValueError("Invalid value for `service_message_array`, must not be `None`")  # noqa: E501

        self._service_message_array = service_message_array

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
        if issubclass(SendPOResponse, dict):
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
        if not isinstance(other, SendPOResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
