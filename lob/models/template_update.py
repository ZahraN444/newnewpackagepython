# -*- coding: utf-8 -*-

"""
lob

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from lob.api_helper import APIHelper


class TemplateUpdate(object):

    """Implementation of the 'template_update' model.

    TODO: type model description here.

    Attributes:
        description (str): An internal description that identifies this
            resource. Must be no longer than 255 characters.
        published_version (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "description": 'description',
        "published_version": 'published_version'
    }

    _optionals = [
        'description',
        'published_version',
    ]

    _nullables = [
        'description',
    ]

    def __init__(self,
                 description=APIHelper.SKIP,
                 published_version=APIHelper.SKIP):
        """Constructor for the TemplateUpdate class"""

        # Initialize members of the class
        if description is not APIHelper.SKIP:
            self.description = description 
        if published_version is not APIHelper.SKIP:
            self.published_version = published_version 

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
        description = dictionary.get("description") if "description" in dictionary.keys() else APIHelper.SKIP
        published_version = dictionary.get("published_version") if dictionary.get("published_version") else APIHelper.SKIP
        # Return an object of this model
        return cls(description,
                   published_version)