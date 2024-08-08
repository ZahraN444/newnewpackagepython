# -*- coding: utf-8 -*-

"""
lob

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from lob.api_helper import APIHelper
from lob.models.name_enum import NameEnum
from lob.models.object_3_enum import Object3Enum


class TrackingEventNormal(object):

    """Implementation of the 'tracking_event_normal' model.

    TODO: type model description here.

    Attributes:
        id (str): Unique identifier prefixed with `evnt_`.
        time (datetime): A timestamp in ISO 8601 format of the date USPS
            registered the event.
        date_created (datetime): A timestamp in ISO 8601 format of the date
            the resource was created.
        date_modified (datetime): A timestamp in ISO 8601 format of the date
            the resource was last modified.
        object (Object3Enum): TODO: type description here.
        mtype (str): non-Certified postcards, self mailers, letters, and
            checks
        name (NameEnum): TODO: type description here.
        details (object): Will be `null` for `type=normal` events
        location (str): The zip code in which the scan event occurred. Null
            for `Mailed` events.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "date_created": 'date_created',
        "date_modified": 'date_modified',
        "object": 'object',
        "mtype": 'type',
        "name": 'name',
        "time": 'time',
        "details": 'details',
        "location": 'location'
    }

    _optionals = [
        'time',
        'details',
        'location',
    ]

    _nullables = [
        'details',
        'location',
    ]

    def __init__(self,
                 id=None,
                 date_created=None,
                 date_modified=None,
                 object=None,
                 name=None,
                 time=APIHelper.SKIP,
                 details=APIHelper.SKIP,
                 location=APIHelper.SKIP):
        """Constructor for the TrackingEventNormal class"""

        # Initialize members of the class
        self.id = id 
        if time is not APIHelper.SKIP:
            self.time = APIHelper.apply_datetime_converter(time, APIHelper.RFC3339DateTime) if time else None 
        self.date_created = APIHelper.apply_datetime_converter(date_created, APIHelper.RFC3339DateTime) if date_created else None 
        self.date_modified = APIHelper.apply_datetime_converter(date_modified, APIHelper.RFC3339DateTime) if date_modified else None 
        self.object = object 
        self.mtype = 'normal' 
        self.name = name 
        if details is not APIHelper.SKIP:
            self.details = details 
        if location is not APIHelper.SKIP:
            self.location = location 

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
        name = dictionary.get("name") if dictionary.get("name") else None
        time = APIHelper.RFC3339DateTime.from_value(dictionary.get("time")).datetime if dictionary.get("time") else APIHelper.SKIP
        details = dictionary.get("details") if "details" in dictionary.keys() else APIHelper.SKIP
        location = dictionary.get("location") if "location" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   date_created,
                   date_modified,
                   object,
                   name,
                   time,
                   details,
                   location)

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
            return APIHelper.is_valid_type(value=dictionary.id,
                                           type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.date_created,
                                            type_callable=lambda value: isinstance(value, APIHelper.RFC3339DateTime)) \
                and APIHelper.is_valid_type(value=dictionary.date_modified,
                                            type_callable=lambda value: isinstance(value, APIHelper.RFC3339DateTime)) \
                and APIHelper.is_valid_type(value=dictionary.object,
                                            type_callable=lambda value: Object3Enum.validate(value)) \
                and APIHelper.is_valid_type(value=dictionary.mtype,
                                            type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.name,
                                            type_callable=lambda value: NameEnum.validate(value))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('id'),
                                       type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('date_created'),
                                        type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('date_modified'),
                                        type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('object'),
                                        type_callable=lambda value: Object3Enum.validate(value)) \
            and APIHelper.is_valid_type(value=dictionary.get('type'),
                                        type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('name'),
                                        type_callable=lambda value: NameEnum.validate(value))
