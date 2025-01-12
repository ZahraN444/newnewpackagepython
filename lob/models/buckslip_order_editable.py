# -*- coding: utf-8 -*-

"""
lob

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class BuckslipOrderEditable(object):

    """Implementation of the 'buckslip_order_editable' model.

    TODO: type model description here.

    Attributes:
        quantity (int): The quantity of buckslips in the order (minimum
            5,000).

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "quantity": 'quantity'
    }

    def __init__(self,
                 quantity=None):
        """Constructor for the BuckslipOrderEditable class"""

        # Initialize members of the class
        self.quantity = quantity 

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
        quantity = dictionary.get("quantity") if dictionary.get("quantity") else None
        # Return an object of this model
        return cls(quantity)
