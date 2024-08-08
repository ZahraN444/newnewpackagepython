# -*- coding: utf-8 -*-

"""
lob

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from lob.api_helper import APIHelper
from lob.models.template_version import TemplateVersion


class Template(object):

    """Implementation of the 'template' model.

    TODO: type model description here.

    Attributes:
        description (str): An internal description that identifies this
            resource. Must be no longer than 255 characters.
        id (str): Unique identifier prefixed with `tmpl_`. ID of a saved [HTML
            template](#section/HTML-Templates).
        versions (List[TemplateVersion]): An array of all non-deleted [version
            objects](#tag/Template-Versions) associated with the template.
        published_version (TemplateVersion): TODO: type description here.
        object (Object12Enum): TODO: type description here.
        metadata (Dict[str, str]): Use metadata to store custom information
            for tagging and labeling back to your internal systems. Must be an
            object with up to 20 key-value pairs. Keys must be at most 40
            characters and values must be at most 500 characters. Neither can
            contain the characters `"` and `\`. i.e. '{"customer_id" :
            "NEWYORK2015"}' Nested objects are not supported.  See
            [Metadata](#section/Metadata) for more information.
        date_created (datetime): A timestamp in ISO 8601 format of the date
            the resource was created.
        date_modified (datetime): A timestamp in ISO 8601 format of the date
            the resource was last modified.
        deleted (bool): Only returned if the resource has been successfully
            deleted.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "versions": 'versions',
        "published_version": 'published_version',
        "description": 'description',
        "object": 'object',
        "metadata": 'metadata',
        "date_created": 'date_created',
        "date_modified": 'date_modified',
        "deleted": 'deleted'
    }

    _optionals = [
        'description',
        'object',
        'metadata',
        'date_created',
        'date_modified',
        'deleted',
    ]

    _nullables = [
        'description',
    ]

    def __init__(self,
                 id=None,
                 versions=None,
                 published_version=None,
                 description=APIHelper.SKIP,
                 object=APIHelper.SKIP,
                 metadata=APIHelper.SKIP,
                 date_created=APIHelper.SKIP,
                 date_modified=APIHelper.SKIP,
                 deleted=APIHelper.SKIP):
        """Constructor for the Template class"""

        # Initialize members of the class
        if description is not APIHelper.SKIP:
            self.description = description 
        self.id = id 
        self.versions = versions 
        self.published_version = published_version 
        if object is not APIHelper.SKIP:
            self.object = object 
        if metadata is not APIHelper.SKIP:
            self.metadata = metadata 
        if date_created is not APIHelper.SKIP:
            self.date_created = APIHelper.apply_datetime_converter(date_created, APIHelper.RFC3339DateTime) if date_created else None 
        if date_modified is not APIHelper.SKIP:
            self.date_modified = APIHelper.apply_datetime_converter(date_modified, APIHelper.RFC3339DateTime) if date_modified else None 
        if deleted is not APIHelper.SKIP:
            self.deleted = deleted 

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
        id = dictionary.get("id") if dictionary.get("id") else None
        versions = None
        if dictionary.get('versions') is not None:
            versions = [TemplateVersion.from_dictionary(x) for x in dictionary.get('versions')]
        published_version = TemplateVersion.from_dictionary(dictionary.get('published_version')) if dictionary.get('published_version') else None
        description = dictionary.get("description") if "description" in dictionary.keys() else APIHelper.SKIP
        object = dictionary.get("object") if dictionary.get("object") else APIHelper.SKIP
        metadata = dictionary.get("metadata") if dictionary.get("metadata") else APIHelper.SKIP
        date_created = APIHelper.RFC3339DateTime.from_value(dictionary.get("date_created")).datetime if dictionary.get("date_created") else APIHelper.SKIP
        date_modified = APIHelper.RFC3339DateTime.from_value(dictionary.get("date_modified")).datetime if dictionary.get("date_modified") else APIHelper.SKIP
        deleted = dictionary.get("deleted") if "deleted" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   versions,
                   published_version,
                   description,
                   object,
                   metadata,
                   date_created,
                   date_modified,
                   deleted)
