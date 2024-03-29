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

class PsDomainModelOrderStatusV200OrderStatusDetail(object):
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
        'sales_order_number': 'object',
        'status': 'object',
        'issue_category': 'object',
        'expected_ship_date': 'object',
        'expected_delivery_date': 'object',
        'additional_explanation': 'object',
        'quality_proof_url': 'object',
        'order_contact_array': 'object',
        'product_array': 'object',
        'issue_array': 'object',
        'valid_timestamp': 'object'
    }

    attribute_map = {
        'sales_order_number': 'salesOrderNumber',
        'status': 'status',
        'issue_category': 'issueCategory',
        'expected_ship_date': 'expectedShipDate',
        'expected_delivery_date': 'expectedDeliveryDate',
        'additional_explanation': 'additionalExplanation',
        'quality_proof_url': 'qualityProofURL',
        'order_contact_array': 'OrderContactArray',
        'product_array': 'ProductArray',
        'issue_array': 'IssueArray',
        'valid_timestamp': 'validTimestamp'
    }

    def __init__(self, sales_order_number=None, status=None, issue_category=None, expected_ship_date=None, expected_delivery_date=None, additional_explanation=None, quality_proof_url=None, order_contact_array=None, product_array=None, issue_array=None, valid_timestamp=None):  # noqa: E501
        """PsDomainModelOrderStatusV200OrderStatusDetail - a model defined in Swagger"""  # noqa: E501
        self._sales_order_number = None
        self._status = None
        self._issue_category = None
        self._expected_ship_date = None
        self._expected_delivery_date = None
        self._additional_explanation = None
        self._quality_proof_url = None
        self._order_contact_array = None
        self._product_array = None
        self._issue_array = None
        self._valid_timestamp = None
        self.discriminator = None
        self.sales_order_number = sales_order_number
        self.status = status
        if issue_category is not None:
            self.issue_category = issue_category
        if expected_ship_date is not None:
            self.expected_ship_date = expected_ship_date
        if expected_delivery_date is not None:
            self.expected_delivery_date = expected_delivery_date
        if additional_explanation is not None:
            self.additional_explanation = additional_explanation
        if quality_proof_url is not None:
            self.quality_proof_url = quality_proof_url
        if order_contact_array is not None:
            self.order_contact_array = order_contact_array
        if product_array is not None:
            self.product_array = product_array
        if issue_array is not None:
            self.issue_array = issue_array
        self.valid_timestamp = valid_timestamp

    @property
    def sales_order_number(self):
        """Gets the sales_order_number of this PsDomainModelOrderStatusV200OrderStatusDetail.  # noqa: E501


        :return: The sales_order_number of this PsDomainModelOrderStatusV200OrderStatusDetail.  # noqa: E501
        :rtype: object
        """
        return self._sales_order_number

    @sales_order_number.setter
    def sales_order_number(self, sales_order_number):
        """Sets the sales_order_number of this PsDomainModelOrderStatusV200OrderStatusDetail.


        :param sales_order_number: The sales_order_number of this PsDomainModelOrderStatusV200OrderStatusDetail.  # noqa: E501
        :type: object
        """
        if sales_order_number is None:
            raise ValueError("Invalid value for `sales_order_number`, must not be `None`")  # noqa: E501

        self._sales_order_number = sales_order_number

    @property
    def status(self):
        """Gets the status of this PsDomainModelOrderStatusV200OrderStatusDetail.  # noqa: E501


        :return: The status of this PsDomainModelOrderStatusV200OrderStatusDetail.  # noqa: E501
        :rtype: object
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PsDomainModelOrderStatusV200OrderStatusDetail.


        :param status: The status of this PsDomainModelOrderStatusV200OrderStatusDetail.  # noqa: E501
        :type: object
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def issue_category(self):
        """Gets the issue_category of this PsDomainModelOrderStatusV200OrderStatusDetail.  # noqa: E501


        :return: The issue_category of this PsDomainModelOrderStatusV200OrderStatusDetail.  # noqa: E501
        :rtype: object
        """
        return self._issue_category

    @issue_category.setter
    def issue_category(self, issue_category):
        """Sets the issue_category of this PsDomainModelOrderStatusV200OrderStatusDetail.


        :param issue_category: The issue_category of this PsDomainModelOrderStatusV200OrderStatusDetail.  # noqa: E501
        :type: object
        """

        self._issue_category = issue_category

    @property
    def expected_ship_date(self):
        """Gets the expected_ship_date of this PsDomainModelOrderStatusV200OrderStatusDetail.  # noqa: E501


        :return: The expected_ship_date of this PsDomainModelOrderStatusV200OrderStatusDetail.  # noqa: E501
        :rtype: object
        """
        return self._expected_ship_date

    @expected_ship_date.setter
    def expected_ship_date(self, expected_ship_date):
        """Sets the expected_ship_date of this PsDomainModelOrderStatusV200OrderStatusDetail.


        :param expected_ship_date: The expected_ship_date of this PsDomainModelOrderStatusV200OrderStatusDetail.  # noqa: E501
        :type: object
        """

        self._expected_ship_date = expected_ship_date

    @property
    def expected_delivery_date(self):
        """Gets the expected_delivery_date of this PsDomainModelOrderStatusV200OrderStatusDetail.  # noqa: E501


        :return: The expected_delivery_date of this PsDomainModelOrderStatusV200OrderStatusDetail.  # noqa: E501
        :rtype: object
        """
        return self._expected_delivery_date

    @expected_delivery_date.setter
    def expected_delivery_date(self, expected_delivery_date):
        """Sets the expected_delivery_date of this PsDomainModelOrderStatusV200OrderStatusDetail.


        :param expected_delivery_date: The expected_delivery_date of this PsDomainModelOrderStatusV200OrderStatusDetail.  # noqa: E501
        :type: object
        """

        self._expected_delivery_date = expected_delivery_date

    @property
    def additional_explanation(self):
        """Gets the additional_explanation of this PsDomainModelOrderStatusV200OrderStatusDetail.  # noqa: E501


        :return: The additional_explanation of this PsDomainModelOrderStatusV200OrderStatusDetail.  # noqa: E501
        :rtype: object
        """
        return self._additional_explanation

    @additional_explanation.setter
    def additional_explanation(self, additional_explanation):
        """Sets the additional_explanation of this PsDomainModelOrderStatusV200OrderStatusDetail.


        :param additional_explanation: The additional_explanation of this PsDomainModelOrderStatusV200OrderStatusDetail.  # noqa: E501
        :type: object
        """

        self._additional_explanation = additional_explanation

    @property
    def quality_proof_url(self):
        """Gets the quality_proof_url of this PsDomainModelOrderStatusV200OrderStatusDetail.  # noqa: E501


        :return: The quality_proof_url of this PsDomainModelOrderStatusV200OrderStatusDetail.  # noqa: E501
        :rtype: object
        """
        return self._quality_proof_url

    @quality_proof_url.setter
    def quality_proof_url(self, quality_proof_url):
        """Sets the quality_proof_url of this PsDomainModelOrderStatusV200OrderStatusDetail.


        :param quality_proof_url: The quality_proof_url of this PsDomainModelOrderStatusV200OrderStatusDetail.  # noqa: E501
        :type: object
        """

        self._quality_proof_url = quality_proof_url

    @property
    def order_contact_array(self):
        """Gets the order_contact_array of this PsDomainModelOrderStatusV200OrderStatusDetail.  # noqa: E501


        :return: The order_contact_array of this PsDomainModelOrderStatusV200OrderStatusDetail.  # noqa: E501
        :rtype: object
        """
        return self._order_contact_array

    @order_contact_array.setter
    def order_contact_array(self, order_contact_array):
        """Sets the order_contact_array of this PsDomainModelOrderStatusV200OrderStatusDetail.


        :param order_contact_array: The order_contact_array of this PsDomainModelOrderStatusV200OrderStatusDetail.  # noqa: E501
        :type: object
        """

        self._order_contact_array = order_contact_array

    @property
    def product_array(self):
        """Gets the product_array of this PsDomainModelOrderStatusV200OrderStatusDetail.  # noqa: E501


        :return: The product_array of this PsDomainModelOrderStatusV200OrderStatusDetail.  # noqa: E501
        :rtype: object
        """
        return self._product_array

    @product_array.setter
    def product_array(self, product_array):
        """Sets the product_array of this PsDomainModelOrderStatusV200OrderStatusDetail.


        :param product_array: The product_array of this PsDomainModelOrderStatusV200OrderStatusDetail.  # noqa: E501
        :type: object
        """

        self._product_array = product_array

    @property
    def issue_array(self):
        """Gets the issue_array of this PsDomainModelOrderStatusV200OrderStatusDetail.  # noqa: E501


        :return: The issue_array of this PsDomainModelOrderStatusV200OrderStatusDetail.  # noqa: E501
        :rtype: object
        """
        return self._issue_array

    @issue_array.setter
    def issue_array(self, issue_array):
        """Sets the issue_array of this PsDomainModelOrderStatusV200OrderStatusDetail.


        :param issue_array: The issue_array of this PsDomainModelOrderStatusV200OrderStatusDetail.  # noqa: E501
        :type: object
        """

        self._issue_array = issue_array

    @property
    def valid_timestamp(self):
        """Gets the valid_timestamp of this PsDomainModelOrderStatusV200OrderStatusDetail.  # noqa: E501


        :return: The valid_timestamp of this PsDomainModelOrderStatusV200OrderStatusDetail.  # noqa: E501
        :rtype: object
        """
        return self._valid_timestamp

    @valid_timestamp.setter
    def valid_timestamp(self, valid_timestamp):
        """Sets the valid_timestamp of this PsDomainModelOrderStatusV200OrderStatusDetail.


        :param valid_timestamp: The valid_timestamp of this PsDomainModelOrderStatusV200OrderStatusDetail.  # noqa: E501
        :type: object
        """
        if valid_timestamp is None:
            raise ValueError("Invalid value for `valid_timestamp`, must not be `None`")  # noqa: E501

        self._valid_timestamp = valid_timestamp

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
        if issubclass(PsDomainModelOrderStatusV200OrderStatusDetail, dict):
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
        if not isinstance(other, PsDomainModelOrderStatusV200OrderStatusDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
