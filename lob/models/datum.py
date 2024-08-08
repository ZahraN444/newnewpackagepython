# -*- coding: utf-8 -*-

"""
lob

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from lob.api_helper import APIHelper


class Datum(object):

    """Implementation of the 'Datum' model.

    TODO: type model description here.

    Attributes:
        row_number (float): The row number of the csv file containing this
            data.
        status (Status4Enum): TODO: type description here.
        error_message (str): The error message detailing the reason why
            processing the line item failed.
        mailpiece_id (str): The mailpiece id created from the line item when
            it was validated.
        original_data (object): Key-value pairs where each key is the column
            header and each value is the value of the column for the row.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "row_number": 'rowNumber',
        "status": 'status',
        "error_message": 'errorMessage',
        "mailpiece_id": 'mailpieceId',
        "original_data": 'originalData'
    }

    _optionals = [
        'row_number',
        'status',
        'error_message',
        'mailpiece_id',
        'original_data',
    ]

    _nullables = [
        'error_message',
        'mailpiece_id',
    ]

    def __init__(self,
                 row_number=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 error_message=APIHelper.SKIP,
                 mailpiece_id=APIHelper.SKIP,
                 original_data=APIHelper.SKIP):
        """Constructor for the Datum class"""

        # Initialize members of the class
        if row_number is not APIHelper.SKIP:
            self.row_number = row_number 
        if status is not APIHelper.SKIP:
            self.status = status 
        if error_message is not APIHelper.SKIP:
            self.error_message = error_message 
        if mailpiece_id is not APIHelper.SKIP:
            self.mailpiece_id = mailpiece_id 
        if original_data is not APIHelper.SKIP:
            self.original_data = original_data 

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
        row_number = dictionary.get("rowNumber") if dictionary.get("rowNumber") else APIHelper.SKIP
        status = dictionary.get("status") if dictionary.get("status") else APIHelper.SKIP
        error_message = dictionary.get("errorMessage") if "errorMessage" in dictionary.keys() else APIHelper.SKIP
        mailpiece_id = dictionary.get("mailpieceId") if "mailpieceId" in dictionary.keys() else APIHelper.SKIP
        original_data = dictionary.get("originalData") if dictionary.get("originalData") else APIHelper.SKIP
        # Return an object of this model
        return cls(row_number,
                   status,
                   error_message,
                   mailpiece_id,
                   original_data)