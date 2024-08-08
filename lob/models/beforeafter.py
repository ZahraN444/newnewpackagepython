# -*- coding: utf-8 -*-

"""
lob

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class Beforeafter(object):

    """Implementation of the 'beforeafter' model.

    TODO: type model description here.

    Attributes:
        before (str): A reference to a list entry used for paginating to the
            previous set of entries. This field is pre-populated in the
            `previous_url` field in the return response.
        after (str): A reference to a list entry used for paginating to the
            next set of entries. This field is pre-populated in the `next_url`
            field in the return response.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "before": 'before',
        "after": 'after'
    }

    def __init__(self,
                 before=None,
                 after=None):
        """Constructor for the Beforeafter class"""

        # Initialize members of the class
        self.before = before 
        self.after = after 

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
        before = dictionary.get("before") if dictionary.get("before") else None
        after = dictionary.get("after") if dictionary.get("after") else None
        # Return an object of this model
        return cls(before,
                   after)
