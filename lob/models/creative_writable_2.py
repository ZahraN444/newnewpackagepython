# -*- coding: utf-8 -*-

"""
lob

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from lob.api_helper import APIHelper
from lob.models.details_4 import Details4


class CreativeWritable2(object):

    """Implementation of the 'creative_writable2' model.

    TODO: type model description here.

    Attributes:
        resource_type (str): Mailpiece type for the creative
        campaign_id (str): Unique identifier prefixed with `cmp_`.
        inside (object): TODO: type description here.
        outside (object): TODO: type description here.
        details (Details4): TODO: type description here.
        mfrom (object): TODO: type description here.
        description (str): An internal description that identifies this
            resource. Must be no longer than 255 characters.
        metadata (Dict[str, str]): Use metadata to store custom information
            for tagging and labeling back to your internal systems. Must be an
            object with up to 20 key-value pairs. Keys must be at most 40
            characters and values must be at most 500 characters. Neither can
            contain the characters `"` and `\`. i.e. '{"customer_id" :
            "NEWYORK2015"}' Nested objects are not supported.  See
            [Metadata](#section/Metadata) for more information.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "resource_type": 'resource_type',
        "campaign_id": 'campaign_id',
        "inside": 'inside',
        "outside": 'outside',
        "details": 'details',
        "mfrom": 'from',
        "description": 'description',
        "metadata": 'metadata'
    }

    _optionals = [
        'mfrom',
        'description',
        'metadata',
    ]

    _nullables = [
        'description',
    ]

    def __init__(self,
                 campaign_id=None,
                 inside=None,
                 outside=None,
                 details=None,
                 mfrom=APIHelper.SKIP,
                 description=APIHelper.SKIP,
                 metadata=APIHelper.SKIP):
        """Constructor for the CreativeWritable2 class"""

        # Initialize members of the class
        self.resource_type = 'self_mailer' 
        self.campaign_id = campaign_id 
        self.inside = inside 
        self.outside = outside 
        self.details = details 
        if mfrom is not APIHelper.SKIP:
            self.mfrom = mfrom 
        if description is not APIHelper.SKIP:
            self.description = description 
        if metadata is not APIHelper.SKIP:
            self.metadata = metadata 

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
        campaign_id = dictionary.get("campaign_id") if dictionary.get("campaign_id") else None
        inside = dictionary.get("inside") if dictionary.get("inside") else None
        outside = dictionary.get("outside") if dictionary.get("outside") else None
        details = Details4.from_dictionary(dictionary.get('details')) if dictionary.get('details') else None
        mfrom = dictionary.get("from") if dictionary.get("from") else APIHelper.SKIP
        description = dictionary.get("description") if "description" in dictionary.keys() else APIHelper.SKIP
        metadata = dictionary.get("metadata") if dictionary.get("metadata") else APIHelper.SKIP
        # Return an object of this model
        return cls(campaign_id,
                   inside,
                   outside,
                   details,
                   mfrom,
                   description,
                   metadata)