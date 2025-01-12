# -*- coding: utf-8 -*-

"""
lob

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from lob.api_helper import APIHelper


class TrackingEventBase(object):

    """Implementation of the 'tracking_event_base' model.

    As mail pieces travel through the mail stream, USPS scans their unique
    barcodes, and Lob processes these mail scans to generate tracking events.

    Attributes:
        id (str): Unique identifier prefixed with `evnt_`.
        time (datetime): A timestamp in ISO 8601 format of the date USPS
            registered the event.
        date_created (datetime): A timestamp in ISO 8601 format of the date
            the resource was created.
        date_modified (datetime): A timestamp in ISO 8601 format of the date
            the resource was last modified.
        object (Object3Enum): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "date_created": 'date_created',
        "date_modified": 'date_modified',
        "object": 'object',
        "time": 'time'
    }

    _optionals = [
        'time',
    ]

    def __init__(self,
                 id=None,
                 date_created=None,
                 date_modified=None,
                 object=None,
                 time=APIHelper.SKIP):
        """Constructor for the TrackingEventBase class"""

        # Initialize members of the class
        self.id = id 
        if time is not APIHelper.SKIP:
            self.time = APIHelper.apply_datetime_converter(time, APIHelper.RFC3339DateTime) if time else None 
        self.date_created = APIHelper.apply_datetime_converter(date_created, APIHelper.RFC3339DateTime) if date_created else None 
        self.date_modified = APIHelper.apply_datetime_converter(date_modified, APIHelper.RFC3339DateTime) if date_modified else None 
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
        id = dictionary.get("id") if dictionary.get("id") else None
        date_created = APIHelper.RFC3339DateTime.from_value(dictionary.get("date_created")).datetime if dictionary.get("date_created") else None
        date_modified = APIHelper.RFC3339DateTime.from_value(dictionary.get("date_modified")).datetime if dictionary.get("date_modified") else None
        object = dictionary.get("object") if dictionary.get("object") else None
        time = APIHelper.RFC3339DateTime.from_value(dictionary.get("time")).datetime if dictionary.get("time") else APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   date_created,
                   date_modified,
                   object,
                   time)
