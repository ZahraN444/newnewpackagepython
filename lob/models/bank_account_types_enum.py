# -*- coding: utf-8 -*-

"""
lob

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class BankAccountTypesEnum(object):

    """Implementation of the 'bank_account_types' enum.

    Unique identifier referring to status of bank account

    Attributes:
        ENUM_BANK_ACCOUNTCREATED: TODO: type description here.
        ENUM_BANK_ACCOUNTDELETED: TODO: type description here.
        ENUM_BANK_ACCOUNTVERIFIED: TODO: type description here.

    """
    _all_values = ['bank_account.created', 'bank_account.deleted', 'bank_account.verified']
    ENUM_BANK_ACCOUNTCREATED = 'bank_account.created'

    ENUM_BANK_ACCOUNTDELETED = 'bank_account.deleted'

    ENUM_BANK_ACCOUNTVERIFIED = 'bank_account.verified'

    @classmethod
    def validate(cls, value):
        """Validates value contains in enum

        Args:
            value: the value to be validated

        Returns:
            boolean : if value is valid enum values.

        """
        return value in cls._all_values
   