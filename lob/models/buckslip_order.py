# -*- coding: utf-8 -*-

"""
lob

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from lob.api_helper import APIHelper


class BuckslipOrder(object):

    """Implementation of the 'buckslip_order' model.

    TODO: type model description here.

    Attributes:
        date_created (datetime): A timestamp in ISO 8601 format of the date
            the resource was created.
        date_modified (datetime): A timestamp in ISO 8601 format of the date
            the resource was last modified.
        deleted (bool): Only returned if the resource has been successfully
            deleted.
        object (str): Value is resource type.
        id (str): Unique identifier prefixed with `bo_`.
        buckslip_id (str): Unique identifier prefixed with `bck_`.
        status (StatusEnum): TODO: type description here.
        quantity_ordered (float): The quantity of buckslips ordered.
        unit_price (float): The unit price for the buckslip order.
        inventory (float): The inventory of the buckslip order.
        cancelled_reason (str): The reason for cancellation.
        availability_date (datetime): A timestamp in ISO 8601 format of the
            date the resource was created.
        expected_availability_date (datetime): The fixed deadline for the
            buckslips to be printed.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "date_created": 'date_created',
        "date_modified": 'date_modified',
        "object": 'object',
        "deleted": 'deleted',
        "id": 'id',
        "buckslip_id": 'buckslip_id',
        "status": 'status',
        "quantity_ordered": 'quantity_ordered',
        "unit_price": 'unit_price',
        "inventory": 'inventory',
        "cancelled_reason": 'cancelled_reason',
        "availability_date": 'availability_date',
        "expected_availability_date": 'expected_availability_date'
    }

    _optionals = [
        'deleted',
        'id',
        'buckslip_id',
        'status',
        'quantity_ordered',
        'unit_price',
        'inventory',
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
                 buckslip_id=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 quantity_ordered=0,
                 unit_price=0,
                 inventory=0,
                 cancelled_reason=APIHelper.SKIP,
                 availability_date=APIHelper.SKIP,
                 expected_availability_date=APIHelper.SKIP):
        """Constructor for the BuckslipOrder class"""

        # Initialize members of the class
        self.date_created = APIHelper.apply_datetime_converter(date_created, APIHelper.RFC3339DateTime) if date_created else None 
        self.date_modified = APIHelper.apply_datetime_converter(date_modified, APIHelper.RFC3339DateTime) if date_modified else None 
        if deleted is not APIHelper.SKIP:
            self.deleted = deleted 
        self.object = object 
        if id is not APIHelper.SKIP:
            self.id = id 
        if buckslip_id is not APIHelper.SKIP:
            self.buckslip_id = buckslip_id 
        if status is not APIHelper.SKIP:
            self.status = status 
        self.quantity_ordered = quantity_ordered 
        self.unit_price = unit_price 
        self.inventory = inventory 
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
        buckslip_id = dictionary.get("buckslip_id") if dictionary.get("buckslip_id") else APIHelper.SKIP
        status = dictionary.get("status") if dictionary.get("status") else APIHelper.SKIP
        quantity_ordered = dictionary.get("quantity_ordered") if dictionary.get("quantity_ordered") else 0
        unit_price = dictionary.get("unit_price") if dictionary.get("unit_price") else 0
        inventory = dictionary.get("inventory") if dictionary.get("inventory") else 0
        cancelled_reason = dictionary.get("cancelled_reason") if dictionary.get("cancelled_reason") else APIHelper.SKIP
        availability_date = APIHelper.RFC3339DateTime.from_value(dictionary.get("availability_date")).datetime if dictionary.get("availability_date") else APIHelper.SKIP
        expected_availability_date = APIHelper.RFC3339DateTime.from_value(dictionary.get("expected_availability_date")).datetime if dictionary.get("expected_availability_date") else APIHelper.SKIP
        # Return an object of this model
        return cls(date_created,
                   date_modified,
                   object,
                   deleted,
                   id,
                   buckslip_id,
                   status,
                   quantity_ordered,
                   unit_price,
                   inventory,
                   cancelled_reason,
                   availability_date,
                   expected_availability_date)

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
            return APIHelper.is_valid_type(value=dictionary.date_created,
                                           type_callable=lambda value: isinstance(value, APIHelper.RFC3339DateTime)) \
                and APIHelper.is_valid_type(value=dictionary.date_modified,
                                            type_callable=lambda value: isinstance(value, APIHelper.RFC3339DateTime)) \
                and APIHelper.is_valid_type(value=dictionary.object,
                                            type_callable=lambda value: isinstance(value, str))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('date_created'),
                                       type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('date_modified'),
                                        type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('object'),
                                        type_callable=lambda value: isinstance(value, str))
