# -*- coding: utf-8 -*-

"""
lob

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from lob.api_helper import APIHelper


class Scans(object):

    """Implementation of the 'scans' model.

    TODO: type model description here.

    Attributes:
        ip_location (str): TODO: type description here.
        scan_date (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ip_location": 'ip_location',
        "scan_date": 'scan_date'
    }

    _optionals = [
        'ip_location',
        'scan_date',
    ]

    def __init__(self,
                 ip_location=APIHelper.SKIP,
                 scan_date=APIHelper.SKIP):
        """Constructor for the Scans class"""

        # Initialize members of the class
        if ip_location is not APIHelper.SKIP:
            self.ip_location = ip_location 
        if scan_date is not APIHelper.SKIP:
            self.scan_date = scan_date 

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
        ip_location = dictionary.get("ip_location") if dictionary.get("ip_location") else APIHelper.SKIP
        scan_date = dictionary.get("scan_date") if dictionary.get("scan_date") else APIHelper.SKIP
        # Return an object of this model
        return cls(ip_location,
                   scan_date)