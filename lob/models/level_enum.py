# -*- coding: utf-8 -*-

"""
lob

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class LevelEnum(object):

    """Implementation of the 'Level' enum.

    Indicates the likelihood that the address is a valid, mail-receiving
    address. Possible values are:
      - `high` — Over 70% of mailpieces Lob has sent to this address were
      delivered successfully and recent mailings were also successful.
      - `medium` — Between 40% and 70% of mailpieces Lob has sent to this
      address were delivered successfully.
      - `low` — Less than 40% of mailpieces Lob has sent to this address were
      delivered successfully and recent mailings weren't successful.
      - `""` — No tracking data exists for this address or lob deliverability
      was unable to find a corresponding level of mail success.

    Attributes:
        HIGH: TODO: type description here.
        MEDIUM: TODO: type description here.
        LOW: TODO: type description here.

    """
    _all_values = ['high', 'medium', 'low']
    HIGH = 'high'

    MEDIUM = 'medium'

    LOW = 'low'

    @classmethod
    def validate(cls, value):
        """Validates value contains in enum

        Args:
            value: the value to be validated

        Returns:
            boolean : if value is valid enum values.

        """
        return value in cls._all_values
   