# -*- coding: utf-8 -*-

"""
lob

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class Deliverability1Enum(object):

    """Implementation of the 'Deliverability1' enum.

    Summarizes the deliverability of the `intl_verification` object. Possible
    values are:
    * `deliverable` — The address is deliverable.
    * `deliverable_missing_info` — The address is missing some information,
    but is most likely deliverable.
    * `undeliverable` — The address is most likely not deliverable. Some
    components of the address (such as city or postal code) may have been
    found.
    * `no_match` — This address is not deliverable. No matching street could
    be found within the city or postal code.

    Attributes:
        DELIVERABLE: TODO: type description here.
        DELIVERABLE_MISSING_INFO: TODO: type description here.
        UNDELIVERABLE: TODO: type description here.
        NO_MATCH: TODO: type description here.

    """
    _all_values = ['deliverable', 'deliverable_missing_info', 'undeliverable', 'no_match']
    DELIVERABLE = 'deliverable'

    DELIVERABLE_MISSING_INFO = 'deliverable_missing_info'

    UNDELIVERABLE = 'undeliverable'

    NO_MATCH = 'no_match'

    @classmethod
    def validate(cls, value):
        """Validates value contains in enum

        Args:
            value: the value to be validated

        Returns:
            boolean : if value is valid enum values.

        """
        return value in cls._all_values
   