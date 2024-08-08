# -*- coding: utf-8 -*-

"""
lob

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
import dateutil.parser

from lob.api_helper import APIHelper
from lob.models.address_us import AddressUs
from lob.models.thumbnail import Thumbnail
from lob.models.tracking_event_certified import TrackingEventCertified


class SelfMailer(object):

    """Implementation of the 'self_mailer' model.

    TODO: type model description here.

    Attributes:
        description (str): An internal description that identifies this
            resource. Must be no longer than 255 characters.
        metadata (Dict[str, str]): Use metadata to store custom information
            for tagging and labeling back to your internal systems. Must be an
            object with up to 20 key-value pairs. Keys must be at most 40
            characters and values must be at most 500 characters. Neither can
            contain the characters `"` and `\`. i.e. '{"customer_id" :
            "NEWYORK2015"}' Nested objects are not supported.  See
            [Metadata](#section/Metadata) for more information.
        mail_type (MailTypeEnum): TODO: type description here.
        merge_variables (object): You can input a merge variable payload
            object to your template to render dynamic content. For example, if
            you have a template like: `{{variable_name}}`, pass in
            `{"variable_name": "Harry"}` to render `Harry`. `merge_variables`
            must be an object. Any type of value is accepted as long as the
            object is valid JSON; you can use `strings`, `numbers`,
            `booleans`, `arrays`, `objects`, or `null`. The max length of the
            object is 25,000 characters. If you call `JSON.stringify` on your
            object, it can be no longer than 25,000 characters. Your variable
            names cannot contain any whitespace or any of the following
            special characters: `!`, `"`, `#`, `%`, `&`, `'`, `(`, `)`, `*`,
            `+`, `,`, `/`, `;`, `<`, `=`, `>`, `@`, `[`, `\`, `]`, `^`, `` `
            ``, `{`, `|`, `}`, `~`. More instructions can be found in <a
            href="https://help.lob.com/print-and-mail/designing-mail-creatives/
            dynamic-personalization#using-html-and-merge-variables-10"
            target="_blank">our guide to using html and merge variables</a>.
            Depending on your <a
            href="https://dashboard.lob.com/#/settings/account"
            target="_blank">Merge Variable strictness</a> setting, if you
            define variables in your HTML but do not pass them here, you will
            either receive an error or the variable will render as an empty
            string.
        send_date (object): TODO: type description here.
        size (SelfMailerSizeEnum): TODO: type description here.
        to (object): TODO: type description here.
        carrier (str): TODO: type description here.
        thumbnails (List[Thumbnail]): TODO: type description here.
        expected_delivery_date (date): A date in YYYY-MM-DD format of the
            mailpiece's expected delivery date based on its `send_date`.
        date_created (datetime): A timestamp in ISO 8601 format of the date
            the resource was created.
        date_modified (datetime): A timestamp in ISO 8601 format of the date
            the resource was last modified.
        deleted (bool): Only returned if the resource has been successfully
            deleted.
        mfrom (AddressUs): TODO: type description here.
        id (str): Unique identifier prefixed with `sfm_`.
        outside_template_id (str): The unique ID of the HTML template used for
            the outside of the self mailer.
        inside_template_id (str): The unique ID of the HTML template used for
            the inside of the self mailer.
        outside_template_version_id (str): The unique ID of the specific
            version of the HTML template used for the outside of the self
            mailer.
        inside_template_version_id (str): The unique ID of the specific
            version of the HTML template used for the inside of the self
            mailer.
        object (Object11Enum): TODO: type description here.
        tracking_events (List[TrackingEventCertified]): An array of certified
            tracking events ordered by ascending `time`. Not populated in test
            mode.
        use_type (object): TODO: type description here.
        url (str): A [signed link](#section/Asset-URLs) served over HTTPS. The
            link returned will expire in 30 days to prevent mis-sharing. Each
            time a GET request is initiated, a new signed URL will be
            generated.
        fsc (bool): This is in beta. Contact support@lob.com or your account
            contact to learn more. Not available for `11x9_bifold` self-mailer
            size.
        status (ThestatusofthebuckslipEnum): TODO: type description here.
        failure_reason (str): A string describing the reason for failure if
            the self mailer failed to render.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "to": 'to',
        "carrier": 'carrier',
        "id": 'id',
        "use_type": 'use_type',
        "url": 'url',
        "description": 'description',
        "metadata": 'metadata',
        "mail_type": 'mail_type',
        "merge_variables": 'merge_variables',
        "send_date": 'send_date',
        "size": 'size',
        "thumbnails": 'thumbnails',
        "expected_delivery_date": 'expected_delivery_date',
        "date_created": 'date_created',
        "date_modified": 'date_modified',
        "deleted": 'deleted',
        "mfrom": 'from',
        "outside_template_id": 'outside_template_id',
        "inside_template_id": 'inside_template_id',
        "outside_template_version_id": 'outside_template_version_id',
        "inside_template_version_id": 'inside_template_version_id',
        "object": 'object',
        "tracking_events": 'tracking_events',
        "fsc": 'fsc',
        "status": 'status',
        "failure_reason": 'failure_reason'
    }

    _optionals = [
        'description',
        'metadata',
        'mail_type',
        'merge_variables',
        'send_date',
        'size',
        'thumbnails',
        'expected_delivery_date',
        'date_created',
        'date_modified',
        'deleted',
        'mfrom',
        'outside_template_id',
        'inside_template_id',
        'outside_template_version_id',
        'inside_template_version_id',
        'object',
        'tracking_events',
        'fsc',
        'status',
        'failure_reason',
    ]

    _nullables = [
        'description',
        'merge_variables',
        'outside_template_id',
        'inside_template_id',
        'outside_template_version_id',
        'inside_template_version_id',
        'failure_reason',
    ]

    def __init__(self,
                 to=None,
                 id=None,
                 use_type=None,
                 url=None,
                 description=APIHelper.SKIP,
                 metadata=APIHelper.SKIP,
                 mail_type=APIHelper.SKIP,
                 merge_variables=APIHelper.SKIP,
                 send_date=APIHelper.SKIP,
                 size=APIHelper.SKIP,
                 thumbnails=APIHelper.SKIP,
                 expected_delivery_date=APIHelper.SKIP,
                 date_created=APIHelper.SKIP,
                 date_modified=APIHelper.SKIP,
                 deleted=APIHelper.SKIP,
                 mfrom=APIHelper.SKIP,
                 outside_template_id=APIHelper.SKIP,
                 inside_template_id=APIHelper.SKIP,
                 outside_template_version_id=APIHelper.SKIP,
                 inside_template_version_id=APIHelper.SKIP,
                 object=APIHelper.SKIP,
                 tracking_events=APIHelper.SKIP,
                 fsc=False,
                 status=APIHelper.SKIP,
                 failure_reason=APIHelper.SKIP):
        """Constructor for the SelfMailer class"""

        # Initialize members of the class
        if description is not APIHelper.SKIP:
            self.description = description 
        if metadata is not APIHelper.SKIP:
            self.metadata = metadata 
        if mail_type is not APIHelper.SKIP:
            self.mail_type = mail_type 
        if merge_variables is not APIHelper.SKIP:
            self.merge_variables = merge_variables 
        if send_date is not APIHelper.SKIP:
            self.send_date = send_date 
        if size is not APIHelper.SKIP:
            self.size = size 
        self.to = to 
        self.carrier = 'USPS' 
        if thumbnails is not APIHelper.SKIP:
            self.thumbnails = thumbnails 
        if expected_delivery_date is not APIHelper.SKIP:
            self.expected_delivery_date = expected_delivery_date 
        if date_created is not APIHelper.SKIP:
            self.date_created = APIHelper.apply_datetime_converter(date_created, APIHelper.RFC3339DateTime) if date_created else None 
        if date_modified is not APIHelper.SKIP:
            self.date_modified = APIHelper.apply_datetime_converter(date_modified, APIHelper.RFC3339DateTime) if date_modified else None 
        if deleted is not APIHelper.SKIP:
            self.deleted = deleted 
        if mfrom is not APIHelper.SKIP:
            self.mfrom = mfrom 
        self.id = id 
        if outside_template_id is not APIHelper.SKIP:
            self.outside_template_id = outside_template_id 
        if inside_template_id is not APIHelper.SKIP:
            self.inside_template_id = inside_template_id 
        if outside_template_version_id is not APIHelper.SKIP:
            self.outside_template_version_id = outside_template_version_id 
        if inside_template_version_id is not APIHelper.SKIP:
            self.inside_template_version_id = inside_template_version_id 
        if object is not APIHelper.SKIP:
            self.object = object 
        if tracking_events is not APIHelper.SKIP:
            self.tracking_events = tracking_events 
        self.use_type = use_type 
        self.url = url 
        self.fsc = fsc 
        if status is not APIHelper.SKIP:
            self.status = status 
        if failure_reason is not APIHelper.SKIP:
            self.failure_reason = failure_reason 

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
        to = dictionary.get("to") if dictionary.get("to") else None
        id = dictionary.get("id") if dictionary.get("id") else None
        use_type = dictionary.get("use_type") if dictionary.get("use_type") else None
        url = dictionary.get("url") if dictionary.get("url") else None
        description = dictionary.get("description") if "description" in dictionary.keys() else APIHelper.SKIP
        metadata = dictionary.get("metadata") if dictionary.get("metadata") else APIHelper.SKIP
        mail_type = dictionary.get("mail_type") if dictionary.get("mail_type") else APIHelper.SKIP
        merge_variables = dictionary.get("merge_variables") if "merge_variables" in dictionary.keys() else APIHelper.SKIP
        send_date = dictionary.get("send_date") if dictionary.get("send_date") else APIHelper.SKIP
        size = dictionary.get("size") if dictionary.get("size") else APIHelper.SKIP
        thumbnails = None
        if dictionary.get('thumbnails') is not None:
            thumbnails = [Thumbnail.from_dictionary(x) for x in dictionary.get('thumbnails')]
        else:
            thumbnails = APIHelper.SKIP
        expected_delivery_date = dateutil.parser.parse(dictionary.get('expected_delivery_date')).date() if dictionary.get('expected_delivery_date') else APIHelper.SKIP
        date_created = APIHelper.RFC3339DateTime.from_value(dictionary.get("date_created")).datetime if dictionary.get("date_created") else APIHelper.SKIP
        date_modified = APIHelper.RFC3339DateTime.from_value(dictionary.get("date_modified")).datetime if dictionary.get("date_modified") else APIHelper.SKIP
        deleted = dictionary.get("deleted") if "deleted" in dictionary.keys() else APIHelper.SKIP
        mfrom = AddressUs.from_dictionary(dictionary.get('from')) if 'from' in dictionary.keys() else APIHelper.SKIP
        outside_template_id = dictionary.get("outside_template_id") if "outside_template_id" in dictionary.keys() else APIHelper.SKIP
        inside_template_id = dictionary.get("inside_template_id") if "inside_template_id" in dictionary.keys() else APIHelper.SKIP
        outside_template_version_id = dictionary.get("outside_template_version_id") if "outside_template_version_id" in dictionary.keys() else APIHelper.SKIP
        inside_template_version_id = dictionary.get("inside_template_version_id") if "inside_template_version_id" in dictionary.keys() else APIHelper.SKIP
        object = dictionary.get("object") if dictionary.get("object") else APIHelper.SKIP
        tracking_events = None
        if dictionary.get('tracking_events') is not None:
            tracking_events = [TrackingEventCertified.from_dictionary(x) for x in dictionary.get('tracking_events')]
        else:
            tracking_events = APIHelper.SKIP
        fsc = dictionary.get("fsc") if dictionary.get("fsc") else False
        status = dictionary.get("status") if dictionary.get("status") else APIHelper.SKIP
        failure_reason = dictionary.get("failure_reason") if "failure_reason" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(to,
                   id,
                   use_type,
                   url,
                   description,
                   metadata,
                   mail_type,
                   merge_variables,
                   send_date,
                   size,
                   thumbnails,
                   expected_delivery_date,
                   date_created,
                   date_modified,
                   deleted,
                   mfrom,
                   outside_template_id,
                   inside_template_id,
                   outside_template_version_id,
                   inside_template_version_id,
                   object,
                   tracking_events,
                   fsc,
                   status,
                   failure_reason)
