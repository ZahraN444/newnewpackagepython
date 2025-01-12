# -*- coding: utf-8 -*-

"""
lob

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from lob.api_helper import APIHelper


class CardOrder(object):

    """Implementation of the 'card_order' model.

    TODO: type model description here.

    Attributes:
        date_created (datetime): A timestamp in ISO 8601 format of the date
            the resource was created.
        date_modified (datetime): A timestamp in ISO 8601 format of the date
            the resource was last modified.
        deleted (bool): Only returned if the resource has been successfully
            deleted.
        object (str): Value is resource type.
        id (str): Unique identifier prefixed with `co_`.
        card_id (str): Unique identifier prefixed with `card_`.
        status (Status2Enum): TODO: type description here.
        inventory (float): The inventory of the card order.
        quantity_ordered (float): The quantity of cards ordered
        unit_price (float): The unit price for the card order.
        cancelled_reason (str): The reason for cancellation.
        availability_date (datetime): A timestamp in ISO 8601 format of the
            date the resource was created.
        expected_availability_date (datetime): The fixed deadline for the
            cards to be printed.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "date_created": 'date_created',
        "date_modified": 'date_modified',
        "object": 'object',
        "deleted": 'deleted',
        "id": 'id',
        "card_id": 'card_id',
        "status": 'status',
        "inventory": 'inventory',
        "quantity_ordered": 'quantity_ordered',
        "unit_price": 'unit_price',
        "cancelled_reason": 'cancelled_reason',
        "availability_date": 'availability_date',
        "expected_availability_date": 'expected_availability_date'
    }

    _optionals = [
        'deleted',
        'id',
        'card_id',
        'status',
        'inventory',
        'quantity_ordered',
        'unit_price',
        'cancelled_reason',
        'availability_date',
        'expected_availability_date',
    ]

    def __init__(self,
                 date_created=None,
                 date_modified=None,
                 object=None,
                 deleted=APIHelper.SKIP,
                 id=APIHelper.SKIP,
                 card_id=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 inventory=0,
                 quantity_ordered=0,
                 unit_price=0,
                 cancelled_reason=APIHelper.SKIP,
                 availability_date=APIHelper.SKIP,
                 expected_availability_date=APIHelper.SKIP):
        """Constructor for the CardOrder class"""

        # Initialize members of the class
        self.date_created = APIHelper.apply_datetime_converter(date_created, APIHelper.RFC3339DateTime) if date_created else None 
        self.date_modified = APIHelper.apply_datetime_converter(date_modified, APIHelper.RFC3339DateTime) if date_modified else None 
        if deleted is not APIHelper.SKIP:
            self.deleted = deleted 
        self.object = object 
        if id is not APIHelper.SKIP:
            self.id = id 
        if card_id is not APIHelper.SKIP:
            self.card_id = card_id 
        if status is not APIHelper.SKIP:
            self.status = status 
        self.inventory = inventory 
        self.quantity_ordered = quantity_ordered 
        self.unit_price = unit_price 
        if cancelled_reason is not APIHelper.SKIP:
            self.cancelled_reason = cancelled_reason 
        if availability_date is not APIHelper.SKIP:
            self.availability_date = APIHelper.apply_datetime_converter(availability_date, APIHelper.RFC3339DateTime) if availability_date else None 
        if expected_availability_date is not APIHelper.SKIP:
            self.expected_availability_date = APIHelper.apply_datetime_converter(expected_availability_date, APIHelper.RFC3339DateTime) if expected_availability_date else None 

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
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        card_id = dictionary.get("card_id") if dictionary.get("card_id") else APIHelper.SKIP
        status = dictionary.get("status") if dictionary.get("status") else APIHelper.SKIP
        inventory = dictionary.get("inventory") if dictionary.get("inventory") else 0
        quantity_ordered = dictionary.get("quantity_ordered") if dictionary.get("quantity_ordered") else 0
        unit_price = dictionary.get("unit_price") if dictionary.get("unit_price") else 0
        cancelled_reason = dictionary.get("cancelled_reason") if dictionary.get("cancelled_reason") else APIHelper.SKIP
        availability_date = APIHelper.RFC3339DateTime.from_value(dictionary.get("availability_date")).datetime if dictionary.get("availability_date") else APIHelper.SKIP
        expected_availability_date = APIHelper.RFC3339DateTime.from_value(dictionary.get("expected_availability_date")).datetime if dictionary.get("expected_availability_date") else APIHelper.SKIP
        # Return an object of this model
        return cls(date_created,
                   date_modified,
                   object,
                   deleted,
                   id,
                   card_id,
                   status,
                   inventory,
                   quantity_ordered,
                   unit_price,
                   cancelled_reason,
                   availability_date,
                   expected_availability_date)
