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

class PsDomainModelOrderStatusV100OrderStatusDetail(object):
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
        'factory_order_number': 'object',
        'status_id': 'object',
        'status_name': 'object',
        'response_required': 'object',
        'valid_timestamp': 'object',
        'expected_ship_date': 'object',
        'expected_delivery_date': 'object',
        'response_to_array': 'object',
        'additional_explanation': 'object'
    }

    attribute_map = {
        'factory_order_number': 'factoryOrderNumber',
        'status_id': 'statusID',
        'status_name': 'statusName',
        'response_required': 'responseRequired',
        'valid_timestamp': 'validTimestamp',
        'expected_ship_date': 'expectedShipDate',
        'expected_delivery_date': 'expectedDeliveryDate',
        'response_to_array': 'ResponseToArray',
        'additional_explanation': 'additionalExplanation'
    }

    def __init__(self, factory_order_number=None, status_id=None, status_name=None, response_required=None, valid_timestamp=None, expected_ship_date=None, expected_delivery_date=None, response_to_array=None, additional_explanation=None):  # noqa: E501
        """PsDomainModelOrderStatusV100OrderStatusDetail - a model defined in Swagger"""  # noqa: E501
        self._factory_order_number = None
        self._status_id = None
        self._status_name = None
        self._response_required = None
        self._valid_timestamp = None
        self._expected_ship_date = None
        self._expected_delivery_date = None
        self._response_to_array = None
        self._additional_explanation = None
        self.discriminator = None
        self.factory_order_number = factory_order_number
        self.status_id = status_id
        self.status_name = status_name
        if response_required is not None:
            self.response_required = response_required
        self.valid_timestamp = valid_timestamp
        self.expected_ship_date = expected_ship_date
        self.expected_delivery_date = expected_delivery_date
        self.response_to_array = response_to_array
        self.additional_explanation = additional_explanation

    @property
    def factory_order_number(self):
        """Gets the factory_order_number of this PsDomainModelOrderStatusV100OrderStatusDetail.  # noqa: E501


        :return: The factory_order_number of this PsDomainModelOrderStatusV100OrderStatusDetail.  # noqa: E501
        :rtype: object
        """
        return self._factory_order_number

    @factory_order_number.setter
    def factory_order_number(self, factory_order_number):
        """Sets the factory_order_number of this PsDomainModelOrderStatusV100OrderStatusDetail.


        :param factory_order_number: The factory_order_number of this PsDomainModelOrderStatusV100OrderStatusDetail.  # noqa: E501
        :type: object
        """
        if factory_order_number is None:
            raise ValueError("Invalid value for `factory_order_number`, must not be `None`")  # noqa: E501

        self._factory_order_number = factory_order_number

    @property
    def status_id(self):
        """Gets the status_id of this PsDomainModelOrderStatusV100OrderStatusDetail.  # noqa: E501


        :return: The status_id of this PsDomainModelOrderStatusV100OrderStatusDetail.  # noqa: E501
        :rtype: object
        """
        return self._status_id

    @status_id.setter
    def status_id(self, status_id):
        """Sets the status_id of this PsDomainModelOrderStatusV100OrderStatusDetail.


        :param status_id: The status_id of this PsDomainModelOrderStatusV100OrderStatusDetail.  # noqa: E501
        :type: object
        """
        if status_id is None:
            raise ValueError("Invalid value for `status_id`, must not be `None`")  # noqa: E501

        self._status_id = status_id

    @property
    def status_name(self):
        """Gets the status_name of this PsDomainModelOrderStatusV100OrderStatusDetail.  # noqa: E501


        :return: The status_name of this PsDomainModelOrderStatusV100OrderStatusDetail.  # noqa: E501
        :rtype: object
        """
        return self._status_name

    @status_name.setter
    def status_name(self, status_name):
        """Sets the status_name of this PsDomainModelOrderStatusV100OrderStatusDetail.


        :param status_name: The status_name of this PsDomainModelOrderStatusV100OrderStatusDetail.  # noqa: E501
        :type: object
        """
        if status_name is None:
            raise ValueError("Invalid value for `status_name`, must not be `None`")  # noqa: E501

        self._status_name = status_name

    @property
    def response_required(self):
        """Gets the response_required of this PsDomainModelOrderStatusV100OrderStatusDetail.  # noqa: E501


        :return: The response_required of this PsDomainModelOrderStatusV100OrderStatusDetail.  # noqa: E501
        :rtype: object
        """
        return self._response_required

    @response_required.setter
    def response_required(self, response_required):
        """Sets the response_required of this PsDomainModelOrderStatusV100OrderStatusDetail.


        :param response_required: The response_required of this PsDomainModelOrderStatusV100OrderStatusDetail.  # noqa: E501
        :type: object
        """

        self._response_required = response_required

    @property
    def valid_timestamp(self):
        """Gets the valid_timestamp of this PsDomainModelOrderStatusV100OrderStatusDetail.  # noqa: E501


        :return: The valid_timestamp of this PsDomainModelOrderStatusV100OrderStatusDetail.  # noqa: E501
        :rtype: object
        """
        return self._valid_timestamp

    @valid_timestamp.setter
    def valid_timestamp(self, valid_timestamp):
        """Sets the valid_timestamp of this PsDomainModelOrderStatusV100OrderStatusDetail.


        :param valid_timestamp: The valid_timestamp of this PsDomainModelOrderStatusV100OrderStatusDetail.  # noqa: E501
        :type: object
        """
        if valid_timestamp is None:
            raise ValueError("Invalid value for `valid_timestamp`, must not be `None`")  # noqa: E501

        self._valid_timestamp = valid_timestamp

    @property
    def expected_ship_date(self):
        """Gets the expected_ship_date of this PsDomainModelOrderStatusV100OrderStatusDetail.  # noqa: E501


        :return: The expected_ship_date of this PsDomainModelOrderStatusV100OrderStatusDetail.  # noqa: E501
        :rtype: object
        """
        return self._expected_ship_date

    @expected_ship_date.setter
    def expected_ship_date(self, expected_ship_date):
        """Sets the expected_ship_date of this PsDomainModelOrderStatusV100OrderStatusDetail.


        :param expected_ship_date: The expected_ship_date of this PsDomainModelOrderStatusV100OrderStatusDetail.  # noqa: E501
        :type: object
        """
        if expected_ship_date is None:
            raise ValueError("Invalid value for `expected_ship_date`, must not be `None`")  # noqa: E501

        self._expected_ship_date = expected_ship_date

    @property
    def expected_delivery_date(self):
        """Gets the expected_delivery_date of this PsDomainModelOrderStatusV100OrderStatusDetail.  # noqa: E501


        :return: The expected_delivery_date of this PsDomainModelOrderStatusV100OrderStatusDetail.  # noqa: E501
        :rtype: object
        """
        return self._expected_delivery_date

    @expected_delivery_date.setter
    def expected_delivery_date(self, expected_delivery_date):
        """Sets the expected_delivery_date of this PsDomainModelOrderStatusV100OrderStatusDetail.


        :param expected_delivery_date: The expected_delivery_date of this PsDomainModelOrderStatusV100OrderStatusDetail.  # noqa: E501
        :type: object
        """
        if expected_delivery_date is None:
            raise ValueError("Invalid value for `expected_delivery_date`, must not be `None`")  # noqa: E501

        self._expected_delivery_date = expected_delivery_date

    @property
    def response_to_array(self):
        """Gets the response_to_array of this PsDomainModelOrderStatusV100OrderStatusDetail.  # noqa: E501


        :return: The response_to_array of this PsDomainModelOrderStatusV100OrderStatusDetail.  # noqa: E501
        :rtype: object
        """
        return self._response_to_array

    @response_to_array.setter
    def response_to_array(self, response_to_array):
        """Sets the response_to_array of this PsDomainModelOrderStatusV100OrderStatusDetail.


        :param response_to_array: The response_to_array of this PsDomainModelOrderStatusV100OrderStatusDetail.  # noqa: E501
        :type: object
        """
        if response_to_array is None:
            raise ValueError("Invalid value for `response_to_array`, must not be `None`")  # noqa: E501

        self._response_to_array = response_to_array

    @property
    def additional_explanation(self):
        """Gets the additional_explanation of this PsDomainModelOrderStatusV100OrderStatusDetail.  # noqa: E501


        :return: The additional_explanation of this PsDomainModelOrderStatusV100OrderStatusDetail.  # noqa: E501
        :rtype: object
        """
        return self._additional_explanation

    @additional_explanation.setter
    def additional_explanation(self, additional_explanation):
        """Sets the additional_explanation of this PsDomainModelOrderStatusV100OrderStatusDetail.


        :param additional_explanation: The additional_explanation of this PsDomainModelOrderStatusV100OrderStatusDetail.  # noqa: E501
        :type: object
        """
        if additional_explanation is None:
            raise ValueError("Invalid value for `additional_explanation`, must not be `None`")  # noqa: E501

        self._additional_explanation = additional_explanation

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
        if issubclass(PsDomainModelOrderStatusV100OrderStatusDetail, dict):
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
        if not isinstance(other, PsDomainModelOrderStatusV100OrderStatusDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
