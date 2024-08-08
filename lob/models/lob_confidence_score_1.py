# -*- coding: utf-8 -*-

"""
lob

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from lob.api_helper import APIHelper
from lob.models.level_enum import LevelEnum


class LobConfidenceScore1(object):

    """Implementation of the 'LobConfidenceScore1' model.

    TODO: type model description here.

    Attributes:
        score (float): A numerical score between 0 and 100 that represents the
            percentage of mailpieces Lob has sent to this addresses that have
            been delivered successfully over the past 2 years. Will be `null`
            if no tracking data exists for this address.
        level (LevelEnum): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "score": 'score',
        "level": 'level'
    }

    _nullables = [
        'score',
    ]

    def __init__(self,
                 score=None,
                 level=None):
        """Constructor for the LobConfidenceScore1 class"""

        # Initialize members of the class
        self.score = score 
        self.level = level 

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
        score = dictionary.get("score") if dictionary.get("score") else None
        level = dictionary.get("level") if dictionary.get("level") else None
        # Return an object of this model
        return cls(score,
                   level)

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
            return APIHelper.is_valid_type(value=dictionary.score,
                                           type_callable=lambda value: isinstance(value, float),
                                           is_value_nullable=True) \
                and APIHelper.is_valid_type(value=dictionary.level,
                                            type_callable=lambda value: LevelEnum.validate(value))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('score'),
                                       type_callable=lambda value: isinstance(value, float),
                                       is_value_nullable=True) \
            and APIHelper.is_valid_type(value=dictionary.get('level'),
                                        type_callable=lambda value: LevelEnum.validate(value))