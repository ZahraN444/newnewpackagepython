# -*- coding: utf-8 -*-

"""
lob

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from lob.api_helper import APIHelper


class UploadsExportsResponse(object):

    """Implementation of the 'UploadsExportsResponse' model.

    TODO: type model description here.

    Attributes:
        id (str): Unique identifier prefixed with `ex_`.
        date_created (datetime): A timestamp in ISO 8601 format of the date
            the export was created
        date_modified (datetime): A timestamp in ISO 8601 format of the date
            the export was last modified
        deleted (bool): Returns as `true` if the resource has been
            successfully deleted.
        s_3_url (str): The URL for the generated export file.
        state (StateEnum): TODO: type description here.
        mtype (Type1Enum): TODO: type description here.
        upload_id (str): Unique identifier prefixed with `upl_`.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "date_created": 'dateCreated',
        "date_modified": 'dateModified',
        "deleted": 'deleted',
        "s_3_url": 's3Url',
        "state": 'state',
        "mtype": 'type',
        "upload_id": 'uploadId'
    }

    def __init__(self,
                 id=None,
                 date_created=None,
                 date_modified=None,
                 deleted=None,
                 s_3_url=None,
                 state=None,
                 mtype=None,
                 upload_id=None):
        """Constructor for the UploadsExportsResponse class"""

        # Initialize members of the class
        self.id = id 
        self.date_created = APIHelper.apply_datetime_converter(date_created, APIHelper.RFC3339DateTime) if date_created else None 
        self.date_modified = APIHelper.apply_datetime_converter(date_modified, APIHelper.RFC3339DateTime) if date_modified else None 
        self.deleted = deleted 
        self.s_3_url = s_3_url 
        self.state = state 
        self.mtype = mtype 
        self.upload_id = upload_id 

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
        date_created = APIHelper.RFC3339DateTime.from_value(dictionary.get("dateCreated")).datetime if dictionary.get("dateCreated") else None
        date_modified = APIHelper.RFC3339DateTime.from_value(dictionary.get("dateModified")).datetime if dictionary.get("dateModified") else None
        deleted = dictionary.get("deleted") if "deleted" in dictionary.keys() else None
        s_3_url = dictionary.get("s3Url") if dictionary.get("s3Url") else None
        state = dictionary.get("state") if dictionary.get("state") else None
        mtype = dictionary.get("type") if dictionary.get("type") else None
        upload_id = dictionary.get("uploadId") if dictionary.get("uploadId") else None
        # Return an object of this model
        return cls(id,
                   date_created,
                   date_modified,
                   deleted,
                   s_3_url,
                   state,
                   mtype,
                   upload_id)
