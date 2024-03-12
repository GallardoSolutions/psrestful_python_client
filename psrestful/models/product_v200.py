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

class ProductV200(object):
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
        'product_id': 'object',
        'product_name': 'object',
        'description': 'object',
        'price_expires_date': 'object',
        'product_brand': 'object',
        'export': 'object',
        'last_change_date': 'object',
        'creation_date': 'object',
        'end_date': 'object',
        'effective_date': 'object',
        'is_caution': 'object',
        'caution_comment': 'object',
        'is_closeout': 'object',
        'line_name': 'object',
        'primary_image_url': 'object',
        'compliance_info_available': 'object',
        'unspsc_commodity_code': 'object',
        'imprint_size': 'object',
        'default_set_up_charge': 'object',
        'default_run_charge': 'object',
        'product_category_array': 'object',
        'related_product_array': 'object',
        'product_part_array': 'ProductPartArray',
        'product_keyword_array': 'object',
        'location_decoration_array': 'object',
        'product_price_group_array': 'object',
        'fob_point_array': 'object',
        'product_marketing_point_array': 'object'
    }

    attribute_map = {
        'product_id': 'productId',
        'product_name': 'productName',
        'description': 'description',
        'price_expires_date': 'priceExpiresDate',
        'product_brand': 'productBrand',
        'export': 'export',
        'last_change_date': 'lastChangeDate',
        'creation_date': 'creationDate',
        'end_date': 'endDate',
        'effective_date': 'effectiveDate',
        'is_caution': 'isCaution',
        'caution_comment': 'cautionComment',
        'is_closeout': 'isCloseout',
        'line_name': 'lineName',
        'primary_image_url': 'primaryImageURL',
        'compliance_info_available': 'complianceInfoAvailable',
        'unspsc_commodity_code': 'unspscCommodityCode',
        'imprint_size': 'imprintSize',
        'default_set_up_charge': 'defaultSetUpCharge',
        'default_run_charge': 'defaultRunCharge',
        'product_category_array': 'ProductCategoryArray',
        'related_product_array': 'RelatedProductArray',
        'product_part_array': 'ProductPartArray',
        'product_keyword_array': 'ProductKeywordArray',
        'location_decoration_array': 'LocationDecorationArray',
        'product_price_group_array': 'ProductPriceGroupArray',
        'fob_point_array': 'FobPointArray',
        'product_marketing_point_array': 'ProductMarketingPointArray'
    }

    def __init__(self, product_id=None, product_name=None, description=None, price_expires_date=None, product_brand=None, export=None, last_change_date=None, creation_date=None, end_date=None, effective_date=None, is_caution=None, caution_comment=None, is_closeout=None, line_name=None, primary_image_url=None, compliance_info_available=None, unspsc_commodity_code=None, imprint_size=None, default_set_up_charge=None, default_run_charge=None, product_category_array=None, related_product_array=None, product_part_array=None, product_keyword_array=None, location_decoration_array=None, product_price_group_array=None, fob_point_array=None, product_marketing_point_array=None):  # noqa: E501
        """ProductV200 - a model defined in Swagger"""  # noqa: E501
        self._product_id = None
        self._product_name = None
        self._description = None
        self._price_expires_date = None
        self._product_brand = None
        self._export = None
        self._last_change_date = None
        self._creation_date = None
        self._end_date = None
        self._effective_date = None
        self._is_caution = None
        self._caution_comment = None
        self._is_closeout = None
        self._line_name = None
        self._primary_image_url = None
        self._compliance_info_available = None
        self._unspsc_commodity_code = None
        self._imprint_size = None
        self._default_set_up_charge = None
        self._default_run_charge = None
        self._product_category_array = None
        self._related_product_array = None
        self._product_part_array = None
        self._product_keyword_array = None
        self._location_decoration_array = None
        self._product_price_group_array = None
        self._fob_point_array = None
        self._product_marketing_point_array = None
        self.discriminator = None
        self.product_id = product_id
        self.product_name = product_name
        if description is not None:
            self.description = description
        if price_expires_date is not None:
            self.price_expires_date = price_expires_date
        if product_brand is not None:
            self.product_brand = product_brand
        if export is not None:
            self.export = export
        if last_change_date is not None:
            self.last_change_date = last_change_date
        if creation_date is not None:
            self.creation_date = creation_date
        if end_date is not None:
            self.end_date = end_date
        if effective_date is not None:
            self.effective_date = effective_date
        if is_caution is not None:
            self.is_caution = is_caution
        if caution_comment is not None:
            self.caution_comment = caution_comment
        if is_closeout is not None:
            self.is_closeout = is_closeout
        if line_name is not None:
            self.line_name = line_name
        if primary_image_url is not None:
            self.primary_image_url = primary_image_url
        if compliance_info_available is not None:
            self.compliance_info_available = compliance_info_available
        if unspsc_commodity_code is not None:
            self.unspsc_commodity_code = unspsc_commodity_code
        if imprint_size is not None:
            self.imprint_size = imprint_size
        if default_set_up_charge is not None:
            self.default_set_up_charge = default_set_up_charge
        if default_run_charge is not None:
            self.default_run_charge = default_run_charge
        self.product_category_array = product_category_array
        self.related_product_array = related_product_array
        self.product_part_array = product_part_array
        self.product_keyword_array = product_keyword_array
        self.location_decoration_array = location_decoration_array
        self.product_price_group_array = product_price_group_array
        self.fob_point_array = fob_point_array
        self.product_marketing_point_array = product_marketing_point_array

    @property
    def product_id(self):
        """Gets the product_id of this ProductV200.  # noqa: E501


        :return: The product_id of this ProductV200.  # noqa: E501
        :rtype: object
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this ProductV200.


        :param product_id: The product_id of this ProductV200.  # noqa: E501
        :type: object
        """
        if product_id is None:
            raise ValueError("Invalid value for `product_id`, must not be `None`")  # noqa: E501

        self._product_id = product_id

    @property
    def product_name(self):
        """Gets the product_name of this ProductV200.  # noqa: E501


        :return: The product_name of this ProductV200.  # noqa: E501
        :rtype: object
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """Sets the product_name of this ProductV200.


        :param product_name: The product_name of this ProductV200.  # noqa: E501
        :type: object
        """
        if product_name is None:
            raise ValueError("Invalid value for `product_name`, must not be `None`")  # noqa: E501

        self._product_name = product_name

    @property
    def description(self):
        """Gets the description of this ProductV200.  # noqa: E501


        :return: The description of this ProductV200.  # noqa: E501
        :rtype: object
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ProductV200.


        :param description: The description of this ProductV200.  # noqa: E501
        :type: object
        """

        self._description = description

    @property
    def price_expires_date(self):
        """Gets the price_expires_date of this ProductV200.  # noqa: E501


        :return: The price_expires_date of this ProductV200.  # noqa: E501
        :rtype: object
        """
        return self._price_expires_date

    @price_expires_date.setter
    def price_expires_date(self, price_expires_date):
        """Sets the price_expires_date of this ProductV200.


        :param price_expires_date: The price_expires_date of this ProductV200.  # noqa: E501
        :type: object
        """

        self._price_expires_date = price_expires_date

    @property
    def product_brand(self):
        """Gets the product_brand of this ProductV200.  # noqa: E501


        :return: The product_brand of this ProductV200.  # noqa: E501
        :rtype: object
        """
        return self._product_brand

    @product_brand.setter
    def product_brand(self, product_brand):
        """Sets the product_brand of this ProductV200.


        :param product_brand: The product_brand of this ProductV200.  # noqa: E501
        :type: object
        """

        self._product_brand = product_brand

    @property
    def export(self):
        """Gets the export of this ProductV200.  # noqa: E501


        :return: The export of this ProductV200.  # noqa: E501
        :rtype: object
        """
        return self._export

    @export.setter
    def export(self, export):
        """Sets the export of this ProductV200.


        :param export: The export of this ProductV200.  # noqa: E501
        :type: object
        """

        self._export = export

    @property
    def last_change_date(self):
        """Gets the last_change_date of this ProductV200.  # noqa: E501


        :return: The last_change_date of this ProductV200.  # noqa: E501
        :rtype: object
        """
        return self._last_change_date

    @last_change_date.setter
    def last_change_date(self, last_change_date):
        """Sets the last_change_date of this ProductV200.


        :param last_change_date: The last_change_date of this ProductV200.  # noqa: E501
        :type: object
        """

        self._last_change_date = last_change_date

    @property
    def creation_date(self):
        """Gets the creation_date of this ProductV200.  # noqa: E501


        :return: The creation_date of this ProductV200.  # noqa: E501
        :rtype: object
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this ProductV200.


        :param creation_date: The creation_date of this ProductV200.  # noqa: E501
        :type: object
        """

        self._creation_date = creation_date

    @property
    def end_date(self):
        """Gets the end_date of this ProductV200.  # noqa: E501


        :return: The end_date of this ProductV200.  # noqa: E501
        :rtype: object
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this ProductV200.


        :param end_date: The end_date of this ProductV200.  # noqa: E501
        :type: object
        """

        self._end_date = end_date

    @property
    def effective_date(self):
        """Gets the effective_date of this ProductV200.  # noqa: E501


        :return: The effective_date of this ProductV200.  # noqa: E501
        :rtype: object
        """
        return self._effective_date

    @effective_date.setter
    def effective_date(self, effective_date):
        """Sets the effective_date of this ProductV200.


        :param effective_date: The effective_date of this ProductV200.  # noqa: E501
        :type: object
        """

        self._effective_date = effective_date

    @property
    def is_caution(self):
        """Gets the is_caution of this ProductV200.  # noqa: E501


        :return: The is_caution of this ProductV200.  # noqa: E501
        :rtype: object
        """
        return self._is_caution

    @is_caution.setter
    def is_caution(self, is_caution):
        """Sets the is_caution of this ProductV200.


        :param is_caution: The is_caution of this ProductV200.  # noqa: E501
        :type: object
        """

        self._is_caution = is_caution

    @property
    def caution_comment(self):
        """Gets the caution_comment of this ProductV200.  # noqa: E501


        :return: The caution_comment of this ProductV200.  # noqa: E501
        :rtype: object
        """
        return self._caution_comment

    @caution_comment.setter
    def caution_comment(self, caution_comment):
        """Sets the caution_comment of this ProductV200.


        :param caution_comment: The caution_comment of this ProductV200.  # noqa: E501
        :type: object
        """

        self._caution_comment = caution_comment

    @property
    def is_closeout(self):
        """Gets the is_closeout of this ProductV200.  # noqa: E501


        :return: The is_closeout of this ProductV200.  # noqa: E501
        :rtype: object
        """
        return self._is_closeout

    @is_closeout.setter
    def is_closeout(self, is_closeout):
        """Sets the is_closeout of this ProductV200.


        :param is_closeout: The is_closeout of this ProductV200.  # noqa: E501
        :type: object
        """

        self._is_closeout = is_closeout

    @property
    def line_name(self):
        """Gets the line_name of this ProductV200.  # noqa: E501


        :return: The line_name of this ProductV200.  # noqa: E501
        :rtype: object
        """
        return self._line_name

    @line_name.setter
    def line_name(self, line_name):
        """Sets the line_name of this ProductV200.


        :param line_name: The line_name of this ProductV200.  # noqa: E501
        :type: object
        """

        self._line_name = line_name

    @property
    def primary_image_url(self):
        """Gets the primary_image_url of this ProductV200.  # noqa: E501


        :return: The primary_image_url of this ProductV200.  # noqa: E501
        :rtype: object
        """
        return self._primary_image_url

    @primary_image_url.setter
    def primary_image_url(self, primary_image_url):
        """Sets the primary_image_url of this ProductV200.


        :param primary_image_url: The primary_image_url of this ProductV200.  # noqa: E501
        :type: object
        """

        self._primary_image_url = primary_image_url

    @property
    def compliance_info_available(self):
        """Gets the compliance_info_available of this ProductV200.  # noqa: E501


        :return: The compliance_info_available of this ProductV200.  # noqa: E501
        :rtype: object
        """
        return self._compliance_info_available

    @compliance_info_available.setter
    def compliance_info_available(self, compliance_info_available):
        """Sets the compliance_info_available of this ProductV200.


        :param compliance_info_available: The compliance_info_available of this ProductV200.  # noqa: E501
        :type: object
        """

        self._compliance_info_available = compliance_info_available

    @property
    def unspsc_commodity_code(self):
        """Gets the unspsc_commodity_code of this ProductV200.  # noqa: E501


        :return: The unspsc_commodity_code of this ProductV200.  # noqa: E501
        :rtype: object
        """
        return self._unspsc_commodity_code

    @unspsc_commodity_code.setter
    def unspsc_commodity_code(self, unspsc_commodity_code):
        """Sets the unspsc_commodity_code of this ProductV200.


        :param unspsc_commodity_code: The unspsc_commodity_code of this ProductV200.  # noqa: E501
        :type: object
        """

        self._unspsc_commodity_code = unspsc_commodity_code

    @property
    def imprint_size(self):
        """Gets the imprint_size of this ProductV200.  # noqa: E501


        :return: The imprint_size of this ProductV200.  # noqa: E501
        :rtype: object
        """
        return self._imprint_size

    @imprint_size.setter
    def imprint_size(self, imprint_size):
        """Sets the imprint_size of this ProductV200.


        :param imprint_size: The imprint_size of this ProductV200.  # noqa: E501
        :type: object
        """

        self._imprint_size = imprint_size

    @property
    def default_set_up_charge(self):
        """Gets the default_set_up_charge of this ProductV200.  # noqa: E501


        :return: The default_set_up_charge of this ProductV200.  # noqa: E501
        :rtype: object
        """
        return self._default_set_up_charge

    @default_set_up_charge.setter
    def default_set_up_charge(self, default_set_up_charge):
        """Sets the default_set_up_charge of this ProductV200.


        :param default_set_up_charge: The default_set_up_charge of this ProductV200.  # noqa: E501
        :type: object
        """

        self._default_set_up_charge = default_set_up_charge

    @property
    def default_run_charge(self):
        """Gets the default_run_charge of this ProductV200.  # noqa: E501


        :return: The default_run_charge of this ProductV200.  # noqa: E501
        :rtype: object
        """
        return self._default_run_charge

    @default_run_charge.setter
    def default_run_charge(self, default_run_charge):
        """Sets the default_run_charge of this ProductV200.


        :param default_run_charge: The default_run_charge of this ProductV200.  # noqa: E501
        :type: object
        """

        self._default_run_charge = default_run_charge

    @property
    def product_category_array(self):
        """Gets the product_category_array of this ProductV200.  # noqa: E501


        :return: The product_category_array of this ProductV200.  # noqa: E501
        :rtype: object
        """
        return self._product_category_array

    @product_category_array.setter
    def product_category_array(self, product_category_array):
        """Sets the product_category_array of this ProductV200.


        :param product_category_array: The product_category_array of this ProductV200.  # noqa: E501
        :type: object
        """
        if product_category_array is None:
            raise ValueError("Invalid value for `product_category_array`, must not be `None`")  # noqa: E501

        self._product_category_array = product_category_array

    @property
    def related_product_array(self):
        """Gets the related_product_array of this ProductV200.  # noqa: E501


        :return: The related_product_array of this ProductV200.  # noqa: E501
        :rtype: object
        """
        return self._related_product_array

    @related_product_array.setter
    def related_product_array(self, related_product_array):
        """Sets the related_product_array of this ProductV200.


        :param related_product_array: The related_product_array of this ProductV200.  # noqa: E501
        :type: object
        """
        if related_product_array is None:
            raise ValueError("Invalid value for `related_product_array`, must not be `None`")  # noqa: E501

        self._related_product_array = related_product_array

    @property
    def product_part_array(self):
        """Gets the product_part_array of this ProductV200.  # noqa: E501


        :return: The product_part_array of this ProductV200.  # noqa: E501
        :rtype: ProductPartArray
        """
        return self._product_part_array

    @product_part_array.setter
    def product_part_array(self, product_part_array):
        """Sets the product_part_array of this ProductV200.


        :param product_part_array: The product_part_array of this ProductV200.  # noqa: E501
        :type: ProductPartArray
        """
        if product_part_array is None:
            raise ValueError("Invalid value for `product_part_array`, must not be `None`")  # noqa: E501

        self._product_part_array = product_part_array

    @property
    def product_keyword_array(self):
        """Gets the product_keyword_array of this ProductV200.  # noqa: E501


        :return: The product_keyword_array of this ProductV200.  # noqa: E501
        :rtype: object
        """
        return self._product_keyword_array

    @product_keyword_array.setter
    def product_keyword_array(self, product_keyword_array):
        """Sets the product_keyword_array of this ProductV200.


        :param product_keyword_array: The product_keyword_array of this ProductV200.  # noqa: E501
        :type: object
        """
        if product_keyword_array is None:
            raise ValueError("Invalid value for `product_keyword_array`, must not be `None`")  # noqa: E501

        self._product_keyword_array = product_keyword_array

    @property
    def location_decoration_array(self):
        """Gets the location_decoration_array of this ProductV200.  # noqa: E501


        :return: The location_decoration_array of this ProductV200.  # noqa: E501
        :rtype: object
        """
        return self._location_decoration_array

    @location_decoration_array.setter
    def location_decoration_array(self, location_decoration_array):
        """Sets the location_decoration_array of this ProductV200.


        :param location_decoration_array: The location_decoration_array of this ProductV200.  # noqa: E501
        :type: object
        """
        if location_decoration_array is None:
            raise ValueError("Invalid value for `location_decoration_array`, must not be `None`")  # noqa: E501

        self._location_decoration_array = location_decoration_array

    @property
    def product_price_group_array(self):
        """Gets the product_price_group_array of this ProductV200.  # noqa: E501


        :return: The product_price_group_array of this ProductV200.  # noqa: E501
        :rtype: object
        """
        return self._product_price_group_array

    @product_price_group_array.setter
    def product_price_group_array(self, product_price_group_array):
        """Sets the product_price_group_array of this ProductV200.


        :param product_price_group_array: The product_price_group_array of this ProductV200.  # noqa: E501
        :type: object
        """
        if product_price_group_array is None:
            raise ValueError("Invalid value for `product_price_group_array`, must not be `None`")  # noqa: E501

        self._product_price_group_array = product_price_group_array

    @property
    def fob_point_array(self):
        """Gets the fob_point_array of this ProductV200.  # noqa: E501


        :return: The fob_point_array of this ProductV200.  # noqa: E501
        :rtype: object
        """
        return self._fob_point_array

    @fob_point_array.setter
    def fob_point_array(self, fob_point_array):
        """Sets the fob_point_array of this ProductV200.


        :param fob_point_array: The fob_point_array of this ProductV200.  # noqa: E501
        :type: object
        """
        if fob_point_array is None:
            raise ValueError("Invalid value for `fob_point_array`, must not be `None`")  # noqa: E501

        self._fob_point_array = fob_point_array

    @property
    def product_marketing_point_array(self):
        """Gets the product_marketing_point_array of this ProductV200.  # noqa: E501


        :return: The product_marketing_point_array of this ProductV200.  # noqa: E501
        :rtype: object
        """
        return self._product_marketing_point_array

    @product_marketing_point_array.setter
    def product_marketing_point_array(self, product_marketing_point_array):
        """Sets the product_marketing_point_array of this ProductV200.


        :param product_marketing_point_array: The product_marketing_point_array of this ProductV200.  # noqa: E501
        :type: object
        """
        if product_marketing_point_array is None:
            raise ValueError("Invalid value for `product_marketing_point_array`, must not be `None`")  # noqa: E501

        self._product_marketing_point_array = product_marketing_point_array

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
        if issubclass(ProductV200, dict):
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
        if not isinstance(other, ProductV200):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other