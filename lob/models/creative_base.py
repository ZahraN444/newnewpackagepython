# -*- coding: utf-8 -*-

"""
lob

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from lob.api_helper import APIHelper


class CreativeBase(object):

    """Implementation of the 'creative_base' model.

    TODO: type model description here.

    Attributes:
        mfrom (object): TODO: type description here.
        description (str): An internal description that identifies this
            resource. Must be no longer than 255 characters.
        metadata (Dict[str, str]): Use metadata to store custom information
            for tagging and labeling back to your internal systems. Must be an
            object with up to 20 key-value pairs. Keys must be at most 40
            characters and values must be at most 500 characters. Neither can
            contain the characters `"` and `\`. i.e. '{"customer_id" :
            "NEWYORK2015"}' Nested objects are not supported.  See
            [Metadata](#section/Metadata) for more information.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mfrom": 'from',
        "description": 'description',
        "metadata": 'metadata'
    }

    _optionals = [
        'mfrom',
        'description',
        'metadata',
    ]

    _nullables = [
        'description',
    ]

    def __init__(self,
                 mfrom=APIHelper.SKIP,
                 description=APIHelper.SKIP,
                 metadata=APIHelper.SKIP):
        """Constructor for the CreativeBase class"""

        # Initialize members of the class
        if mfrom is not APIHelper.SKIP:
            self.mfrom = mfrom 
        if description is not APIHelper.SKIP:
            self.description = description 
        if metadata is not APIHelper.SKIP:
            self.metadata = metadata 

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
        description = dictionary.get("description") if "description" in dictionary.keys() else APIHelper.SKIP
        metadata = dictionary.get("metadata") if dictionary.get("metadata") else APIHelper.SKIP
        # Return an object of this model
        return cls(mfrom,
                   description,
                   metadata)
