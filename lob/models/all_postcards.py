# -*- coding: utf-8 -*-

"""
lob

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from lob.api_helper import APIHelper
from lob.models.postcard import Postcard


class AllPostcards(object):

    """Implementation of the 'all_postcards' model.

    TODO: type model description here.

    Attributes:
        object (str): Value is resource type.
        next_url (str): Url of next page of items in list.
        previous_url (str): Url of previous page of items in list.
        count (int): number of resources in a set
        total_count (int): Indicates the total number of records. Provided
            when the request specifies an "include" query parameter
        data (List[Postcard]): list of postcards

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "object": 'object',
        "next_url": 'next_url',
        "previous_url": 'previous_url',
        "count": 'count',
        "total_count": 'total_count',
        "data": 'data'
    }

    _optionals = [
        'object',
        'next_url',
        'previous_url',
        'count',
        'total_count',
        'data',
    ]

    _nullables = [
        'next_url',
        'previous_url',
    ]

    def __init__(self,
                 object=APIHelper.SKIP,
                 next_url=APIHelper.SKIP,
                 previous_url=APIHelper.SKIP,
                 count=APIHelper.SKIP,
                 total_count=APIHelper.SKIP,
                 data=APIHelper.SKIP):
        """Constructor for the AllPostcards class"""

        # Initialize members of the class
        if object is not APIHelper.SKIP:
            self.object = object 
        if next_url is not APIHelper.SKIP:
            self.next_url = next_url 
        if previous_url is not APIHelper.SKIP:
            self.previous_url = previous_url 
        if count is not APIHelper.SKIP:
            self.count = count 
        if total_count is not APIHelper.SKIP:
            self.total_count = total_count 
        if data is not APIHelper.SKIP:
            self.data = data 

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
        object = dictionary.get("object") if dictionary.get("object") else APIHelper.SKIP
        next_url = dictionary.get("next_url") if "next_url" in dictionary.keys() else APIHelper.SKIP
        previous_url = dictionary.get("previous_url") if "previous_url" in dictionary.keys() else APIHelper.SKIP
        count = dictionary.get("count") if dictionary.get("count") else APIHelper.SKIP
        total_count = dictionary.get("total_count") if dictionary.get("total_count") else APIHelper.SKIP
        data = None
        if dictionary.get('data') is not None:
            data = [Postcard.from_dictionary(x) for x in dictionary.get('data')]
        else:
            data = APIHelper.SKIP
        # Return an object of this model
        return cls(object,
                   next_url,
                   previous_url,
                   count,
                   total_count,
                   data)
