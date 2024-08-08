# -*- coding: utf-8 -*-

"""
lob

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from lob.api_helper import APIHelper


class From(object):

    """Implementation of the 'from' model.

    TODO: type model description here.

    Attributes:
        mfrom (object): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mfrom": 'from'
    }

    _optionals = [
        'mfrom',
    ]

    def __init__(self,
                 mfrom=APIHelper.SKIP):
        """Constructor for the From class"""

        # Initialize members of the class
        if mfrom is not APIHelper.SKIP:
            self.mfrom = mfrom 

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
        mfrom = dictionary.get("from") if dictionary.get("from") else APIHelper.SKIP
        # Return an object of this model
        return cls(mfrom)