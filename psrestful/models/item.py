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

class Item(object):
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
        'supplier_product_id': 'object',
        'supplier_part_id': 'object',
        'distributor_product_id': 'object',
        'distributor_part_id': 'object',
        'purchase_order_line_number': 'object',
        'quantity': 'object'
    }

    attribute_map = {
        'supplier_product_id': 'supplierProductId',
        'supplier_part_id': 'supplierPartId',
        'distributor_product_id': 'distributorProductId',
        'distributor_part_id': 'distributorPartId',
        'purchase_order_line_number': 'purchaseOrderLineNumber',
        'quantity': 'quantity'
    }

    def __init__(self, supplier_product_id=None, supplier_part_id=None, distributor_product_id=None, distributor_part_id=None, purchase_order_line_number=None, quantity=None):  # noqa: E501
        """Item - a model defined in Swagger"""  # noqa: E501
        self._supplier_product_id = None
        self._supplier_part_id = None
        self._distributor_product_id = None
        self._distributor_part_id = None
        self._purchase_order_line_number = None
        self._quantity = None
        self.discriminator = None
        self.supplier_product_id = supplier_product_id
        self.supplier_part_id = supplier_part_id
        self.distributor_product_id = distributor_product_id
        self.distributor_part_id = distributor_part_id
        self.purchase_order_line_number = purchase_order_line_number
        self.quantity = quantity

    @property
    def supplier_product_id(self):
        """Gets the supplier_product_id of this Item.  # noqa: E501


        :return: The supplier_product_id of this Item.  # noqa: E501
        :rtype: object
        """
        return self._supplier_product_id

    @supplier_product_id.setter
    def supplier_product_id(self, supplier_product_id):
        """Sets the supplier_product_id of this Item.


        :param supplier_product_id: The supplier_product_id of this Item.  # noqa: E501
        :type: object
        """
        if supplier_product_id is None:
            raise ValueError("Invalid value for `supplier_product_id`, must not be `None`")  # noqa: E501

        self._supplier_product_id = supplier_product_id

    @property
    def supplier_part_id(self):
        """Gets the supplier_part_id of this Item.  # noqa: E501


        :return: The supplier_part_id of this Item.  # noqa: E501
        :rtype: object
        """
        return self._supplier_part_id

    @supplier_part_id.setter
    def supplier_part_id(self, supplier_part_id):
        """Sets the supplier_part_id of this Item.


        :param supplier_part_id: The supplier_part_id of this Item.  # noqa: E501
        :type: object
        """
        if supplier_part_id is None:
            raise ValueError("Invalid value for `supplier_part_id`, must not be `None`")  # noqa: E501

        self._supplier_part_id = supplier_part_id

    @property
    def distributor_product_id(self):
        """Gets the distributor_product_id of this Item.  # noqa: E501


        :return: The distributor_product_id of this Item.  # noqa: E501
        :rtype: object
        """
        return self._distributor_product_id

    @distributor_product_id.setter
    def distributor_product_id(self, distributor_product_id):
        """Sets the distributor_product_id of this Item.


        :param distributor_product_id: The distributor_product_id of this Item.  # noqa: E501
        :type: object
        """
        if distributor_product_id is None:
            raise ValueError("Invalid value for `distributor_product_id`, must not be `None`")  # noqa: E501

        self._distributor_product_id = distributor_product_id

    @property
    def distributor_part_id(self):
        """Gets the distributor_part_id of this Item.  # noqa: E501


        :return: The distributor_part_id of this Item.  # noqa: E501
        :rtype: object
        """
        return self._distributor_part_id

    @distributor_part_id.setter
    def distributor_part_id(self, distributor_part_id):
        """Sets the distributor_part_id of this Item.


        :param distributor_part_id: The distributor_part_id of this Item.  # noqa: E501
        :type: object
        """
        if distributor_part_id is None:
            raise ValueError("Invalid value for `distributor_part_id`, must not be `None`")  # noqa: E501

        self._distributor_part_id = distributor_part_id

    @property
    def purchase_order_line_number(self):
        """Gets the purchase_order_line_number of this Item.  # noqa: E501


        :return: The purchase_order_line_number of this Item.  # noqa: E501
        :rtype: object
        """
        return self._purchase_order_line_number

    @purchase_order_line_number.setter
    def purchase_order_line_number(self, purchase_order_line_number):
        """Sets the purchase_order_line_number of this Item.


        :param purchase_order_line_number: The purchase_order_line_number of this Item.  # noqa: E501
        :type: object
        """
        if purchase_order_line_number is None:
            raise ValueError("Invalid value for `purchase_order_line_number`, must not be `None`")  # noqa: E501

        self._purchase_order_line_number = purchase_order_line_number

    @property
    def quantity(self):
        """Gets the quantity of this Item.  # noqa: E501


        :return: The quantity of this Item.  # noqa: E501
        :rtype: object
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this Item.


        :param quantity: The quantity of this Item.  # noqa: E501
        :type: object
        """
        if quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")  # noqa: E501

        self._quantity = quantity

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
        if issubclass(Item, dict):
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
        if not isinstance(other, Item):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
