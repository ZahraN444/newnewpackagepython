# -*- coding: utf-8 -*-

"""
lob

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from lob.api_helper import APIHelper


class RecipientInput(object):

    """Implementation of the 'recipient_input' model.

    TODO: type model description here.

    Attributes:
        recipient (str): The intended recipient, typically a person's or
            firm's name.
        primary_line (str): The primary delivery line (usually the street
            address) of the address. Combination of the following applicable
            `components`: * `primary_number` * `street_predirection` *
            `street_name` * `street_suffix` * `street_postdirection` *
            `secondary_designator` * `secondary_number` * `pmb_designator` *
            `pmb_number`
        secondary_line (str): The secondary delivery line of the address. This
            field is typically empty but may contain information if
            `primary_line` is too long.
        urbanization (str): Only present for addresses in Puerto Rico. An
            urbanization refers to an area, sector, or development within a
            city. See <a
            href="https://pe.usps.com/text/pub28/28api_008.htm#:~:text=I51.,-4%
            20Urbanizations&text=In%20Puerto%20Rico%2C%20identical%20street,pla
            ced%20before%20the%20urbanization%20name." target="_blank">USPS
            documentation</a> for clarification.
        city (str): TODO: type description here.
        state (str): The <a href="https://en.wikipedia.org/wiki/ISO_3166-2:US"
            target="_blank">ISO 3166-2</a> two letter code or subdivision name
            for the state. `city` and `state` are required if no `zip_code` is
            passed.
        zip_code (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "recipient": 'recipient',
        "primary_line": 'primary_line',
        "city": 'city',
        "state": 'state',
        "zip_code": 'zip_code',
        "secondary_line": 'secondary_line',
        "urbanization": 'urbanization'
    }

    _optionals = [
        'secondary_line',
        'urbanization',
    ]

    _nullables = [
        'recipient',
    ]

    def __init__(self,
                 recipient=None,
                 primary_line=None,
                 city=None,
                 state=None,
                 zip_code=None,
                 secondary_line=APIHelper.SKIP,
                 urbanization=APIHelper.SKIP):
        """Constructor for the RecipientInput class"""

        # Initialize members of the class
        self.recipient = recipient 
        self.primary_line = primary_line 
        if secondary_line is not APIHelper.SKIP:
            self.secondary_line = secondary_line 
        if urbanization is not APIHelper.SKIP:
            self.urbanization = urbanization 
        self.city = city 
        self.state = state 
        self.zip_code = zip_code 

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
        recipient = dictionary.get("recipient") if dictionary.get("recipient") else None
        primary_line = dictionary.get("primary_line") if dictionary.get("primary_line") else None
        city = dictionary.get("city") if dictionary.get("city") else None
        state = dictionary.get("state") if dictionary.get("state") else None
        zip_code = dictionary.get("zip_code") if dictionary.get("zip_code") else None
        secondary_line = dictionary.get("secondary_line") if dictionary.get("secondary_line") else APIHelper.SKIP
        urbanization = dictionary.get("urbanization") if dictionary.get("urbanization") else APIHelper.SKIP
        # Return an object of this model
        return cls(recipient,
                   primary_line,
                   city,
                   state,
                   zip_code,
                   secondary_line,
                   urbanization)