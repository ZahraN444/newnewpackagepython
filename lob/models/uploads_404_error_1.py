# -*- coding: utf-8 -*-

"""
lob

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from lob.api_helper import APIHelper
from lob.models.error_1 import Error1


class Uploads404Error1(object):

    """Implementation of the 'Uploads404Error1' model.

    TODO: type model description here.

    Attributes:
        error (Error1): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "error": 'error'
    }

    def __init__(self,
                 error=None):
        """Constructor for the Uploads404Error1 class"""

        # Initialize members of the class
        self.error = error 

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
        error = Error1.from_dictionary(dictionary.get('error')) if dictionary.get('error') else None
        # Return an object of this model
        return cls(error)

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
            return APIHelper.is_valid_type(value=dictionary.error,
                                           type_callable=lambda value: Error1.validate(value),
                                           is_model_dict=True)

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('error'),
                                       type_callable=lambda value: Error1.validate(value),
                                       is_model_dict=True)
