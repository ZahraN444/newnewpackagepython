# -*- coding: utf-8 -*-

"""
lob

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from lob.api_helper import APIHelper
from lob.models.dpv_active_enum import DpvActiveEnum
from lob.models.dpv_cmra_enum import DpvCmraEnum
from lob.models.dpv_confirmation_enum import DpvConfirmationEnum
from lob.models.dpv_footnote_enum import DpvFootnoteEnum
from lob.models.dpv_vacant_enum import DpvVacantEnum
from lob.models.lacs_indicator_enum import LacsIndicatorEnum
from lob.models.suite_return_code_enum import SuiteReturnCodeEnum


class DeliverabilityAnalysis1(object):

    """Implementation of the 'DeliverabilityAnalysis1' model.

    TODO: type model description here.

    Attributes:
        dpv_confirmation (DpvConfirmationEnum): TODO: type description here.
        dpv_cmra (DpvCmraEnum): TODO: type description here.
        dpv_vacant (DpvVacantEnum): TODO: type description here.
        dpv_active (DpvActiveEnum): TODO: type description here.
        dpv_footnotes (List[DpvFootnoteEnum]): An array of 2-character strings
            that gives more insight into how
            `deliverability_analysis[dpv_confirmation]` was determined. Will
            always include at least 1 string, and can include up to 3. For
            details, see [US Verification
            Details](#tag/US-Verification-Types).
        ews_match (bool): Indicates whether or not an address has been flagged
            in the <a
            href="https://docs.informatica.com/data-engineering/data-engineerin
            g-quality/10-4-0/address-validator-port-reference/postal-carrier-ce
            rtification-data-ports/early-warning-system-return-code.html"
            target="_blank">Early Warning System</a>, meaning the address is
            under development and not yet ready to receive mail. However, it
            should become available in a few months.
        lacs_indicator (LacsIndicatorEnum): TODO: type description here.
        lacs_return_code (str): A code indicating how
            `deliverability_analysis[lacs_indicator]` was determined. Possible
            values are: * `A` — A new address was produced because a match was
            found in LACS<sup>Link</sup>. * `92` — A LACS<sup>Link</sup>
            record was matched after dropping secondary information. * `14` —
            A match was found in LACS<sup>Link</sup>, but could not be
            converted to a deliverable address. * `00` — A match was not found
            in LACS<sup>Link</sup>, and no new address was produced. * `''` —
            LACS<sup>Link</sup> was not attempted.
        suite_return_code (SuiteReturnCodeEnum): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "dpv_confirmation": 'dpv_confirmation',
        "dpv_cmra": 'dpv_cmra',
        "dpv_vacant": 'dpv_vacant',
        "dpv_active": 'dpv_active',
        "dpv_footnotes": 'dpv_footnotes',
        "ews_match": 'ews_match',
        "lacs_indicator": 'lacs_indicator',
        "lacs_return_code": 'lacs_return_code',
        "suite_return_code": 'suite_return_code'
    }

    def __init__(self,
                 dpv_confirmation=None,
                 dpv_cmra=None,
                 dpv_vacant=None,
                 dpv_active=None,
                 dpv_footnotes=None,
                 ews_match=None,
                 lacs_indicator=None,
                 lacs_return_code=None,
                 suite_return_code=None):
        """Constructor for the DeliverabilityAnalysis1 class"""

        # Initialize members of the class
        self.dpv_confirmation = dpv_confirmation 
        self.dpv_cmra = dpv_cmra 
        self.dpv_vacant = dpv_vacant 
        self.dpv_active = dpv_active 
        self.dpv_footnotes = dpv_footnotes 
        self.ews_match = ews_match 
        self.lacs_indicator = lacs_indicator 
        self.lacs_return_code = lacs_return_code 
        self.suite_return_code = suite_return_code 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        dpv_confirmation = dictionary.get("dpv_confirmation") if dictionary.get("dpv_confirmation") else None
        dpv_cmra = dictionary.get("dpv_cmra") if dictionary.get("dpv_cmra") else None
        dpv_vacant = dictionary.get("dpv_vacant") if dictionary.get("dpv_vacant") else None
        dpv_active = dictionary.get("dpv_active") if dictionary.get("dpv_active") else None
        dpv_footnotes = dictionary.get("dpv_footnotes") if dictionary.get("dpv_footnotes") else None
        ews_match = dictionary.get("ews_match") if "ews_match" in dictionary.keys() else None
        lacs_indicator = dictionary.get("lacs_indicator") if dictionary.get("lacs_indicator") else None
        lacs_return_code = dictionary.get("lacs_return_code") if dictionary.get("lacs_return_code") else None
        suite_return_code = dictionary.get("suite_return_code") if dictionary.get("suite_return_code") else None
        # Return an object of this model
        return cls(dpv_confirmation,
                   dpv_cmra,
                   dpv_vacant,
                   dpv_active,
                   dpv_footnotes,
                   ews_match,
                   lacs_indicator,
                   lacs_return_code,
                   suite_return_code)

    @classmethod
    def validate(cls, dictionary):
        """Validates dictionary against class required properties

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            boolean : if dictionary is valid contains required properties.

        """

        if isinstance(dictionary, cls):
            return APIHelper.is_valid_type(value=dictionary.dpv_confirmation,
                                           type_callable=lambda value: DpvConfirmationEnum.validate(value)) \
                and APIHelper.is_valid_type(value=dictionary.dpv_cmra,
                                            type_callable=lambda value: DpvCmraEnum.validate(value)) \
                and APIHelper.is_valid_type(value=dictionary.dpv_vacant,
                                            type_callable=lambda value: DpvVacantEnum.validate(value)) \
                and APIHelper.is_valid_type(value=dictionary.dpv_active,
                                            type_callable=lambda value: DpvActiveEnum.validate(value)) \
                and APIHelper.is_valid_type(value=dictionary.dpv_footnotes,
                                            type_callable=lambda value: DpvFootnoteEnum.validate(value)) \
                and APIHelper.is_valid_type(value=dictionary.ews_match,
                                            type_callable=lambda value: isinstance(value, bool)) \
                and APIHelper.is_valid_type(value=dictionary.lacs_indicator,
                                            type_callable=lambda value: LacsIndicatorEnum.validate(value)) \
                and APIHelper.is_valid_type(value=dictionary.lacs_return_code,
                                            type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.suite_return_code,
                                            type_callable=lambda value: SuiteReturnCodeEnum.validate(value))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('dpv_confirmation'),
                                       type_callable=lambda value: DpvConfirmationEnum.validate(value)) \
            and APIHelper.is_valid_type(value=dictionary.get('dpv_cmra'),
                                        type_callable=lambda value: DpvCmraEnum.validate(value)) \
            and APIHelper.is_valid_type(value=dictionary.get('dpv_vacant'),
                                        type_callable=lambda value: DpvVacantEnum.validate(value)) \
            and APIHelper.is_valid_type(value=dictionary.get('dpv_active'),
                                        type_callable=lambda value: DpvActiveEnum.validate(value)) \
            and APIHelper.is_valid_type(value=dictionary.get('dpv_footnotes'),
                                        type_callable=lambda value: DpvFootnoteEnum.validate(value)) \
            and APIHelper.is_valid_type(value=dictionary.get('ews_match'),
                                        type_callable=lambda value: isinstance(value, bool)) \
            and APIHelper.is_valid_type(value=dictionary.get('lacs_indicator'),
                                        type_callable=lambda value: LacsIndicatorEnum.validate(value)) \
            and APIHelper.is_valid_type(value=dictionary.get('lacs_return_code'),
                                        type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('suite_return_code'),
                                        type_callable=lambda value: SuiteReturnCodeEnum.validate(value))
