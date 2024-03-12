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

class ContactInput(object):
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
        'contact_type': 'ContactTypeInput',
        'contact_details': 'ContactDetailsInput',
        'account_name': 'object',
        'account_number': 'object'
    }

    attribute_map = {
        'contact_type': 'contactType',
        'contact_details': 'ContactDetails',
        'account_name': 'accountName',
        'account_number': 'accountNumber'
    }

    def __init__(self, contact_type=None, contact_details=None, account_name=None, account_number=None):  # noqa: E501
        """ContactInput - a model defined in Swagger"""  # noqa: E501
        self._contact_type = None
        self._contact_details = None
        self._account_name = None
        self._account_number = None
        self.discriminator = None
        self.contact_type = contact_type
        self.contact_details = contact_details
        self.account_name = account_name
        self.account_number = account_number

    @property
    def contact_type(self):
        """Gets the contact_type of this ContactInput.  # noqa: E501


        :return: The contact_type of this ContactInput.  # noqa: E501
        :rtype: ContactTypeInput
        """
        return self._contact_type

    @contact_type.setter
    def contact_type(self, contact_type):
        """Sets the contact_type of this ContactInput.


        :param contact_type: The contact_type of this ContactInput.  # noqa: E501
        :type: ContactTypeInput
        """
        if contact_type is None:
            raise ValueError("Invalid value for `contact_type`, must not be `None`")  # noqa: E501

        self._contact_type = contact_type

    @property
    def contact_details(self):
        """Gets the contact_details of this ContactInput.  # noqa: E501


        :return: The contact_details of this ContactInput.  # noqa: E501
        :rtype: ContactDetailsInput
        """
        return self._contact_details

    @contact_details.setter
    def contact_details(self, contact_details):
        """Sets the contact_details of this ContactInput.


        :param contact_details: The contact_details of this ContactInput.  # noqa: E501
        :type: ContactDetailsInput
        """
        if contact_details is None:
            raise ValueError("Invalid value for `contact_details`, must not be `None`")  # noqa: E501

        self._contact_details = contact_details

    @property
    def account_name(self):
        """Gets the account_name of this ContactInput.  # noqa: E501


        :return: The account_name of this ContactInput.  # noqa: E501
        :rtype: object
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this ContactInput.


        :param account_name: The account_name of this ContactInput.  # noqa: E501
        :type: object
        """
        if account_name is None:
            raise ValueError("Invalid value for `account_name`, must not be `None`")  # noqa: E501

        self._account_name = account_name

    @property
    def account_number(self):
        """Gets the account_number of this ContactInput.  # noqa: E501


        :return: The account_number of this ContactInput.  # noqa: E501
        :rtype: object
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this ContactInput.


        :param account_number: The account_number of this ContactInput.  # noqa: E501
        :type: object
        """
        if account_number is None:
            raise ValueError("Invalid value for `account_number`, must not be `None`")  # noqa: E501

        self._account_number = account_number

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
        if issubclass(ContactInput, dict):
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
        if not isinstance(other, ContactInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
