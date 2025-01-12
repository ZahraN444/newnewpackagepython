# -*- coding: utf-8 -*-

"""
lob

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from lob.api_helper import APIHelper
from lob.models.intl_suggestions import IntlSuggestions


class IntlAutocompletions(object):

    """Implementation of the 'intl_autocompletions' model.

    TODO: type model description here.

    Attributes:
        id (str): Unique identifier prefixed with `intl_auto_`.
        suggestions (List[IntlSuggestions]): An array of objects representing
            suggested addresses.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "suggestions": 'suggestions'
    }

    _optionals = [
        'id',
        'suggestions',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 suggestions=APIHelper.SKIP):
        """Constructor for the IntlAutocompletions class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if suggestions is not APIHelper.SKIP:
            self.suggestions = suggestions 

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
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        suggestions = None
        if dictionary.get('suggestions') is not None:
            suggestions = [IntlSuggestions.from_dictionary(x) for x in dictionary.get('suggestions')]
        else:
            suggestions = APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   suggestions)
