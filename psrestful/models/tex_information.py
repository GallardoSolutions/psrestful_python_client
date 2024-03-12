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

class TexInformation(object):
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
        'tax_id': 'object',
        'tax_type': 'TaxTypeInput',
        'tax_exempt': 'object',
        'tax_jurisdiction': 'object',
        'tax_amount': 'object'
    }

    attribute_map = {
        'tax_id': 'taxId',
        'tax_type': 'taxType',
        'tax_exempt': 'taxExempt',
        'tax_jurisdiction': 'taxJurisdiction',
        'tax_amount': 'taxAmount'
    }

    def __init__(self, tax_id=None, tax_type=None, tax_exempt=None, tax_jurisdiction=None, tax_amount=None):  # noqa: E501
        """TexInformation - a model defined in Swagger"""  # noqa: E501
        self._tax_id = None
        self._tax_type = None
        self._tax_exempt = None
        self._tax_jurisdiction = None
        self._tax_amount = None
        self.discriminator = None
        self.tax_id = tax_id
        self.tax_type = tax_type
        self.tax_exempt = tax_exempt
        self.tax_jurisdiction = tax_jurisdiction
        self.tax_amount = tax_amount

    @property
    def tax_id(self):
        """Gets the tax_id of this TexInformation.  # noqa: E501

        The purchasers tax identifier  # noqa: E501

        :return: The tax_id of this TexInformation.  # noqa: E501
        :rtype: object
        """
        return self._tax_id

    @tax_id.setter
    def tax_id(self, tax_id):
        """Sets the tax_id of this TexInformation.

        The purchasers tax identifier  # noqa: E501

        :param tax_id: The tax_id of this TexInformation.  # noqa: E501
        :type: object
        """
        if tax_id is None:
            raise ValueError("Invalid value for `tax_id`, must not be `None`")  # noqa: E501

        self._tax_id = tax_id

    @property
    def tax_type(self):
        """Gets the tax_type of this TexInformation.  # noqa: E501


        :return: The tax_type of this TexInformation.  # noqa: E501
        :rtype: TaxTypeInput
        """
        return self._tax_type

    @tax_type.setter
    def tax_type(self, tax_type):
        """Sets the tax_type of this TexInformation.


        :param tax_type: The tax_type of this TexInformation.  # noqa: E501
        :type: TaxTypeInput
        """
        if tax_type is None:
            raise ValueError("Invalid value for `tax_type`, must not be `None`")  # noqa: E501

        self._tax_type = tax_type

    @property
    def tax_exempt(self):
        """Gets the tax_exempt of this TexInformation.  # noqa: E501


        :return: The tax_exempt of this TexInformation.  # noqa: E501
        :rtype: object
        """
        return self._tax_exempt

    @tax_exempt.setter
    def tax_exempt(self, tax_exempt):
        """Sets the tax_exempt of this TexInformation.


        :param tax_exempt: The tax_exempt of this TexInformation.  # noqa: E501
        :type: object
        """
        if tax_exempt is None:
            raise ValueError("Invalid value for `tax_exempt`, must not be `None`")  # noqa: E501

        self._tax_exempt = tax_exempt

    @property
    def tax_jurisdiction(self):
        """Gets the tax_jurisdiction of this TexInformation.  # noqa: E501


        :return: The tax_jurisdiction of this TexInformation.  # noqa: E501
        :rtype: object
        """
        return self._tax_jurisdiction

    @tax_jurisdiction.setter
    def tax_jurisdiction(self, tax_jurisdiction):
        """Sets the tax_jurisdiction of this TexInformation.


        :param tax_jurisdiction: The tax_jurisdiction of this TexInformation.  # noqa: E501
        :type: object
        """
        if tax_jurisdiction is None:
            raise ValueError("Invalid value for `tax_jurisdiction`, must not be `None`")  # noqa: E501

        self._tax_jurisdiction = tax_jurisdiction

    @property
    def tax_amount(self):
        """Gets the tax_amount of this TexInformation.  # noqa: E501

        The amount of tax for this purchase order  # noqa: E501

        :return: The tax_amount of this TexInformation.  # noqa: E501
        :rtype: object
        """
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, tax_amount):
        """Sets the tax_amount of this TexInformation.

        The amount of tax for this purchase order  # noqa: E501

        :param tax_amount: The tax_amount of this TexInformation.  # noqa: E501
        :type: object
        """
        if tax_amount is None:
            raise ValueError("Invalid value for `tax_amount`, must not be `None`")  # noqa: E501

        self._tax_amount = tax_amount

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
        if issubclass(TexInformation, dict):
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
        if not isinstance(other, TexInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
