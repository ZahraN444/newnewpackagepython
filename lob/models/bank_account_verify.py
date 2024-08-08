# -*- coding: utf-8 -*-

"""
lob

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class BankAccountVerify(object):

    """Implementation of the 'bank_account_verify' model.

    TODO: type model description here.

    Attributes:
        amounts (List[int]): In live mode, an array containing the two micro
            deposits (in cents) placed in the bank account. In test mode, no
            micro deposits will be placed, so any two integers between `1` and
            `100` will work.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "amounts": 'amounts'
    }

    def __init__(self,
                 amounts=None):
        """Constructor for the BankAccountVerify class"""

        # Initialize members of the class
        self.amounts = amounts 

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
        amounts = dictionary.get("amounts") if dictionary.get("amounts") else None
        # Return an object of this model
        return cls(amounts)
