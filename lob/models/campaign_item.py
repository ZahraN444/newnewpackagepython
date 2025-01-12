# -*- coding: utf-8 -*-

"""
lob

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from lob.api_helper import APIHelper


class CampaignItem(object):

    """Implementation of the 'campaign_item' model.

    TODO: type model description here.

    Attributes:
        billing_group_id (str): Unique identifier prefixed with `bg_`.
        name (str): Name of the campaign.
        description (str): An internal description that identifies this
            resource. Must be no longer than 255 characters.
        schedule_type (str): How the campaign should be scheduled. Only value
            available today is `immediate`.
        target_delivery_date (datetime): If `schedule_type` is
            `target_delivery_date`, provide a targeted delivery date for mail
            pieces in this campaign.
        send_date (datetime): If `schedule_type` is `scheduled_send_date`,
            provide a date to send this campaign.
        cancel_window_campaign_minutes (int): A window, in minutes, within
            which the campaign can be canceled.
        metadata (Dict[str, str]): Use metadata to store custom information
            for tagging and labeling back to your internal systems. Must be an
            object with up to 20 key-value pairs. Keys must be at most 40
            characters and values must be at most 500 characters. Neither can
            contain the characters `"` and `\`. i.e. '{"customer_id" :
            "NEWYORK2015"}' Nested objects are not supported.  See
            [Metadata](#section/Metadata) for more information.
        use_type (object): TODO: type description here.
        auto_cancel_if_ncoa (bool): Whether or not a mail piece should be
            automatically canceled and not sent if the address is updated via
            NCOA.
        id (str): Unique identifier prefixed with `cmp_`.
        is_draft (bool): Whether or not the campaign is still a draft.
        creatives (List[object]): An array of creatives that have been
            associated with this campaign.
        uploads (List[object]): A single-element array containing the upload
            object that is assocated with this campaign.
        object (str): Value is resource type.
        date_created (datetime): A timestamp in ISO 8601 format of the date
            the resource was created.
        date_modified (datetime): A timestamp in ISO 8601 format of the date
            the resource was last modified.
        deleted (bool): Only returned if the resource has been successfully
            deleted.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "description": 'description',
        "schedule_type": 'schedule_type',
        "use_type": 'use_type',
        "auto_cancel_if_ncoa": 'auto_cancel_if_ncoa',
        "id": 'id',
        "is_draft": 'is_draft',
        "creatives": 'creatives',
        "uploads": 'uploads',
        "object": 'object',
        "date_created": 'date_created',
        "date_modified": 'date_modified',
        "billing_group_id": 'billing_group_id',
        "target_delivery_date": 'target_delivery_date',
        "send_date": 'send_date',
        "cancel_window_campaign_minutes": 'cancel_window_campaign_minutes',
        "metadata": 'metadata',
        "deleted": 'deleted'
    }

    _optionals = [
        'billing_group_id',
        'target_delivery_date',
        'send_date',
        'cancel_window_campaign_minutes',
        'metadata',
        'deleted',
    ]

    _nullables = [
        'billing_group_id',
        'description',
        'target_delivery_date',
        'send_date',
        'cancel_window_campaign_minutes',
    ]

    def __init__(self,
                 name=None,
                 description=None,
                 use_type=None,
                 auto_cancel_if_ncoa=None,
                 id=None,
                 is_draft=None,
                 creatives=None,
                 uploads=None,
                 date_created=None,
                 date_modified=None,
                 billing_group_id=APIHelper.SKIP,
                 target_delivery_date=APIHelper.SKIP,
                 send_date=APIHelper.SKIP,
                 cancel_window_campaign_minutes=APIHelper.SKIP,
                 metadata=APIHelper.SKIP,
                 deleted=APIHelper.SKIP):
        """Constructor for the CampaignItem class"""

        # Initialize members of the class
        if billing_group_id is not APIHelper.SKIP:
            self.billing_group_id = billing_group_id 
        self.name = name 
        self.description = description 
        self.schedule_type = 'immediate' 
        if target_delivery_date is not APIHelper.SKIP:
            self.target_delivery_date = APIHelper.apply_datetime_converter(target_delivery_date, APIHelper.RFC3339DateTime) if target_delivery_date else None 
        if send_date is not APIHelper.SKIP:
            self.send_date = APIHelper.apply_datetime_converter(send_date, APIHelper.RFC3339DateTime) if send_date else None 
        if cancel_window_campaign_minutes is not APIHelper.SKIP:
            self.cancel_window_campaign_minutes = cancel_window_campaign_minutes 
        if metadata is not APIHelper.SKIP:
            self.metadata = metadata 
        self.use_type = use_type 
        self.auto_cancel_if_ncoa = auto_cancel_if_ncoa 
        self.id = id 
        self.is_draft = is_draft 
        self.creatives = creatives 
        self.uploads = uploads 
        self.object = 'campaign' 
        self.date_created = APIHelper.apply_datetime_converter(date_created, APIHelper.RFC3339DateTime) if date_created else None 
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
        name = dictionary.get("name") if dictionary.get("name") else None
        description = dictionary.get("description") if dictionary.get("description") else None
        use_type = dictionary.get("use_type") if dictionary.get("use_type") else None
        auto_cancel_if_ncoa = dictionary.get("auto_cancel_if_ncoa") if "auto_cancel_if_ncoa" in dictionary.keys() else None
        id = dictionary.get("id") if dictionary.get("id") else None
        is_draft = dictionary.get("is_draft") if "is_draft" in dictionary.keys() else None
        creatives = dictionary.get("creatives") if dictionary.get("creatives") else None
        uploads = dictionary.get("uploads") if dictionary.get("uploads") else None
        date_created = APIHelper.RFC3339DateTime.from_value(dictionary.get("date_created")).datetime if dictionary.get("date_created") else None
        date_modified = APIHelper.RFC3339DateTime.from_value(dictionary.get("date_modified")).datetime if dictionary.get("date_modified") else None
        billing_group_id = dictionary.get("billing_group_id") if "billing_group_id" in dictionary.keys() else APIHelper.SKIP
        if 'target_delivery_date' in dictionary.keys():
            target_delivery_date = APIHelper.RFC3339DateTime.from_value(dictionary.get("target_delivery_date")).datetime if dictionary.get("target_delivery_date") else None
        else:
            target_delivery_date = APIHelper.SKIP
        if 'send_date' in dictionary.keys():
            send_date = APIHelper.RFC3339DateTime.from_value(dictionary.get("send_date")).datetime if dictionary.get("send_date") else None
        else:
            send_date = APIHelper.SKIP
        cancel_window_campaign_minutes = dictionary.get("cancel_window_campaign_minutes") if "cancel_window_campaign_minutes" in dictionary.keys() else APIHelper.SKIP
        metadata = dictionary.get("metadata") if dictionary.get("metadata") else APIHelper.SKIP
        deleted = dictionary.get("deleted") if "deleted" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(name,
                   description,
                   use_type,
                   auto_cancel_if_ncoa,
                   id,
                   is_draft,
                   creatives,
                   uploads,
                   date_created,
                   date_modified,
                   billing_group_id,
                   target_delivery_date,
                   send_date,
                   cancel_window_campaign_minutes,
                   metadata,
                   deleted)

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

        if isinstance(dictionary, cls):
            return APIHelper.is_valid_type(value=dictionary.name,
                                           type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.description,
                                            type_callable=lambda value: isinstance(value, str),
                                            is_value_nullable=True) \
                and APIHelper.is_valid_type(value=dictionary.schedule_type,
                                            type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.use_type,
                                            type_callable=lambda value: isinstance(value, object)) \
                and APIHelper.is_valid_type(value=dictionary.auto_cancel_if_ncoa,
                                            type_callable=lambda value: isinstance(value, bool)) \
                and APIHelper.is_valid_type(value=dictionary.id,
                                            type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.is_draft,
                                            type_callable=lambda value: isinstance(value, bool)) \
                and APIHelper.is_valid_type(value=dictionary.creatives,
                                            type_callable=lambda value: isinstance(value, object)) \
                and APIHelper.is_valid_type(value=dictionary.uploads,
                                            type_callable=lambda value: isinstance(value, object)) \
                and APIHelper.is_valid_type(value=dictionary.object,
                                            type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.date_created,
                                            type_callable=lambda value: isinstance(value, APIHelper.RFC3339DateTime)) \
                and APIHelper.is_valid_type(value=dictionary.date_modified,
                                            type_callable=lambda value: isinstance(value, APIHelper.RFC3339DateTime))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('name'),
                                       type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('description'),
                                        type_callable=lambda value: isinstance(value, str),
                                        is_value_nullable=True) \
            and APIHelper.is_valid_type(value=dictionary.get('schedule_type'),
                                        type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('use_type'),
                                        type_callable=lambda value: isinstance(value, object)) \
            and APIHelper.is_valid_type(value=dictionary.get('auto_cancel_if_ncoa'),
                                        type_callable=lambda value: isinstance(value, bool)) \
            and APIHelper.is_valid_type(value=dictionary.get('id'),
                                        type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('is_draft'),
                                        type_callable=lambda value: isinstance(value, bool)) \
            and APIHelper.is_valid_type(value=dictionary.get('creatives'),
                                        type_callable=lambda value: isinstance(value, object)) \
            and APIHelper.is_valid_type(value=dictionary.get('uploads'),
                                        type_callable=lambda value: isinstance(value, object)) \
            and APIHelper.is_valid_type(value=dictionary.get('object'),
                                        type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('date_created'),
                                        type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('date_modified'),
                                        type_callable=lambda value: isinstance(value, str))
