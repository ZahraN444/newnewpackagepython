# -*- coding: utf-8 -*-

"""
lob

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from lob.api_helper import APIHelper


class CardUpdatable(object):

    """Implementation of the 'card_updatable' model.

    TODO: type model description here.

    Attributes:
        description (str): Description of the card.
        auto_reorder (bool): Allows for auto reordering
        reorder_quantity (float): The quantity of items to be reordered (only
            required when auto_reorder is true).

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "description": 'description',
        "auto_reorder": 'auto_reorder',
        "reorder_quantity": 'reorder_quantity'
    }

    _optionals = [
        'description',
        'auto_reorder',
        'reorder_quantity',
    ]

    _nullables = [
        'description',
    ]

    def __init__(self,
                 description=APIHelper.SKIP,
                 auto_reorder=APIHelper.SKIP,
                 reorder_quantity=APIHelper.SKIP):
        """Constructor for the CardUpdatable class"""

        # Initialize members of the class
        if description is not APIHelper.SKIP:
            self.description = description 
        if auto_reorder is not APIHelper.SKIP:
            self.auto_reorder = auto_reorder 
        if reorder_quantity is not APIHelper.SKIP:
            self.reorder_quantity = reorder_quantity 

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
        description = dictionary.get("description") if "description" in dictionary.keys() else APIHelper.SKIP
        auto_reorder = dictionary.get("auto_reorder") if "auto_reorder" in dictionary.keys() else APIHelper.SKIP
        reorder_quantity = dictionary.get("reorder_quantity") if dictionary.get("reorder_quantity") else APIHelper.SKIP
        # Return an object of this model
        return cls(description,
                   auto_reorder,
                   reorder_quantity)
