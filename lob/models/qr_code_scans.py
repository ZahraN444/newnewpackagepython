# -*- coding: utf-8 -*-

"""
lob

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from lob.api_helper import APIHelper
from lob.models.scans import Scans


class QrCodeScans(object):

    """Implementation of the 'qr_code_scans' model.

    TODO: type model description here.

    Attributes:
        resource_id (str): Unique identifier for each mail piece.
        date_created (datetime): A timestamp in ISO 8601 format of the date
            the resource was created.
        number_of_scans (float): Number of times the QR Code associated with
            this mail piece was scanned.
        scans (List[Scans]): Detailed scan information associated with each
            mail piece.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "resource_id": 'resource_id',
        "date_created": 'date_created',
        "number_of_scans": 'number_of_scans',
        "scans": 'scans'
    }

    _optionals = [
        'resource_id',
        'date_created',
        'number_of_scans',
        'scans',
    ]

    def __init__(self,
                 resource_id=APIHelper.SKIP,
                 date_created=APIHelper.SKIP,
                 number_of_scans=APIHelper.SKIP,
                 scans=APIHelper.SKIP):
        """Constructor for the QrCodeScans class"""

        # Initialize members of the class
        if resource_id is not APIHelper.SKIP:
            self.resource_id = resource_id 
        if date_created is not APIHelper.SKIP:
            self.date_created = APIHelper.apply_datetime_converter(date_created, APIHelper.RFC3339DateTime) if date_created else None 
        if number_of_scans is not APIHelper.SKIP:
            self.number_of_scans = number_of_scans 
        if scans is not APIHelper.SKIP:
            self.scans = scans 

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
        resource_id = dictionary.get("resource_id") if dictionary.get("resource_id") else APIHelper.SKIP
        date_created = APIHelper.RFC3339DateTime.from_value(dictionary.get("date_created")).datetime if dictionary.get("date_created") else APIHelper.SKIP
        number_of_scans = dictionary.get("number_of_scans") if dictionary.get("number_of_scans") else APIHelper.SKIP
        scans = None
        if dictionary.get('scans') is not None:
            scans = [Scans.from_dictionary(x) for x in dictionary.get('scans')]
        else:
            scans = APIHelper.SKIP
        # Return an object of this model
        return cls(resource_id,
                   date_created,
                   number_of_scans,
                   scans)