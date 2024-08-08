# -*- coding: utf-8 -*-

"""
lob

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class Zip5(object):

    """Implementation of the 'zip5' model.

    TODO: type model description here.

    Attributes:
        zip_code (str): A 5-digit ZIP code.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "zip_code": 'zip_code'
    }

    def __init__(self,
                 zip_code=None):
        """Constructor for the Zip5 class"""

        # Initialize members of the class
        self.zip_code = zip_code 

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
        zip_code = dictionary.get("zip_code") if dictionary.get("zip_code") else None
        # Return an object of this model
        return cls(zip_code)