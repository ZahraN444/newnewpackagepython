# -*- coding: utf-8 -*-

"""
lob

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from lob.api_helper import APIHelper
from lob.models.resource_enum import ResourceEnum


class EventType(object):

    """Implementation of the 'event_type' model.

    TODO: type model description here.

    Attributes:
        id (PostcardTypesEnum | SelfMailerTypesEnum | LetterTypesEnum |
            CheckTypesEnum | AddressTypesEnum | BankAccountTypesEnum): TODO:
            type description here.
        enabled_for_test (bool): Value is `true` if the event type is enabled
            in both the test and live environments and `false` if it is only
            enabled in the live environment.
        resource (ResourceEnum): TODO: type description here.
        object (str): Value is resource type.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "enabled_for_test": 'enabled_for_test',
        "resource": 'resource',
        "object": 'object'
    }

    def __init__(self,
                 id=None,
                 enabled_for_test=None,
                 resource=None):
        """Constructor for the EventType class"""

        # Initialize members of the class
        self.id = id 
        self.enabled_for_test = enabled_for_test 
        self.resource = resource 
        self.object = 'event_type' 

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
        id = APIHelper.deserialize_union_type(UnionTypeLookUp.get('EventTypeId'), dictionary.get('id'), False) if dictionary.get('id') is not None else None
        enabled_for_test = dictionary.get("enabled_for_test") if "enabled_for_test" in dictionary.keys() else None
        resource = dictionary.get("resource") if dictionary.get("resource") else None
        # Return an object of this model
        return cls(id,
                   enabled_for_test,
                   resource)

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
            return UnionTypeLookUp.get('EventTypeId').validate(dictionary.id).is_valid \
                and APIHelper.is_valid_type(value=dictionary.enabled_for_test,
                                            type_callable=lambda value: isinstance(value, bool)) \
                and APIHelper.is_valid_type(value=dictionary.resource,
                                            type_callable=lambda value: ResourceEnum.validate(value)) \
                and APIHelper.is_valid_type(value=dictionary.object,
                                            type_callable=lambda value: isinstance(value, str))

        if not isinstance(dictionary, dict):
            return False

        return UnionTypeLookUp.get('EventTypeId').validate(dictionary.get('id')).is_valid \
            and APIHelper.is_valid_type(value=dictionary.get('enabled_for_test'),
                                        type_callable=lambda value: isinstance(value, bool)) \
            and APIHelper.is_valid_type(value=dictionary.get('resource'),
                                        type_callable=lambda value: ResourceEnum.validate(value)) \
            and APIHelper.is_valid_type(value=dictionary.get('object'),
                                        type_callable=lambda value: isinstance(value, str))
