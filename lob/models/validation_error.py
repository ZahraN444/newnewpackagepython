# -*- coding: utf-8 -*-

"""
lob

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from lob.api_helper import APIHelper


class ValidationError(object):

    """Implementation of the 'ValidationError' model.

    TODO: type model description here.

    Attributes:
        loc (List[str | int]): TODO: type description here.
        msg (str): TODO: type description here.
        mtype (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "loc": 'loc',
        "msg": 'msg',
        "mtype": 'type'
    }

    def __init__(self,
                 loc=None,
                 msg=None,
                 mtype=None):
        """Constructor for the ValidationError class"""

        # Initialize members of the class
        self.loc = loc 
        self.msg = msg 
        self.mtype = mtype 

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
        loc = APIHelper.deserialize_union_type(UnionTypeLookUp.get('ValidationErrorLoc'), dictionary.get('loc'), False) if dictionary.get('loc') is not None else None
        msg = dictionary.get("msg") if dictionary.get("msg") else None
        mtype = dictionary.get("type") if dictionary.get("type") else None
        # Return an object of this model
        return cls(loc,
                   msg,
                   mtype)

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
            return UnionTypeLookUp.get('ValidationErrorLoc').validate(dictionary.loc).is_valid \
                and APIHelper.is_valid_type(value=dictionary.msg,
                                            type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.mtype,
                                            type_callable=lambda value: isinstance(value, str))

        if not isinstance(dictionary, dict):
            return False

        return UnionTypeLookUp.get('ValidationErrorLoc').validate(dictionary.get('loc')).is_valid \
            and APIHelper.is_valid_type(value=dictionary.get('msg'),
                                        type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('type'),
                                        type_callable=lambda value: isinstance(value, str))
