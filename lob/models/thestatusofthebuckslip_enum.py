# -*- coding: utf-8 -*-

"""
lob

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class ThestatusofthebuckslipEnum(object):

    """Implementation of the 'Thestatusofthebuckslip.' enum.

    TODO: type enum description here.

    Attributes:
        PROCESSED: TODO: type description here.
        RENDERED: TODO: type description here.
        FAILED: TODO: type description here.

    """
    _all_values = ['processed', 'rendered', 'failed']
    PROCESSED = 'processed'

    RENDERED = 'rendered'

    FAILED = 'failed'

    @classmethod
    def validate(cls, value):
        """Validates value contains in enum

        Args:
            value: the value to be validated

        Returns:
            boolean : if value is valid enum values.

        """
        return value in cls._all_values
   