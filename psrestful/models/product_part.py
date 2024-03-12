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

class ProductPart(object):
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
        'part_id': 'object',
        'description': 'object',
        'country_of_origin': 'object',
        'primary_material': 'object',
        'shape': 'object',
        'apparel_size': 'object',
        'dimension': 'object',
        'lead_time': 'object',
        'unspsc': 'object',
        'gtin': 'object',
        'is_rush_service': 'object',
        'end_date': 'object',
        'effective_date': 'object',
        'is_closeout': 'object',
        'is_caution': 'object',
        'caution_comment': 'object',
        'nmfc_code': 'object',
        'nmfc_description': 'object',
        'nmfc_number': 'object',
        'is_on_demand': 'object',
        'is_hazmat': 'object',
        'primary_color': 'object',
        'color_array': 'object',
        'product_packaging_array': 'object',
        'shipping_package_array': 'object'
    }

    attribute_map = {
        'part_id': 'partId',
        'description': 'description',
        'country_of_origin': 'countryOfOrigin',
        'primary_material': 'primaryMaterial',
        'shape': 'shape',
        'apparel_size': 'ApparelSize',
        'dimension': 'Dimension',
        'lead_time': 'leadTime',
        'unspsc': 'unspsc',
        'gtin': 'gtin',
        'is_rush_service': 'isRushService',
        'end_date': 'endDate',
        'effective_date': 'effectiveDate',
        'is_closeout': 'isCloseout',
        'is_caution': 'isCaution',
        'caution_comment': 'cautionComment',
        'nmfc_code': 'nmfcCode',
        'nmfc_description': 'nmfcDescription',
        'nmfc_number': 'nmfcNumber',
        'is_on_demand': 'isOnDemand',
        'is_hazmat': 'isHazmat',
        'primary_color': 'primaryColor',
        'color_array': 'ColorArray',
        'product_packaging_array': 'ProductPackagingArray',
        'shipping_package_array': 'ShippingPackageArray'
    }

    def __init__(self, part_id=None, description=None, country_of_origin=None, primary_material=None, shape=None, apparel_size=None, dimension=None, lead_time=None, unspsc=None, gtin=None, is_rush_service=None, end_date=None, effective_date=None, is_closeout=None, is_caution=None, caution_comment=None, nmfc_code=None, nmfc_description=None, nmfc_number=None, is_on_demand=None, is_hazmat=None, primary_color=None, color_array=None, product_packaging_array=None, shipping_package_array=None):  # noqa: E501
        """ProductPart - a model defined in Swagger"""  # noqa: E501
        self._part_id = None
        self._description = None
        self._country_of_origin = None
        self._primary_material = None
        self._shape = None
        self._apparel_size = None
        self._dimension = None
        self._lead_time = None
        self._unspsc = None
        self._gtin = None
        self._is_rush_service = None
        self._end_date = None
        self._effective_date = None
        self._is_closeout = None
        self._is_caution = None
        self._caution_comment = None
        self._nmfc_code = None
        self._nmfc_description = None
        self._nmfc_number = None
        self._is_on_demand = None
        self._is_hazmat = None
        self._primary_color = None
        self._color_array = None
        self._product_packaging_array = None
        self._shipping_package_array = None
        self.discriminator = None
        self.part_id = part_id
        self.description = description
        self.country_of_origin = country_of_origin
        self.primary_material = primary_material
        self.shape = shape
        self.apparel_size = apparel_size
        self.dimension = dimension
        self.lead_time = lead_time
        self.unspsc = unspsc
        self.gtin = gtin
        self.is_rush_service = is_rush_service
        self.end_date = end_date
        self.effective_date = effective_date
        self.is_closeout = is_closeout
        self.is_caution = is_caution
        self.caution_comment = caution_comment
        self.nmfc_code = nmfc_code
        self.nmfc_description = nmfc_description
        self.nmfc_number = nmfc_number
        self.is_on_demand = is_on_demand
        self.is_hazmat = is_hazmat
        if primary_color is not None:
            self.primary_color = primary_color
        self.color_array = color_array
        self.product_packaging_array = product_packaging_array
        self.shipping_package_array = shipping_package_array

    @property
    def part_id(self):
        """Gets the part_id of this ProductPart.  # noqa: E501


        :return: The part_id of this ProductPart.  # noqa: E501
        :rtype: object
        """
        return self._part_id

    @part_id.setter
    def part_id(self, part_id):
        """Sets the part_id of this ProductPart.


        :param part_id: The part_id of this ProductPart.  # noqa: E501
        :type: object
        """
        if part_id is None:
            raise ValueError("Invalid value for `part_id`, must not be `None`")  # noqa: E501

        self._part_id = part_id

    @property
    def description(self):
        """Gets the description of this ProductPart.  # noqa: E501


        :return: The description of this ProductPart.  # noqa: E501
        :rtype: object
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ProductPart.


        :param description: The description of this ProductPart.  # noqa: E501
        :type: object
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def country_of_origin(self):
        """Gets the country_of_origin of this ProductPart.  # noqa: E501


        :return: The country_of_origin of this ProductPart.  # noqa: E501
        :rtype: object
        """
        return self._country_of_origin

    @country_of_origin.setter
    def country_of_origin(self, country_of_origin):
        """Sets the country_of_origin of this ProductPart.


        :param country_of_origin: The country_of_origin of this ProductPart.  # noqa: E501
        :type: object
        """
        if country_of_origin is None:
            raise ValueError("Invalid value for `country_of_origin`, must not be `None`")  # noqa: E501

        self._country_of_origin = country_of_origin

    @property
    def primary_material(self):
        """Gets the primary_material of this ProductPart.  # noqa: E501


        :return: The primary_material of this ProductPart.  # noqa: E501
        :rtype: object
        """
        return self._primary_material

    @primary_material.setter
    def primary_material(self, primary_material):
        """Sets the primary_material of this ProductPart.


        :param primary_material: The primary_material of this ProductPart.  # noqa: E501
        :type: object
        """
        if primary_material is None:
            raise ValueError("Invalid value for `primary_material`, must not be `None`")  # noqa: E501

        self._primary_material = primary_material

    @property
    def shape(self):
        """Gets the shape of this ProductPart.  # noqa: E501


        :return: The shape of this ProductPart.  # noqa: E501
        :rtype: object
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """Sets the shape of this ProductPart.


        :param shape: The shape of this ProductPart.  # noqa: E501
        :type: object
        """
        if shape is None:
            raise ValueError("Invalid value for `shape`, must not be `None`")  # noqa: E501

        self._shape = shape

    @property
    def apparel_size(self):
        """Gets the apparel_size of this ProductPart.  # noqa: E501


        :return: The apparel_size of this ProductPart.  # noqa: E501
        :rtype: object
        """
        return self._apparel_size

    @apparel_size.setter
    def apparel_size(self, apparel_size):
        """Sets the apparel_size of this ProductPart.


        :param apparel_size: The apparel_size of this ProductPart.  # noqa: E501
        :type: object
        """
        if apparel_size is None:
            raise ValueError("Invalid value for `apparel_size`, must not be `None`")  # noqa: E501

        self._apparel_size = apparel_size

    @property
    def dimension(self):
        """Gets the dimension of this ProductPart.  # noqa: E501


        :return: The dimension of this ProductPart.  # noqa: E501
        :rtype: object
        """
        return self._dimension

    @dimension.setter
    def dimension(self, dimension):
        """Sets the dimension of this ProductPart.


        :param dimension: The dimension of this ProductPart.  # noqa: E501
        :type: object
        """
        if dimension is None:
            raise ValueError("Invalid value for `dimension`, must not be `None`")  # noqa: E501

        self._dimension = dimension

    @property
    def lead_time(self):
        """Gets the lead_time of this ProductPart.  # noqa: E501


        :return: The lead_time of this ProductPart.  # noqa: E501
        :rtype: object
        """
        return self._lead_time

    @lead_time.setter
    def lead_time(self, lead_time):
        """Sets the lead_time of this ProductPart.


        :param lead_time: The lead_time of this ProductPart.  # noqa: E501
        :type: object
        """
        if lead_time is None:
            raise ValueError("Invalid value for `lead_time`, must not be `None`")  # noqa: E501

        self._lead_time = lead_time

    @property
    def unspsc(self):
        """Gets the unspsc of this ProductPart.  # noqa: E501


        :return: The unspsc of this ProductPart.  # noqa: E501
        :rtype: object
        """
        return self._unspsc

    @unspsc.setter
    def unspsc(self, unspsc):
        """Sets the unspsc of this ProductPart.


        :param unspsc: The unspsc of this ProductPart.  # noqa: E501
        :type: object
        """
        if unspsc is None:
            raise ValueError("Invalid value for `unspsc`, must not be `None`")  # noqa: E501

        self._unspsc = unspsc

    @property
    def gtin(self):
        """Gets the gtin of this ProductPart.  # noqa: E501


        :return: The gtin of this ProductPart.  # noqa: E501
        :rtype: object
        """
        return self._gtin

    @gtin.setter
    def gtin(self, gtin):
        """Sets the gtin of this ProductPart.


        :param gtin: The gtin of this ProductPart.  # noqa: E501
        :type: object
        """
        if gtin is None:
            raise ValueError("Invalid value for `gtin`, must not be `None`")  # noqa: E501

        self._gtin = gtin

    @property
    def is_rush_service(self):
        """Gets the is_rush_service of this ProductPart.  # noqa: E501


        :return: The is_rush_service of this ProductPart.  # noqa: E501
        :rtype: object
        """
        return self._is_rush_service

    @is_rush_service.setter
    def is_rush_service(self, is_rush_service):
        """Sets the is_rush_service of this ProductPart.


        :param is_rush_service: The is_rush_service of this ProductPart.  # noqa: E501
        :type: object
        """
        if is_rush_service is None:
            raise ValueError("Invalid value for `is_rush_service`, must not be `None`")  # noqa: E501

        self._is_rush_service = is_rush_service

    @property
    def end_date(self):
        """Gets the end_date of this ProductPart.  # noqa: E501


        :return: The end_date of this ProductPart.  # noqa: E501
        :rtype: object
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this ProductPart.


        :param end_date: The end_date of this ProductPart.  # noqa: E501
        :type: object
        """
        if end_date is None:
            raise ValueError("Invalid value for `end_date`, must not be `None`")  # noqa: E501

        self._end_date = end_date

    @property
    def effective_date(self):
        """Gets the effective_date of this ProductPart.  # noqa: E501


        :return: The effective_date of this ProductPart.  # noqa: E501
        :rtype: object
        """
        return self._effective_date

    @effective_date.setter
    def effective_date(self, effective_date):
        """Sets the effective_date of this ProductPart.


        :param effective_date: The effective_date of this ProductPart.  # noqa: E501
        :type: object
        """
        if effective_date is None:
            raise ValueError("Invalid value for `effective_date`, must not be `None`")  # noqa: E501

        self._effective_date = effective_date

    @property
    def is_closeout(self):
        """Gets the is_closeout of this ProductPart.  # noqa: E501


        :return: The is_closeout of this ProductPart.  # noqa: E501
        :rtype: object
        """
        return self._is_closeout

    @is_closeout.setter
    def is_closeout(self, is_closeout):
        """Sets the is_closeout of this ProductPart.


        :param is_closeout: The is_closeout of this ProductPart.  # noqa: E501
        :type: object
        """
        if is_closeout is None:
            raise ValueError("Invalid value for `is_closeout`, must not be `None`")  # noqa: E501

        self._is_closeout = is_closeout

    @property
    def is_caution(self):
        """Gets the is_caution of this ProductPart.  # noqa: E501


        :return: The is_caution of this ProductPart.  # noqa: E501
        :rtype: object
        """
        return self._is_caution

    @is_caution.setter
    def is_caution(self, is_caution):
        """Sets the is_caution of this ProductPart.


        :param is_caution: The is_caution of this ProductPart.  # noqa: E501
        :type: object
        """
        if is_caution is None:
            raise ValueError("Invalid value for `is_caution`, must not be `None`")  # noqa: E501

        self._is_caution = is_caution

    @property
    def caution_comment(self):
        """Gets the caution_comment of this ProductPart.  # noqa: E501


        :return: The caution_comment of this ProductPart.  # noqa: E501
        :rtype: object
        """
        return self._caution_comment

    @caution_comment.setter
    def caution_comment(self, caution_comment):
        """Sets the caution_comment of this ProductPart.


        :param caution_comment: The caution_comment of this ProductPart.  # noqa: E501
        :type: object
        """
        if caution_comment is None:
            raise ValueError("Invalid value for `caution_comment`, must not be `None`")  # noqa: E501

        self._caution_comment = caution_comment

    @property
    def nmfc_code(self):
        """Gets the nmfc_code of this ProductPart.  # noqa: E501


        :return: The nmfc_code of this ProductPart.  # noqa: E501
        :rtype: object
        """
        return self._nmfc_code

    @nmfc_code.setter
    def nmfc_code(self, nmfc_code):
        """Sets the nmfc_code of this ProductPart.


        :param nmfc_code: The nmfc_code of this ProductPart.  # noqa: E501
        :type: object
        """
        if nmfc_code is None:
            raise ValueError("Invalid value for `nmfc_code`, must not be `None`")  # noqa: E501

        self._nmfc_code = nmfc_code

    @property
    def nmfc_description(self):
        """Gets the nmfc_description of this ProductPart.  # noqa: E501


        :return: The nmfc_description of this ProductPart.  # noqa: E501
        :rtype: object
        """
        return self._nmfc_description

    @nmfc_description.setter
    def nmfc_description(self, nmfc_description):
        """Sets the nmfc_description of this ProductPart.


        :param nmfc_description: The nmfc_description of this ProductPart.  # noqa: E501
        :type: object
        """
        if nmfc_description is None:
            raise ValueError("Invalid value for `nmfc_description`, must not be `None`")  # noqa: E501

        self._nmfc_description = nmfc_description

    @property
    def nmfc_number(self):
        """Gets the nmfc_number of this ProductPart.  # noqa: E501


        :return: The nmfc_number of this ProductPart.  # noqa: E501
        :rtype: object
        """
        return self._nmfc_number

    @nmfc_number.setter
    def nmfc_number(self, nmfc_number):
        """Sets the nmfc_number of this ProductPart.


        :param nmfc_number: The nmfc_number of this ProductPart.  # noqa: E501
        :type: object
        """
        if nmfc_number is None:
            raise ValueError("Invalid value for `nmfc_number`, must not be `None`")  # noqa: E501

        self._nmfc_number = nmfc_number

    @property
    def is_on_demand(self):
        """Gets the is_on_demand of this ProductPart.  # noqa: E501


        :return: The is_on_demand of this ProductPart.  # noqa: E501
        :rtype: object
        """
        return self._is_on_demand

    @is_on_demand.setter
    def is_on_demand(self, is_on_demand):
        """Sets the is_on_demand of this ProductPart.


        :param is_on_demand: The is_on_demand of this ProductPart.  # noqa: E501
        :type: object
        """
        if is_on_demand is None:
            raise ValueError("Invalid value for `is_on_demand`, must not be `None`")  # noqa: E501

        self._is_on_demand = is_on_demand

    @property
    def is_hazmat(self):
        """Gets the is_hazmat of this ProductPart.  # noqa: E501


        :return: The is_hazmat of this ProductPart.  # noqa: E501
        :rtype: object
        """
        return self._is_hazmat

    @is_hazmat.setter
    def is_hazmat(self, is_hazmat):
        """Sets the is_hazmat of this ProductPart.


        :param is_hazmat: The is_hazmat of this ProductPart.  # noqa: E501
        :type: object
        """
        if is_hazmat is None:
            raise ValueError("Invalid value for `is_hazmat`, must not be `None`")  # noqa: E501

        self._is_hazmat = is_hazmat

    @property
    def primary_color(self):
        """Gets the primary_color of this ProductPart.  # noqa: E501


        :return: The primary_color of this ProductPart.  # noqa: E501
        :rtype: object
        """
        return self._primary_color

    @primary_color.setter
    def primary_color(self, primary_color):
        """Sets the primary_color of this ProductPart.


        :param primary_color: The primary_color of this ProductPart.  # noqa: E501
        :type: object
        """

        self._primary_color = primary_color

    @property
    def color_array(self):
        """Gets the color_array of this ProductPart.  # noqa: E501


        :return: The color_array of this ProductPart.  # noqa: E501
        :rtype: object
        """
        return self._color_array

    @color_array.setter
    def color_array(self, color_array):
        """Sets the color_array of this ProductPart.


        :param color_array: The color_array of this ProductPart.  # noqa: E501
        :type: object
        """
        if color_array is None:
            raise ValueError("Invalid value for `color_array`, must not be `None`")  # noqa: E501

        self._color_array = color_array

    @property
    def product_packaging_array(self):
        """Gets the product_packaging_array of this ProductPart.  # noqa: E501


        :return: The product_packaging_array of this ProductPart.  # noqa: E501
        :rtype: object
        """
        return self._product_packaging_array

    @product_packaging_array.setter
    def product_packaging_array(self, product_packaging_array):
        """Sets the product_packaging_array of this ProductPart.


        :param product_packaging_array: The product_packaging_array of this ProductPart.  # noqa: E501
        :type: object
        """
        if product_packaging_array is None:
            raise ValueError("Invalid value for `product_packaging_array`, must not be `None`")  # noqa: E501

        self._product_packaging_array = product_packaging_array

    @property
    def shipping_package_array(self):
        """Gets the shipping_package_array of this ProductPart.  # noqa: E501


        :return: The shipping_package_array of this ProductPart.  # noqa: E501
        :rtype: object
        """
        return self._shipping_package_array

    @shipping_package_array.setter
    def shipping_package_array(self, shipping_package_array):
        """Sets the shipping_package_array of this ProductPart.


        :param shipping_package_array: The shipping_package_array of this ProductPart.  # noqa: E501
        :type: object
        """
        if shipping_package_array is None:
            raise ValueError("Invalid value for `shipping_package_array`, must not be `None`")  # noqa: E501

        self._shipping_package_array = shipping_package_array

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
        if issubclass(ProductPart, dict):
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
        if not isinstance(other, ProductPart):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
