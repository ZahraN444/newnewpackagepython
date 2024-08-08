# -*- coding: utf-8 -*-

"""
lob

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from lob.api_helper import APIHelper


class UsAutocompletionsWritable(object):

    """Implementation of the 'us_autocompletions_writable' model.

    TODO: type model description here.

    Attributes:
        address_prefix (str): Only accepts numbers and street names in an
            alphanumeric format.
        city (str): An optional city input used to filter suggestions. Case
            insensitive and does not match partial abbreviations.
        state (str): An optional state input used to filter suggestions. Case
            insensitive and does not match partial abbreviations.
        zip_code (str): An optional ZIP Code input used to filter suggestions.
            Matches partial entries.
        geo_ip_sort (bool): If `true`, sort suggestions by proximity to the IP
            set in the `X-Forwarded-For` header.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "address_prefix": 'address_prefix',
        "city": 'city',
        "state": 'state',
        "zip_code": 'zip_code',
        "geo_ip_sort": 'geo_ip_sort'
    }

    _optionals = [
        'city',
        'state',
        'zip_code',
        'geo_ip_sort',
    ]

    def __init__(self,
                 address_prefix=None,
                 city=APIHelper.SKIP,
                 state=APIHelper.SKIP,
                 zip_code=APIHelper.SKIP,
                 geo_ip_sort=APIHelper.SKIP):
        """Constructor for the UsAutocompletionsWritable class"""

        # Initialize members of the class
        self.address_prefix = address_prefix 
        if city is not APIHelper.SKIP:
            self.city = city 
        if state is not APIHelper.SKIP:
            self.state = state 
        if zip_code is not APIHelper.SKIP:
            self.zip_code = zip_code 
        if geo_ip_sort is not APIHelper.SKIP:
            self.geo_ip_sort = geo_ip_sort 

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
        address_prefix = dictionary.get("address_prefix") if dictionary.get("address_prefix") else None
        city = dictionary.get("city") if dictionary.get("city") else APIHelper.SKIP
        state = dictionary.get("state") if dictionary.get("state") else APIHelper.SKIP
        zip_code = dictionary.get("zip_code") if dictionary.get("zip_code") else APIHelper.SKIP
        geo_ip_sort = dictionary.get("geo_ip_sort") if "geo_ip_sort" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(address_prefix,
                   city,
                   state,
                   zip_code,
                   geo_ip_sort)
