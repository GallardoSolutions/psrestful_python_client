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

class ContactDetailsInput(object):
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
        'attention_to': 'object',
        'company_name': 'object',
        'address1': 'object',
        'address2': 'object',
        'address3': 'object',
        'city': 'object',
        'region': 'object',
        'postal_code': 'object',
        'country': 'object',
        'email': 'object',
        'phone': 'object',
        'comments': 'object'
    }

    attribute_map = {
        'attention_to': 'attentionTo',
        'company_name': 'companyName',
        'address1': 'address1',
        'address2': 'address2',
        'address3': 'address3',
        'city': 'city',
        'region': 'region',
        'postal_code': 'postalCode',
        'country': 'country',
        'email': 'email',
        'phone': 'phone',
        'comments': 'comments'
    }

    def __init__(self, attention_to=None, company_name=None, address1=None, address2=None, address3=None, city=None, region=None, postal_code=None, country=None, email=None, phone=None, comments=None):  # noqa: E501
        """ContactDetailsInput - a model defined in Swagger"""  # noqa: E501
        self._attention_to = None
        self._company_name = None
        self._address1 = None
        self._address2 = None
        self._address3 = None
        self._city = None
        self._region = None
        self._postal_code = None
        self._country = None
        self._email = None
        self._phone = None
        self._comments = None
        self.discriminator = None
        if attention_to is not None:
            self.attention_to = attention_to
        if company_name is not None:
            self.company_name = company_name
        if address1 is not None:
            self.address1 = address1
        if address2 is not None:
            self.address2 = address2
        if address3 is not None:
            self.address3 = address3
        if city is not None:
            self.city = city
        if region is not None:
            self.region = region
        if postal_code is not None:
            self.postal_code = postal_code
        if country is not None:
            self.country = country
        if email is not None:
            self.email = email
        if phone is not None:
            self.phone = phone
        if comments is not None:
            self.comments = comments

    @property
    def attention_to(self):
        """Gets the attention_to of this ContactDetailsInput.  # noqa: E501


        :return: The attention_to of this ContactDetailsInput.  # noqa: E501
        :rtype: object
        """
        return self._attention_to

    @attention_to.setter
    def attention_to(self, attention_to):
        """Sets the attention_to of this ContactDetailsInput.


        :param attention_to: The attention_to of this ContactDetailsInput.  # noqa: E501
        :type: object
        """

        self._attention_to = attention_to

    @property
    def company_name(self):
        """Gets the company_name of this ContactDetailsInput.  # noqa: E501


        :return: The company_name of this ContactDetailsInput.  # noqa: E501
        :rtype: object
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this ContactDetailsInput.


        :param company_name: The company_name of this ContactDetailsInput.  # noqa: E501
        :type: object
        """

        self._company_name = company_name

    @property
    def address1(self):
        """Gets the address1 of this ContactDetailsInput.  # noqa: E501


        :return: The address1 of this ContactDetailsInput.  # noqa: E501
        :rtype: object
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """Sets the address1 of this ContactDetailsInput.


        :param address1: The address1 of this ContactDetailsInput.  # noqa: E501
        :type: object
        """

        self._address1 = address1

    @property
    def address2(self):
        """Gets the address2 of this ContactDetailsInput.  # noqa: E501


        :return: The address2 of this ContactDetailsInput.  # noqa: E501
        :rtype: object
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """Sets the address2 of this ContactDetailsInput.


        :param address2: The address2 of this ContactDetailsInput.  # noqa: E501
        :type: object
        """

        self._address2 = address2

    @property
    def address3(self):
        """Gets the address3 of this ContactDetailsInput.  # noqa: E501


        :return: The address3 of this ContactDetailsInput.  # noqa: E501
        :rtype: object
        """
        return self._address3

    @address3.setter
    def address3(self, address3):
        """Sets the address3 of this ContactDetailsInput.


        :param address3: The address3 of this ContactDetailsInput.  # noqa: E501
        :type: object
        """

        self._address3 = address3

    @property
    def city(self):
        """Gets the city of this ContactDetailsInput.  # noqa: E501


        :return: The city of this ContactDetailsInput.  # noqa: E501
        :rtype: object
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this ContactDetailsInput.


        :param city: The city of this ContactDetailsInput.  # noqa: E501
        :type: object
        """

        self._city = city

    @property
    def region(self):
        """Gets the region of this ContactDetailsInput.  # noqa: E501


        :return: The region of this ContactDetailsInput.  # noqa: E501
        :rtype: object
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ContactDetailsInput.


        :param region: The region of this ContactDetailsInput.  # noqa: E501
        :type: object
        """

        self._region = region

    @property
    def postal_code(self):
        """Gets the postal_code of this ContactDetailsInput.  # noqa: E501


        :return: The postal_code of this ContactDetailsInput.  # noqa: E501
        :rtype: object
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this ContactDetailsInput.


        :param postal_code: The postal_code of this ContactDetailsInput.  # noqa: E501
        :type: object
        """

        self._postal_code = postal_code

    @property
    def country(self):
        """Gets the country of this ContactDetailsInput.  # noqa: E501


        :return: The country of this ContactDetailsInput.  # noqa: E501
        :rtype: object
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this ContactDetailsInput.


        :param country: The country of this ContactDetailsInput.  # noqa: E501
        :type: object
        """

        self._country = country

    @property
    def email(self):
        """Gets the email of this ContactDetailsInput.  # noqa: E501


        :return: The email of this ContactDetailsInput.  # noqa: E501
        :rtype: object
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ContactDetailsInput.


        :param email: The email of this ContactDetailsInput.  # noqa: E501
        :type: object
        """

        self._email = email

    @property
    def phone(self):
        """Gets the phone of this ContactDetailsInput.  # noqa: E501


        :return: The phone of this ContactDetailsInput.  # noqa: E501
        :rtype: object
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this ContactDetailsInput.


        :param phone: The phone of this ContactDetailsInput.  # noqa: E501
        :type: object
        """

        self._phone = phone

    @property
    def comments(self):
        """Gets the comments of this ContactDetailsInput.  # noqa: E501


        :return: The comments of this ContactDetailsInput.  # noqa: E501
        :rtype: object
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this ContactDetailsInput.


        :param comments: The comments of this ContactDetailsInput.  # noqa: E501
        :type: object
        """

        self._comments = comments

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
        if issubclass(ContactDetailsInput, dict):
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
        if not isinstance(other, ContactDetailsInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
