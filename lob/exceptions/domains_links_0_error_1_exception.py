# -*- coding: utf-8 -*-

"""
lob

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from lob.api_helper import APIHelper
import lob.exceptions.api_exception
from lob.models.error_1 import Error1


class DomainsLinks0Error1Exception(lob.exceptions.api_exception.APIException):
    def __init__(self, reason, response):
        """Constructor for the DomainsLinks0Error1Exception class

        Args:
            reason (string): The reason (or error message) for the Exception
                to be raised.
            response (HttpResponse): The HttpResponse of the API call.

        """
        super(DomainsLinks0Error1Exception, self).__init__(reason, response)
        dictionary = APIHelper.json_deserialize(self.response.text)
        if isinstance(dictionary, dict):
            self.unbox(dictionary)

    def unbox(self, dictionary):
        """Populates the properties of this object by extracting them from a dictionary.

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        """
        self.error = Error1.from_dictionary(dictionary.get('error')) if dictionary.get('error') else None
