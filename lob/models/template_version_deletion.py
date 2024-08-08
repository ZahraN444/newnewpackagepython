# -*- coding: utf-8 -*-

"""
lob

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from lob.api_helper import APIHelper


class TemplateVersionDeletion(object):

    """Implementation of the 'template_version_deletion' model.

    Lob uses RESTful HTTP response codes to indicate success or failure of an
    API request. In general, 2xx indicates success, 4xx indicate an input
    error, and 5xx indicates an error on Lob's end.

    Attributes:
        id (str): Unique identifier prefixed with `vrsn_`.
        deleted (bool): Only returned if the resource has been successfully
            deleted.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "deleted": 'deleted'
    }

    _optionals = [
        'id',
        'deleted',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 deleted=APIHelper.SKIP):
        """Constructor for the TemplateVersionDeletion class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if deleted is not APIHelper.SKIP:
            self.deleted = deleted 

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
        deleted = dictionary.get("deleted") if "deleted" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   deleted)
