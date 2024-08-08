# -*- coding: utf-8 -*-

"""
lob

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class UploadFile(object):

    """Implementation of the 'upload_file' model.

    TODO: type model description here.

    Attributes:
        message (str): TODO: type description here.
        filename (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "message": 'message',
        "filename": 'filename'
    }

    def __init__(self,
                 filename=None):
        """Constructor for the UploadFile class"""

        # Initialize members of the class
        self.message = 'File uploaded successfully' 
        self.filename = filename 

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
        filename = dictionary.get("filename") if dictionary.get("filename") else None
        # Return an object of this model
        return cls(filename)
