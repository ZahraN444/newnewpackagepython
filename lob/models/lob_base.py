# -*- coding: utf-8 -*-

"""
lob

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from lob.api_helper import APIHelper


class LobBase(object):

    """Implementation of the 'lob_base' model.

    TODO: type model description here.

    Attributes:
        date_created (datetime): A timestamp in ISO 8601 format of the date
            the resource was created.
        date_modified (datetime): A timestamp in ISO 8601 format of the date
            the resource was last modified.
        deleted (bool): Only returned if the resource has been successfully
            deleted.
        object (str): Value is resource type.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "date_created": 'date_created',
        "date_modified": 'date_modified',
        "object": 'object',
        "deleted": 'deleted'
    }

    _optionals = [
        'deleted',
    ]

    def __init__(self,
                 date_created=None,
                 date_modified=None,
                 object=None,
                 deleted=APIHelper.SKIP):
        """Constructor for the LobBase class"""

        # Initialize members of the class
        self.date_created = APIHelper.apply_datetime_converter(date_created, APIHelper.RFC3339DateTime) if date_created else None 
        self.date_modified = APIHelper.apply_datetime_converter(date_modified, APIHelper.RFC3339DateTime) if date_modified else None 
        if deleted is not APIHelper.SKIP:
            self.deleted = deleted 
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
        date_created = APIHelper.RFC3339DateTime.from_value(dictionary.get("date_created")).datetime if dictionary.get("date_created") else None
        date_modified = APIHelper.RFC3339DateTime.from_value(dictionary.get("date_modified")).datetime if dictionary.get("date_modified") else None
        object = dictionary.get("object") if dictionary.get("object") else None
        deleted = dictionary.get("deleted") if "deleted" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(date_created,
                   date_modified,
                   object,
                   deleted)
