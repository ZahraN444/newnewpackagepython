# -*- coding: utf-8 -*-

"""
lob

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class Status1Enum(object):

    """Implementation of the 'Status1' enum.

    The status level for the country. This represents the maximum level of
    accuracy an input address can be verified to.
    * `LV4` - Verified. The input data is correct. All input data was able to
    match in databases.
    * `LV3` - Verified. The input data is correct. All input data was able to
    match in databases <em>after</em> some or all elements were standarized.
    The input data may also be using outdated city, state, or country names.
    * `LV2` - Verified. The input data is correct although some input data is
    unverifiable due to incomplete data.
    * `LV1` - Verified. The input data is acceptable but in an attempt to
    standarize user input, errors were introduced.
    * `LF4` - Fixed. The input data is matched and fixed. (Example: Brighon,
    UK -> Brighton, UK)
    * `LF3` - Fixed. The input data is matched and fixed but some elements
    such as Subbuilding number and house number cannot be checked.
    * `LF2` - Fixed. The input data is matched but some elements such as
    Street cannot be checked.
    * `LF1` - Fixed. The input data is acceptable but in an attempt to
    standarize user input, errors were introduced.
    * `LM4` - Missing Info. The input data cannot be corrected completely.
    * `LM3` - Missing Info. The input data cannot be corrected completely and
    there were multiple matches found in databases.
    * `LM2` - Missing Info. The input data cannot be corrected completely and
    only some elements were found.
    * `LU1` - Unverified. The input data cannot be corrected or matched.

    Attributes:
        LV4: TODO: type description here.
        LV3: TODO: type description here.
        LV2: TODO: type description here.
        LV1: TODO: type description here.
        LF4: TODO: type description here.
        LF3: TODO: type description here.
        LF2: TODO: type description here.
        LF1: TODO: type description here.
        LM4: TODO: type description here.
        LM3: TODO: type description here.
        LM2: TODO: type description here.
        LU1: TODO: type description here.

    """
    _all_values = ['LV4', 'LV3', 'LV2', 'LV1', 'LF4', 'LF3', 'LF2', 'LF1', 'LM4', 'LM3', 'LM2', 'LU1']
    LV4 = 'LV4'

    LV3 = 'LV3'

    LV2 = 'LV2'

    LV1 = 'LV1'

    LF4 = 'LF4'

    LF3 = 'LF3'

    LF2 = 'LF2'

    LF1 = 'LF1'

    LM4 = 'LM4'

    LM3 = 'LM3'

    LM2 = 'LM2'

    LU1 = 'LU1'

    @classmethod
    def validate(cls, value):
        """Validates value contains in enum

        Args:
            value: the value to be validated

        Returns:
            boolean : if value is valid enum values.

        """
        return value in cls._all_values
   