# -*- coding: utf-8 -*-

"""
lob

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from lob.api_helper import APIHelper


class BuckslipEditable(object):

    """Implementation of the 'buckslip_editable' model.

    TODO: type model description here.

    Attributes:
        description (str): Description of the buckslip.
        size (SizeEnum): TODO: type description here.
        front (str): A PDF template for the front of the buckslip
        back (str | None): A PDF template for the back of the buckslip

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "front": 'front',
        "description": 'description',
        "size": 'size',
        "back": 'back'
    }

    _optionals = [
        'description',
        'size',
        'back',
    ]

    _nullables = [
        'description',
    ]

    def __init__(self,
                 front=None,
                 description=APIHelper.SKIP,
                 size=APIHelper.SKIP,
                 back=APIHelper.SKIP):
        """Constructor for the BuckslipEditable class"""

        # Initialize members of the class
        if description is not APIHelper.SKIP:
            self.description = description 
        if size is not APIHelper.SKIP:
            self.size = size 
        self.front = front 
        if back is not APIHelper.SKIP:
            self.back = back 

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
        from lob.utilities.union_type_lookup import UnionTypeLookUp

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        front = APIHelper.deserialize_union_type(UnionTypeLookUp.get('BuckslipEditableFront'), dictionary.get('front'), False) if dictionary.get('front') is not None else None
        description = dictionary.get("description") if "description" in dictionary.keys() else APIHelper.SKIP
        size = dictionary.get("size") if dictionary.get("size") else APIHelper.SKIP
        back = APIHelper.deserialize_union_type(UnionTypeLookUp.get('BuckslipEditableBack'), dictionary.get('back'), False) if dictionary.get('back') is not None else APIHelper.SKIP
        # Return an object of this model
        return cls(front,
                   description,
                   size,
                   back)

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
        from lob.utilities.union_type_lookup import UnionTypeLookUp

        if isinstance(dictionary, cls):
            return UnionTypeLookUp.get('BuckslipEditableFront').validate(dictionary.front).is_valid

        if not isinstance(dictionary, dict):
            return False

        return UnionTypeLookUp.get('BuckslipEditableFront').validate(dictionary.get('front')).is_valid
