# -*- coding: utf-8 -*-

"""
lob

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from lob.api_helper import APIHelper


class CompanyValidation(object):

    """Implementation of the 'company_validation' model.

    TODO: type model description here.

    Attributes:
        id (str): Unique identifier prefixed with `id_validation_`.
        company (str): The name of the company or firm.
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
        last_line (str): Combination of the following applicable `components`:
            * City (`city`) * State (`state`) * ZIP code (`zip_code`) * ZIP+4
            (`zip_code_plus_4`)
        score (float): A numerical score between 0 and 100 that represents the
            likelihood the provided name is associated with a physical
            address.
        confidence (ConfidenceEnum): TODO: type description here.
        object (Object6Enum): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "company": 'company',
        "primary_line": 'primary_line',
        "secondary_line": 'secondary_line',
        "urbanization": 'urbanization',
        "last_line": 'last_line',
        "score": 'score',
        "confidence": 'confidence',
        "object": 'object'
    }

    _optionals = [
        'id',
        'company',
        'primary_line',
        'secondary_line',
        'urbanization',
        'last_line',
        'score',
        'confidence',
        'object',
    ]

    _nullables = [
        'company',
        'score',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 company=APIHelper.SKIP,
                 primary_line=APIHelper.SKIP,
                 secondary_line=APIHelper.SKIP,
                 urbanization=APIHelper.SKIP,
                 last_line=APIHelper.SKIP,
                 score=APIHelper.SKIP,
                 confidence=APIHelper.SKIP,
                 object=APIHelper.SKIP):
        """Constructor for the CompanyValidation class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if company is not APIHelper.SKIP:
            self.company = company 
        if primary_line is not APIHelper.SKIP:
            self.primary_line = primary_line 
        if secondary_line is not APIHelper.SKIP:
            self.secondary_line = secondary_line 
        if urbanization is not APIHelper.SKIP:
            self.urbanization = urbanization 
        if last_line is not APIHelper.SKIP:
            self.last_line = last_line 
        if score is not APIHelper.SKIP:
            self.score = score 
        if confidence is not APIHelper.SKIP:
            self.confidence = confidence 
        if object is not APIHelper.SKIP:
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
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        company = dictionary.get("company") if "company" in dictionary.keys() else APIHelper.SKIP
        primary_line = dictionary.get("primary_line") if dictionary.get("primary_line") else APIHelper.SKIP
        secondary_line = dictionary.get("secondary_line") if dictionary.get("secondary_line") else APIHelper.SKIP
        urbanization = dictionary.get("urbanization") if dictionary.get("urbanization") else APIHelper.SKIP
        last_line = dictionary.get("last_line") if dictionary.get("last_line") else APIHelper.SKIP
        score = dictionary.get("score") if "score" in dictionary.keys() else APIHelper.SKIP
        confidence = dictionary.get("confidence") if dictionary.get("confidence") else APIHelper.SKIP
        object = dictionary.get("object") if dictionary.get("object") else APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   company,
                   primary_line,
                   secondary_line,
                   urbanization,
                   last_line,
                   score,
                   confidence,
                   object)

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
            return True

        if not isinstance(dictionary, dict):
            return False

        return True