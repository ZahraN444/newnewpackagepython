# -*- coding: utf-8 -*-

"""
lob

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from lob.api_helper import APIHelper
from lob.models.country_extended_enum import CountryExtendedEnum


class InlineAddressIntl(object):

    """Implementation of the 'inline_address_intl' model.

    TODO: type model description here.

    Attributes:
        address_line_1 (str): The primary number, street name, and directional
            information.
        address_line_2 (str): An optional field containing any information
            which can't fit into line 1.
        address_city (str): TODO: type description here.
        address_state (str): TODO: type description here.
        address_zip (str): Optional postal code.
        description (str): An internal description that identifies this
            resource. Must be no longer than 255 characters.
        name (str): Either `name` or `company` is required, you may also add
            both. Must be no longer than 40 characters. If both `name` and
            `company` are provided, they will be printed on two separate lines
            above the rest of the address.
        company (str): Either `name` or `company` is required, you may also
            add both. Must be no longer than 40 characters. If both `name` and
            `company` are provided, they will be printed on two separate lines
            above the rest of the address. This field can be used for any
            secondary recipient information which is not part of the actual
            mailing address (Company Name, Department, Attention Line, etc).
        phone (str): Must be no longer than 40 characters.
        email (str): Must be no longer than 100 characters.
        address_country (CountryExtendedEnum): TODO: type description here.
        metadata (Dict[str, str]): Use metadata to store custom information
            for tagging and labeling back to your internal systems. Must be an
            object with up to 20 key-value pairs. Keys must be at most 40
            characters and values must be at most 500 characters. Neither can
            contain the characters `"` and `\`. i.e. '{"customer_id" :
            "NEWYORK2015"}' Nested objects are not supported.  See
            [Metadata](#section/Metadata) for more information.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "address_line_1": 'address_line1',
        "address_city": 'address_city',
        "address_state": 'address_state',
        "address_zip": 'address_zip',
        "name": 'name',
        "company": 'company',
        "address_country": 'address_country',
        "address_line_2": 'address_line2',
        "description": 'description',
        "phone": 'phone',
        "email": 'email',
        "metadata": 'metadata'
    }

    _optionals = [
        'address_line_2',
        'description',
        'phone',
        'email',
        'metadata',
    ]

    _nullables = [
        'address_line_2',
        'address_city',
        'address_state',
        'address_zip',
        'description',
        'name',
        'company',
        'phone',
        'email',
    ]

    def __init__(self,
                 address_line_1=None,
                 address_city=None,
                 address_state=None,
                 address_zip=None,
                 name=None,
                 company=None,
                 address_country=None,
                 address_line_2=APIHelper.SKIP,
                 description=APIHelper.SKIP,
                 phone=APIHelper.SKIP,
                 email=APIHelper.SKIP,
                 metadata=APIHelper.SKIP):
        """Constructor for the InlineAddressIntl class"""

        # Initialize members of the class
        self.address_line_1 = address_line_1 
        if address_line_2 is not APIHelper.SKIP:
            self.address_line_2 = address_line_2 
        self.address_city = address_city 
        self.address_state = address_state 
        self.address_zip = address_zip 
        if description is not APIHelper.SKIP:
            self.description = description 
        self.name = name 
        self.company = company 
        if phone is not APIHelper.SKIP:
            self.phone = phone 
        if email is not APIHelper.SKIP:
            self.email = email 
        self.address_country = address_country 
        if metadata is not APIHelper.SKIP:
            self.metadata = metadata 

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
        address_line_1 = dictionary.get("address_line1") if dictionary.get("address_line1") else None
        address_city = dictionary.get("address_city") if dictionary.get("address_city") else None
        address_state = dictionary.get("address_state") if dictionary.get("address_state") else None
        address_zip = dictionary.get("address_zip") if dictionary.get("address_zip") else None
        name = dictionary.get("name") if dictionary.get("name") else None
        company = dictionary.get("company") if dictionary.get("company") else None
        address_country = dictionary.get("address_country") if dictionary.get("address_country") else None
        address_line_2 = dictionary.get("address_line2") if "address_line2" in dictionary.keys() else APIHelper.SKIP
        description = dictionary.get("description") if "description" in dictionary.keys() else APIHelper.SKIP
        phone = dictionary.get("phone") if "phone" in dictionary.keys() else APIHelper.SKIP
        email = dictionary.get("email") if "email" in dictionary.keys() else APIHelper.SKIP
        metadata = dictionary.get("metadata") if dictionary.get("metadata") else APIHelper.SKIP
        # Return an object of this model
        return cls(address_line_1,
                   address_city,
                   address_state,
                   address_zip,
                   name,
                   company,
                   address_country,
                   address_line_2,
                   description,
                   phone,
                   email,
                   metadata)

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
            return APIHelper.is_valid_type(value=dictionary.address_line_1,
                                           type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.address_city,
                                            type_callable=lambda value: isinstance(value, str),
                                            is_value_nullable=True) \
                and APIHelper.is_valid_type(value=dictionary.address_state,
                                            type_callable=lambda value: isinstance(value, str),
                                            is_value_nullable=True) \
                and APIHelper.is_valid_type(value=dictionary.address_zip,
                                            type_callable=lambda value: isinstance(value, str),
                                            is_value_nullable=True) \
                and APIHelper.is_valid_type(value=dictionary.name,
                                            type_callable=lambda value: isinstance(value, str),
                                            is_value_nullable=True) \
                and APIHelper.is_valid_type(value=dictionary.company,
                                            type_callable=lambda value: isinstance(value, str),
                                            is_value_nullable=True) \
                and APIHelper.is_valid_type(value=dictionary.address_country,
                                            type_callable=lambda value: CountryExtendedEnum.validate(value))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('address_line1'),
                                       type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('address_city'),
                                        type_callable=lambda value: isinstance(value, str),
                                        is_value_nullable=True) \
            and APIHelper.is_valid_type(value=dictionary.get('address_state'),
                                        type_callable=lambda value: isinstance(value, str),
                                        is_value_nullable=True) \
            and APIHelper.is_valid_type(value=dictionary.get('address_zip'),
                                        type_callable=lambda value: isinstance(value, str),
                                        is_value_nullable=True) \
            and APIHelper.is_valid_type(value=dictionary.get('name'),
                                        type_callable=lambda value: isinstance(value, str),
                                        is_value_nullable=True) \
            and APIHelper.is_valid_type(value=dictionary.get('company'),
                                        type_callable=lambda value: isinstance(value, str),
                                        is_value_nullable=True) \
            and APIHelper.is_valid_type(value=dictionary.get('address_country'),
                                        type_callable=lambda value: CountryExtendedEnum.validate(value))
