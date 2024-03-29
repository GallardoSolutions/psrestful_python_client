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

class Invoice(object):
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
        'invoice_number': 'object',
        'invoice_type': 'object',
        'invoice_date': 'object',
        'purchase_order_number': 'object',
        'purchase_order_version': 'object',
        'bill_to': 'object',
        'sold_to': 'object',
        'invoice_comments': 'object',
        'payment_terms': 'object',
        'payment_due_date': 'object',
        'currency': 'object',
        'fob_id': 'object',
        'sales_amount': 'object',
        'shipping_amount': 'object',
        'handling_amount': 'object',
        'tax_amount': 'object',
        'invoice_amount': 'object',
        'advance_payment_amount': 'object',
        'invoice_amount_due': 'object',
        'invoice_document_url': 'object',
        'invoice_line_items_array': 'object',
        'sales_order_numbers_array': 'object',
        'tax_array': 'object',
        'invoice_payment_url': 'object'
    }

    attribute_map = {
        'invoice_number': 'invoiceNumber',
        'invoice_type': 'invoiceType',
        'invoice_date': 'invoiceDate',
        'purchase_order_number': 'purchaseOrderNumber',
        'purchase_order_version': 'purchaseOrderVersion',
        'bill_to': 'BillTo',
        'sold_to': 'SoldTo',
        'invoice_comments': 'invoiceComments',
        'payment_terms': 'paymentTerms',
        'payment_due_date': 'paymentDueDate',
        'currency': 'currency',
        'fob_id': 'fobId',
        'sales_amount': 'salesAmount',
        'shipping_amount': 'shippingAmount',
        'handling_amount': 'handlingAmount',
        'tax_amount': 'taxAmount',
        'invoice_amount': 'invoiceAmount',
        'advance_payment_amount': 'advancePaymentAmount',
        'invoice_amount_due': 'invoiceAmountDue',
        'invoice_document_url': 'invoiceDocumentUrl',
        'invoice_line_items_array': 'InvoiceLineItemsArray',
        'sales_order_numbers_array': 'SalesOrderNumbersArray',
        'tax_array': 'TaxArray',
        'invoice_payment_url': 'invoicePaymentUrl'
    }

    def __init__(self, invoice_number=None, invoice_type=None, invoice_date=None, purchase_order_number=None, purchase_order_version=None, bill_to=None, sold_to=None, invoice_comments=None, payment_terms=None, payment_due_date=None, currency=None, fob_id=None, sales_amount=None, shipping_amount=None, handling_amount=None, tax_amount=None, invoice_amount=None, advance_payment_amount=None, invoice_amount_due=None, invoice_document_url=None, invoice_line_items_array=None, sales_order_numbers_array=None, tax_array=None, invoice_payment_url=None):  # noqa: E501
        """Invoice - a model defined in Swagger"""  # noqa: E501
        self._invoice_number = None
        self._invoice_type = None
        self._invoice_date = None
        self._purchase_order_number = None
        self._purchase_order_version = None
        self._bill_to = None
        self._sold_to = None
        self._invoice_comments = None
        self._payment_terms = None
        self._payment_due_date = None
        self._currency = None
        self._fob_id = None
        self._sales_amount = None
        self._shipping_amount = None
        self._handling_amount = None
        self._tax_amount = None
        self._invoice_amount = None
        self._advance_payment_amount = None
        self._invoice_amount_due = None
        self._invoice_document_url = None
        self._invoice_line_items_array = None
        self._sales_order_numbers_array = None
        self._tax_array = None
        self._invoice_payment_url = None
        self.discriminator = None
        self.invoice_number = invoice_number
        self.invoice_type = invoice_type
        self.invoice_date = invoice_date
        self.purchase_order_number = purchase_order_number
        self.purchase_order_version = purchase_order_version
        self.bill_to = bill_to
        self.sold_to = sold_to
        self.invoice_comments = invoice_comments
        self.payment_terms = payment_terms
        self.payment_due_date = payment_due_date
        self.currency = currency
        self.fob_id = fob_id
        self.sales_amount = sales_amount
        self.shipping_amount = shipping_amount
        self.handling_amount = handling_amount
        self.tax_amount = tax_amount
        self.invoice_amount = invoice_amount
        self.advance_payment_amount = advance_payment_amount
        self.invoice_amount_due = invoice_amount_due
        self.invoice_document_url = invoice_document_url
        self.invoice_line_items_array = invoice_line_items_array
        self.sales_order_numbers_array = sales_order_numbers_array
        self.tax_array = tax_array
        self.invoice_payment_url = invoice_payment_url

    @property
    def invoice_number(self):
        """Gets the invoice_number of this Invoice.  # noqa: E501


        :return: The invoice_number of this Invoice.  # noqa: E501
        :rtype: object
        """
        return self._invoice_number

    @invoice_number.setter
    def invoice_number(self, invoice_number):
        """Sets the invoice_number of this Invoice.


        :param invoice_number: The invoice_number of this Invoice.  # noqa: E501
        :type: object
        """
        if invoice_number is None:
            raise ValueError("Invalid value for `invoice_number`, must not be `None`")  # noqa: E501

        self._invoice_number = invoice_number

    @property
    def invoice_type(self):
        """Gets the invoice_type of this Invoice.  # noqa: E501


        :return: The invoice_type of this Invoice.  # noqa: E501
        :rtype: object
        """
        return self._invoice_type

    @invoice_type.setter
    def invoice_type(self, invoice_type):
        """Sets the invoice_type of this Invoice.


        :param invoice_type: The invoice_type of this Invoice.  # noqa: E501
        :type: object
        """
        if invoice_type is None:
            raise ValueError("Invalid value for `invoice_type`, must not be `None`")  # noqa: E501

        self._invoice_type = invoice_type

    @property
    def invoice_date(self):
        """Gets the invoice_date of this Invoice.  # noqa: E501


        :return: The invoice_date of this Invoice.  # noqa: E501
        :rtype: object
        """
        return self._invoice_date

    @invoice_date.setter
    def invoice_date(self, invoice_date):
        """Sets the invoice_date of this Invoice.


        :param invoice_date: The invoice_date of this Invoice.  # noqa: E501
        :type: object
        """
        if invoice_date is None:
            raise ValueError("Invalid value for `invoice_date`, must not be `None`")  # noqa: E501

        self._invoice_date = invoice_date

    @property
    def purchase_order_number(self):
        """Gets the purchase_order_number of this Invoice.  # noqa: E501


        :return: The purchase_order_number of this Invoice.  # noqa: E501
        :rtype: object
        """
        return self._purchase_order_number

    @purchase_order_number.setter
    def purchase_order_number(self, purchase_order_number):
        """Sets the purchase_order_number of this Invoice.


        :param purchase_order_number: The purchase_order_number of this Invoice.  # noqa: E501
        :type: object
        """
        if purchase_order_number is None:
            raise ValueError("Invalid value for `purchase_order_number`, must not be `None`")  # noqa: E501

        self._purchase_order_number = purchase_order_number

    @property
    def purchase_order_version(self):
        """Gets the purchase_order_version of this Invoice.  # noqa: E501


        :return: The purchase_order_version of this Invoice.  # noqa: E501
        :rtype: object
        """
        return self._purchase_order_version

    @purchase_order_version.setter
    def purchase_order_version(self, purchase_order_version):
        """Sets the purchase_order_version of this Invoice.


        :param purchase_order_version: The purchase_order_version of this Invoice.  # noqa: E501
        :type: object
        """
        if purchase_order_version is None:
            raise ValueError("Invalid value for `purchase_order_version`, must not be `None`")  # noqa: E501

        self._purchase_order_version = purchase_order_version

    @property
    def bill_to(self):
        """Gets the bill_to of this Invoice.  # noqa: E501


        :return: The bill_to of this Invoice.  # noqa: E501
        :rtype: object
        """
        return self._bill_to

    @bill_to.setter
    def bill_to(self, bill_to):
        """Sets the bill_to of this Invoice.


        :param bill_to: The bill_to of this Invoice.  # noqa: E501
        :type: object
        """
        if bill_to is None:
            raise ValueError("Invalid value for `bill_to`, must not be `None`")  # noqa: E501

        self._bill_to = bill_to

    @property
    def sold_to(self):
        """Gets the sold_to of this Invoice.  # noqa: E501


        :return: The sold_to of this Invoice.  # noqa: E501
        :rtype: object
        """
        return self._sold_to

    @sold_to.setter
    def sold_to(self, sold_to):
        """Sets the sold_to of this Invoice.


        :param sold_to: The sold_to of this Invoice.  # noqa: E501
        :type: object
        """
        if sold_to is None:
            raise ValueError("Invalid value for `sold_to`, must not be `None`")  # noqa: E501

        self._sold_to = sold_to

    @property
    def invoice_comments(self):
        """Gets the invoice_comments of this Invoice.  # noqa: E501


        :return: The invoice_comments of this Invoice.  # noqa: E501
        :rtype: object
        """
        return self._invoice_comments

    @invoice_comments.setter
    def invoice_comments(self, invoice_comments):
        """Sets the invoice_comments of this Invoice.


        :param invoice_comments: The invoice_comments of this Invoice.  # noqa: E501
        :type: object
        """
        if invoice_comments is None:
            raise ValueError("Invalid value for `invoice_comments`, must not be `None`")  # noqa: E501

        self._invoice_comments = invoice_comments

    @property
    def payment_terms(self):
        """Gets the payment_terms of this Invoice.  # noqa: E501


        :return: The payment_terms of this Invoice.  # noqa: E501
        :rtype: object
        """
        return self._payment_terms

    @payment_terms.setter
    def payment_terms(self, payment_terms):
        """Sets the payment_terms of this Invoice.


        :param payment_terms: The payment_terms of this Invoice.  # noqa: E501
        :type: object
        """
        if payment_terms is None:
            raise ValueError("Invalid value for `payment_terms`, must not be `None`")  # noqa: E501

        self._payment_terms = payment_terms

    @property
    def payment_due_date(self):
        """Gets the payment_due_date of this Invoice.  # noqa: E501


        :return: The payment_due_date of this Invoice.  # noqa: E501
        :rtype: object
        """
        return self._payment_due_date

    @payment_due_date.setter
    def payment_due_date(self, payment_due_date):
        """Sets the payment_due_date of this Invoice.


        :param payment_due_date: The payment_due_date of this Invoice.  # noqa: E501
        :type: object
        """
        if payment_due_date is None:
            raise ValueError("Invalid value for `payment_due_date`, must not be `None`")  # noqa: E501

        self._payment_due_date = payment_due_date

    @property
    def currency(self):
        """Gets the currency of this Invoice.  # noqa: E501


        :return: The currency of this Invoice.  # noqa: E501
        :rtype: object
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this Invoice.


        :param currency: The currency of this Invoice.  # noqa: E501
        :type: object
        """
        if currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def fob_id(self):
        """Gets the fob_id of this Invoice.  # noqa: E501


        :return: The fob_id of this Invoice.  # noqa: E501
        :rtype: object
        """
        return self._fob_id

    @fob_id.setter
    def fob_id(self, fob_id):
        """Sets the fob_id of this Invoice.


        :param fob_id: The fob_id of this Invoice.  # noqa: E501
        :type: object
        """
        if fob_id is None:
            raise ValueError("Invalid value for `fob_id`, must not be `None`")  # noqa: E501

        self._fob_id = fob_id

    @property
    def sales_amount(self):
        """Gets the sales_amount of this Invoice.  # noqa: E501


        :return: The sales_amount of this Invoice.  # noqa: E501
        :rtype: object
        """
        return self._sales_amount

    @sales_amount.setter
    def sales_amount(self, sales_amount):
        """Sets the sales_amount of this Invoice.


        :param sales_amount: The sales_amount of this Invoice.  # noqa: E501
        :type: object
        """
        if sales_amount is None:
            raise ValueError("Invalid value for `sales_amount`, must not be `None`")  # noqa: E501

        self._sales_amount = sales_amount

    @property
    def shipping_amount(self):
        """Gets the shipping_amount of this Invoice.  # noqa: E501


        :return: The shipping_amount of this Invoice.  # noqa: E501
        :rtype: object
        """
        return self._shipping_amount

    @shipping_amount.setter
    def shipping_amount(self, shipping_amount):
        """Sets the shipping_amount of this Invoice.


        :param shipping_amount: The shipping_amount of this Invoice.  # noqa: E501
        :type: object
        """
        if shipping_amount is None:
            raise ValueError("Invalid value for `shipping_amount`, must not be `None`")  # noqa: E501

        self._shipping_amount = shipping_amount

    @property
    def handling_amount(self):
        """Gets the handling_amount of this Invoice.  # noqa: E501


        :return: The handling_amount of this Invoice.  # noqa: E501
        :rtype: object
        """
        return self._handling_amount

    @handling_amount.setter
    def handling_amount(self, handling_amount):
        """Sets the handling_amount of this Invoice.


        :param handling_amount: The handling_amount of this Invoice.  # noqa: E501
        :type: object
        """
        if handling_amount is None:
            raise ValueError("Invalid value for `handling_amount`, must not be `None`")  # noqa: E501

        self._handling_amount = handling_amount

    @property
    def tax_amount(self):
        """Gets the tax_amount of this Invoice.  # noqa: E501


        :return: The tax_amount of this Invoice.  # noqa: E501
        :rtype: object
        """
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, tax_amount):
        """Sets the tax_amount of this Invoice.


        :param tax_amount: The tax_amount of this Invoice.  # noqa: E501
        :type: object
        """
        if tax_amount is None:
            raise ValueError("Invalid value for `tax_amount`, must not be `None`")  # noqa: E501

        self._tax_amount = tax_amount

    @property
    def invoice_amount(self):
        """Gets the invoice_amount of this Invoice.  # noqa: E501


        :return: The invoice_amount of this Invoice.  # noqa: E501
        :rtype: object
        """
        return self._invoice_amount

    @invoice_amount.setter
    def invoice_amount(self, invoice_amount):
        """Sets the invoice_amount of this Invoice.


        :param invoice_amount: The invoice_amount of this Invoice.  # noqa: E501
        :type: object
        """
        if invoice_amount is None:
            raise ValueError("Invalid value for `invoice_amount`, must not be `None`")  # noqa: E501

        self._invoice_amount = invoice_amount

    @property
    def advance_payment_amount(self):
        """Gets the advance_payment_amount of this Invoice.  # noqa: E501


        :return: The advance_payment_amount of this Invoice.  # noqa: E501
        :rtype: object
        """
        return self._advance_payment_amount

    @advance_payment_amount.setter
    def advance_payment_amount(self, advance_payment_amount):
        """Sets the advance_payment_amount of this Invoice.


        :param advance_payment_amount: The advance_payment_amount of this Invoice.  # noqa: E501
        :type: object
        """
        if advance_payment_amount is None:
            raise ValueError("Invalid value for `advance_payment_amount`, must not be `None`")  # noqa: E501

        self._advance_payment_amount = advance_payment_amount

    @property
    def invoice_amount_due(self):
        """Gets the invoice_amount_due of this Invoice.  # noqa: E501


        :return: The invoice_amount_due of this Invoice.  # noqa: E501
        :rtype: object
        """
        return self._invoice_amount_due

    @invoice_amount_due.setter
    def invoice_amount_due(self, invoice_amount_due):
        """Sets the invoice_amount_due of this Invoice.


        :param invoice_amount_due: The invoice_amount_due of this Invoice.  # noqa: E501
        :type: object
        """
        if invoice_amount_due is None:
            raise ValueError("Invalid value for `invoice_amount_due`, must not be `None`")  # noqa: E501

        self._invoice_amount_due = invoice_amount_due

    @property
    def invoice_document_url(self):
        """Gets the invoice_document_url of this Invoice.  # noqa: E501


        :return: The invoice_document_url of this Invoice.  # noqa: E501
        :rtype: object
        """
        return self._invoice_document_url

    @invoice_document_url.setter
    def invoice_document_url(self, invoice_document_url):
        """Sets the invoice_document_url of this Invoice.


        :param invoice_document_url: The invoice_document_url of this Invoice.  # noqa: E501
        :type: object
        """
        if invoice_document_url is None:
            raise ValueError("Invalid value for `invoice_document_url`, must not be `None`")  # noqa: E501

        self._invoice_document_url = invoice_document_url

    @property
    def invoice_line_items_array(self):
        """Gets the invoice_line_items_array of this Invoice.  # noqa: E501


        :return: The invoice_line_items_array of this Invoice.  # noqa: E501
        :rtype: object
        """
        return self._invoice_line_items_array

    @invoice_line_items_array.setter
    def invoice_line_items_array(self, invoice_line_items_array):
        """Sets the invoice_line_items_array of this Invoice.


        :param invoice_line_items_array: The invoice_line_items_array of this Invoice.  # noqa: E501
        :type: object
        """
        if invoice_line_items_array is None:
            raise ValueError("Invalid value for `invoice_line_items_array`, must not be `None`")  # noqa: E501

        self._invoice_line_items_array = invoice_line_items_array

    @property
    def sales_order_numbers_array(self):
        """Gets the sales_order_numbers_array of this Invoice.  # noqa: E501


        :return: The sales_order_numbers_array of this Invoice.  # noqa: E501
        :rtype: object
        """
        return self._sales_order_numbers_array

    @sales_order_numbers_array.setter
    def sales_order_numbers_array(self, sales_order_numbers_array):
        """Sets the sales_order_numbers_array of this Invoice.


        :param sales_order_numbers_array: The sales_order_numbers_array of this Invoice.  # noqa: E501
        :type: object
        """
        if sales_order_numbers_array is None:
            raise ValueError("Invalid value for `sales_order_numbers_array`, must not be `None`")  # noqa: E501

        self._sales_order_numbers_array = sales_order_numbers_array

    @property
    def tax_array(self):
        """Gets the tax_array of this Invoice.  # noqa: E501


        :return: The tax_array of this Invoice.  # noqa: E501
        :rtype: object
        """
        return self._tax_array

    @tax_array.setter
    def tax_array(self, tax_array):
        """Sets the tax_array of this Invoice.


        :param tax_array: The tax_array of this Invoice.  # noqa: E501
        :type: object
        """
        if tax_array is None:
            raise ValueError("Invalid value for `tax_array`, must not be `None`")  # noqa: E501

        self._tax_array = tax_array

    @property
    def invoice_payment_url(self):
        """Gets the invoice_payment_url of this Invoice.  # noqa: E501


        :return: The invoice_payment_url of this Invoice.  # noqa: E501
        :rtype: object
        """
        return self._invoice_payment_url

    @invoice_payment_url.setter
    def invoice_payment_url(self, invoice_payment_url):
        """Sets the invoice_payment_url of this Invoice.


        :param invoice_payment_url: The invoice_payment_url of this Invoice.  # noqa: E501
        :type: object
        """
        if invoice_payment_url is None:
            raise ValueError("Invalid value for `invoice_payment_url`, must not be `None`")  # noqa: E501

        self._invoice_payment_url = invoice_payment_url

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
        if issubclass(Invoice, dict):
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
        if not isinstance(other, Invoice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
