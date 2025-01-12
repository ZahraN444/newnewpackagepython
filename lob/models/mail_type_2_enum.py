# -*- coding: utf-8 -*-

"""
lob

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class MailType2Enum(object):

    """Implementation of the 'MailType2' enum.

    Checks must be sent `usps_first_class`

    Attributes:
        USPS_FIRST_CLASS: TODO: type description here.

    """
    _all_values = ['usps_first_class']
    USPS_FIRST_CLASS = 'usps_first_class'

    @classmethod
    def validate(cls, value):
        """Validates value contains in enum

        Args:
            value: the value to be validated

        Returns:
            boolean : if value is valid enum values.

        """
        return value in cls._all_values
   