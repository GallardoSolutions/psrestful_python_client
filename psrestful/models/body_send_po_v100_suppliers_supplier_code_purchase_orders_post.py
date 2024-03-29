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

class BodySendPoV100SuppliersSupplierCodePurchaseOrdersPost(object):
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
        'po': 'PO',
        'pub_api_key': 'object'
    }

    attribute_map = {
        'po': 'po',
        'pub_api_key': 'pub_api_key'
    }

    def __init__(self, po=None, pub_api_key=None):  # noqa: E501
        """BodySendPoV100SuppliersSupplierCodePurchaseOrdersPost - a model defined in Swagger"""  # noqa: E501
        self._po = None
        self._pub_api_key = None
        self.discriminator = None
        self.po = po
        if pub_api_key is not None:
            self.pub_api_key = pub_api_key

    @property
    def po(self):
        """Gets the po of this BodySendPoV100SuppliersSupplierCodePurchaseOrdersPost.  # noqa: E501


        :return: The po of this BodySendPoV100SuppliersSupplierCodePurchaseOrdersPost.  # noqa: E501
        :rtype: PO
        """
        return self._po

    @po.setter
    def po(self, po):
        """Sets the po of this BodySendPoV100SuppliersSupplierCodePurchaseOrdersPost.


        :param po: The po of this BodySendPoV100SuppliersSupplierCodePurchaseOrdersPost.  # noqa: E501
        :type: PO
        """
        if po is None:
            raise ValueError("Invalid value for `po`, must not be `None`")  # noqa: E501

        self._po = po

    @property
    def pub_api_key(self):
        """Gets the pub_api_key of this BodySendPoV100SuppliersSupplierCodePurchaseOrdersPost.  # noqa: E501


        :return: The pub_api_key of this BodySendPoV100SuppliersSupplierCodePurchaseOrdersPost.  # noqa: E501
        :rtype: object
        """
        return self._pub_api_key

    @pub_api_key.setter
    def pub_api_key(self, pub_api_key):
        """Sets the pub_api_key of this BodySendPoV100SuppliersSupplierCodePurchaseOrdersPost.


        :param pub_api_key: The pub_api_key of this BodySendPoV100SuppliersSupplierCodePurchaseOrdersPost.  # noqa: E501
        :type: object
        """

        self._pub_api_key = pub_api_key

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
        if issubclass(BodySendPoV100SuppliersSupplierCodePurchaseOrdersPost, dict):
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
        if not isinstance(other, BodySendPoV100SuppliersSupplierCodePurchaseOrdersPost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
