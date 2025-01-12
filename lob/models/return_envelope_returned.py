# -*- coding: utf-8 -*-

"""
lob

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from lob.api_helper import APIHelper


class ReturnEnvelopeReturned(object):

    """Implementation of the 'return_envelope_returned' model.

    TODO: type model description here.

    Attributes:
        id (str): The unique ID of the Return Envelope.
        alias (str): A quick reference name for the Return Envelope.
        url (str): The url of the return envelope.
        object (str): Value is resource type.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "alias": 'alias',
        "url": 'url',
        "object": 'object'
    }

    _optionals = [
        'id',
        'alias',
        'url',
        'object',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 alias=APIHelper.SKIP,
                 url=APIHelper.SKIP,
                 object=APIHelper.SKIP):
        """Constructor for the ReturnEnvelopeReturned class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if alias is not APIHelper.SKIP:
            self.alias = alias 
        if url is not APIHelper.SKIP:
            self.url = url 
        if object is not APIHelper.SKIP:
            self.object = object 

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
        alias = dictionary.get("alias") if dictionary.get("alias") else APIHelper.SKIP
        url = dictionary.get("url") if dictionary.get("url") else APIHelper.SKIP
        object = dictionary.get("object") if dictionary.get("object") else APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   alias,
                   url,
                   object)
