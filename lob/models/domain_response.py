# -*- coding: utf-8 -*-

"""
lob

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from lob.api_helper import APIHelper


class DomainResponse(object):

    """Implementation of the 'domain_response' model.

    TODO: type model description here.

    Attributes:
        id (str): Unique identifier for a domain.
        domain (str): The registered domain/hostname.
        account_id (str): Unique identifier associated with the account the
            domain is registered for.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "domain": 'domain',
        "account_id": 'account_id'
    }

    _optionals = [
        'id',
        'domain',
        'account_id',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 domain=APIHelper.SKIP,
                 account_id=APIHelper.SKIP):
        """Constructor for the DomainResponse class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if domain is not APIHelper.SKIP:
            self.domain = domain 
        if account_id is not APIHelper.SKIP:
            self.account_id = account_id 

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
        domain = dictionary.get("domain") if dictionary.get("domain") else APIHelper.SKIP
        account_id = dictionary.get("account_id") if dictionary.get("account_id") else APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   domain,
                   account_id)
