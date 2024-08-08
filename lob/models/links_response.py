# -*- coding: utf-8 -*-

"""
lob

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from lob.api_helper import APIHelper
from lob.models.link_response import LinkResponse


class LinksResponse(object):

    """Implementation of the 'links_response' model.

    TODO: type model description here.

    Attributes:
        count (int): The number of results in the current response.
        limit (int): How many results to return.
        offset (int): An integer that designates the offset at which to begin
            returning results. Defaults to 0.
        data (List[LinkResponse]): list of links

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "count": 'count',
        "limit": 'limit',
        "offset": 'offset',
        "data": 'data'
    }

    _optionals = [
        'count',
        'limit',
        'offset',
        'data',
    ]

    def __init__(self,
                 count=APIHelper.SKIP,
                 limit=APIHelper.SKIP,
                 offset=APIHelper.SKIP,
                 data=APIHelper.SKIP):
        """Constructor for the LinksResponse class"""

        # Initialize members of the class
        if count is not APIHelper.SKIP:
            self.count = count 
        if limit is not APIHelper.SKIP:
            self.limit = limit 
        if offset is not APIHelper.SKIP:
            self.offset = offset 
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
        count = dictionary.get("count") if dictionary.get("count") else APIHelper.SKIP
        limit = dictionary.get("limit") if dictionary.get("limit") else APIHelper.SKIP
        offset = dictionary.get("offset") if dictionary.get("offset") else APIHelper.SKIP
        data = None
        if dictionary.get('data') is not None:
            data = [LinkResponse.from_dictionary(x) for x in dictionary.get('data')]
        else:
            data = APIHelper.SKIP
        # Return an object of this model
        return cls(count,
                   limit,
                   offset,
                   data)
