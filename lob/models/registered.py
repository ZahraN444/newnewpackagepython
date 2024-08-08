# -*- coding: utf-8 -*-

"""
lob

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
import dateutil.parser

from lob.api_helper import APIHelper
from lob.models.thumbnail import Thumbnail
from lob.models.tracking_event_normal import TrackingEventNormal


class Registered(object):

    """Implementation of the 'registered' model.

    TODO: type model description here.

    Attributes:
        extra_service (str): Add an extra service to your letter. See <a
            href="https://www.lob.com/pricing/print-mail#compare"
            target="_blank">pricing</a> for extra costs incurred.   *
            registered - provides tracking and confirmation for international
            addresses
        tracking_number (str): The tracking number will appear here when it
            becomes available. Dummy tracking numbers are not created in test
            mode.
        tracking_events (List[TrackingEventNormal]): Tracking events are not
            populated for registered letters.
        return_address (object): TODO: type description here.
        description (str): An internal description that identifies this
            resource. Must be no longer than 255 characters.
        metadata (Dict[str, str]): Use metadata to store custom information
            for tagging and labeling back to your internal systems. Must be an
            object with up to 20 key-value pairs. Keys must be at most 40
            characters and values must be at most 500 characters. Neither can
            contain the characters `"` and `\`. i.e. '{"customer_id" :
            "NEWYORK2015"}' Nested objects are not supported.  See
            [Metadata](#section/Metadata) for more information.
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
        mail_type (MailTypeEnum): TODO: type description here.
        color (bool): Set this key to `true` if you would like to print in
            color. Set to `false` if you would like to print in black and
            white.
        double_sided (bool): Set this attribute to `true` for double sided
            printing, or `false` for for single sided printing. Defaults to
            `true`.
        address_placement (AddressPlacementEnum): TODO: type description
            here.
        return_envelope (object): TODO: type description here.
        perforated_page (int): Required if `return_envelope` is `true`. The
            number of the page that should be perforated for use with the
            return envelope. Must be greater than or equal to `1`. The blank
            page added by `address_placement=insert_blank_page` will be
            ignored when considering the perforated page number. To see how
            perforation will impact your letter design, view our <a
            href="https://s3-us-west-2.amazonaws.com/public.lob.com/assets/temp
            lates/letter_perf_template.pdf" target="_blank">perforation
            guide</a>.
        custom_envelope (object): TODO: type description here.
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
        mfrom (object): TODO: type description here.
        url (str): A [signed link](#section/Asset-URLs) served over HTTPS. The
            link returned will expire in 30 days to prevent mis-sharing. Each
            time a GET request is initiated, a new signed URL will be
            generated.
        id (str): Unique identifier prefixed with `ltr_`.
        template_id (str): TODO: type description here.
        template_version_id (str): TODO: type description here.
        campaign_id (str): The unique ID of the associated campaign if the
            resource was generated from a campaign.
        use_type (object): TODO: type description here.
        fsc (bool): This is in beta. Contact support@lob.com or your account
            contact to learn more. Not available for `A4` letter size.
        status (ThestatusofthebuckslipEnum): TODO: type description here.
        failure_reason (str): A string describing the reason for failure if
            the letter failed to render.
        object (Object8Enum): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "extra_service": 'extra_service',
        "color": 'color',
        "to": 'to',
        "carrier": 'carrier',
        "mfrom": 'from',
        "id": 'id',
        "use_type": 'use_type',
        "tracking_number": 'tracking_number',
        "tracking_events": 'tracking_events',
        "return_address": 'return_address',
        "description": 'description',
        "metadata": 'metadata',
        "merge_variables": 'merge_variables',
        "send_date": 'send_date',
        "mail_type": 'mail_type',
        "double_sided": 'double_sided',
        "address_placement": 'address_placement',
        "return_envelope": 'return_envelope',
        "perforated_page": 'perforated_page',
        "custom_envelope": 'custom_envelope',
        "thumbnails": 'thumbnails',
        "expected_delivery_date": 'expected_delivery_date',
        "date_created": 'date_created',
        "date_modified": 'date_modified',
        "deleted": 'deleted',
        "url": 'url',
        "template_id": 'template_id',
        "template_version_id": 'template_version_id',
        "campaign_id": 'campaign_id',
        "fsc": 'fsc',
        "status": 'status',
        "failure_reason": 'failure_reason',
        "object": 'object'
    }

    _optionals = [
        'tracking_number',
        'tracking_events',
        'return_address',
        'description',
        'metadata',
        'merge_variables',
        'send_date',
        'mail_type',
        'double_sided',
        'address_placement',
        'return_envelope',
        'perforated_page',
        'custom_envelope',
        'thumbnails',
        'expected_delivery_date',
        'date_created',
        'date_modified',
        'deleted',
        'url',
        'template_id',
        'template_version_id',
        'campaign_id',
        'fsc',
        'status',
        'failure_reason',
        'object',
    ]

    _nullables = [
        'tracking_number',
        'description',
        'merge_variables',
        'perforated_page',
        'campaign_id',
        'failure_reason',
    ]

    def __init__(self,
                 color=None,
                 to=None,
                 mfrom=None,
                 id=None,
                 use_type=None,
                 tracking_number=APIHelper.SKIP,
                 tracking_events=APIHelper.SKIP,
                 return_address=APIHelper.SKIP,
                 description=APIHelper.SKIP,
                 metadata=APIHelper.SKIP,
                 merge_variables=APIHelper.SKIP,
                 send_date=APIHelper.SKIP,
                 mail_type=APIHelper.SKIP,
                 double_sided=True,
                 address_placement=APIHelper.SKIP,
                 return_envelope=APIHelper.SKIP,
                 perforated_page=APIHelper.SKIP,
                 custom_envelope=APIHelper.SKIP,
                 thumbnails=APIHelper.SKIP,
                 expected_delivery_date=APIHelper.SKIP,
                 date_created=APIHelper.SKIP,
                 date_modified=APIHelper.SKIP,
                 deleted=APIHelper.SKIP,
                 url=APIHelper.SKIP,
                 template_id=APIHelper.SKIP,
                 template_version_id=APIHelper.SKIP,
                 campaign_id=APIHelper.SKIP,
                 fsc=False,
                 status=APIHelper.SKIP,
                 failure_reason=APIHelper.SKIP,
                 object=APIHelper.SKIP):
        """Constructor for the Registered class"""

        # Initialize members of the class
        self.extra_service = 'registered' 
        if tracking_number is not APIHelper.SKIP:
            self.tracking_number = tracking_number 
        if tracking_events is not APIHelper.SKIP:
            self.tracking_events = tracking_events 
        if return_address is not APIHelper.SKIP:
            self.return_address = return_address 
        if description is not APIHelper.SKIP:
            self.description = description 
        if metadata is not APIHelper.SKIP:
            self.metadata = metadata 
        if merge_variables is not APIHelper.SKIP:
            self.merge_variables = merge_variables 
        if send_date is not APIHelper.SKIP:
            self.send_date = send_date 
        if mail_type is not APIHelper.SKIP:
            self.mail_type = mail_type 
        self.color = color 
        self.double_sided = double_sided 
        if address_placement is not APIHelper.SKIP:
            self.address_placement = address_placement 
        if return_envelope is not APIHelper.SKIP:
            self.return_envelope = return_envelope 
        if perforated_page is not APIHelper.SKIP:
            self.perforated_page = perforated_page 
        if custom_envelope is not APIHelper.SKIP:
            self.custom_envelope = custom_envelope 
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
        self.mfrom = mfrom 
        if url is not APIHelper.SKIP:
            self.url = url 
        self.id = id 
        if template_id is not APIHelper.SKIP:
            self.template_id = template_id 
        if template_version_id is not APIHelper.SKIP:
            self.template_version_id = template_version_id 
        if campaign_id is not APIHelper.SKIP:
            self.campaign_id = campaign_id 
        self.use_type = use_type 
        self.fsc = fsc 
        if status is not APIHelper.SKIP:
            self.status = status 
        if failure_reason is not APIHelper.SKIP:
            self.failure_reason = failure_reason 
        if object is not APIHelper.SKIP:
            self.object = object 

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
        color = dictionary.get("color") if "color" in dictionary.keys() else None
        to = dictionary.get("to") if dictionary.get("to") else None
        mfrom = dictionary.get("from") if dictionary.get("from") else None
        id = dictionary.get("id") if dictionary.get("id") else None
        use_type = dictionary.get("use_type") if dictionary.get("use_type") else None
        tracking_number = dictionary.get("tracking_number") if "tracking_number" in dictionary.keys() else APIHelper.SKIP
        tracking_events = None
        if dictionary.get('tracking_events') is not None:
            tracking_events = [TrackingEventNormal.from_dictionary(x) for x in dictionary.get('tracking_events')]
        else:
            tracking_events = APIHelper.SKIP
        return_address = dictionary.get("return_address") if dictionary.get("return_address") else APIHelper.SKIP
        description = dictionary.get("description") if "description" in dictionary.keys() else APIHelper.SKIP
        metadata = dictionary.get("metadata") if dictionary.get("metadata") else APIHelper.SKIP
        merge_variables = dictionary.get("merge_variables") if "merge_variables" in dictionary.keys() else APIHelper.SKIP
        send_date = dictionary.get("send_date") if dictionary.get("send_date") else APIHelper.SKIP
        mail_type = dictionary.get("mail_type") if dictionary.get("mail_type") else APIHelper.SKIP
        double_sided = dictionary.get("double_sided") if dictionary.get("double_sided") else True
        address_placement = dictionary.get("address_placement") if dictionary.get("address_placement") else APIHelper.SKIP
        return_envelope = dictionary.get("return_envelope") if dictionary.get("return_envelope") else APIHelper.SKIP
        perforated_page = dictionary.get("perforated_page") if "perforated_page" in dictionary.keys() else APIHelper.SKIP
        custom_envelope = dictionary.get("custom_envelope") if dictionary.get("custom_envelope") else APIHelper.SKIP
        thumbnails = None
        if dictionary.get('thumbnails') is not None:
            thumbnails = [Thumbnail.from_dictionary(x) for x in dictionary.get('thumbnails')]
        else:
            thumbnails = APIHelper.SKIP
        expected_delivery_date = dateutil.parser.parse(dictionary.get('expected_delivery_date')).date() if dictionary.get('expected_delivery_date') else APIHelper.SKIP
        date_created = APIHelper.RFC3339DateTime.from_value(dictionary.get("date_created")).datetime if dictionary.get("date_created") else APIHelper.SKIP
        date_modified = APIHelper.RFC3339DateTime.from_value(dictionary.get("date_modified")).datetime if dictionary.get("date_modified") else APIHelper.SKIP
        deleted = dictionary.get("deleted") if "deleted" in dictionary.keys() else APIHelper.SKIP
        url = dictionary.get("url") if dictionary.get("url") else APIHelper.SKIP
        template_id = dictionary.get("template_id") if dictionary.get("template_id") else APIHelper.SKIP
        template_version_id = dictionary.get("template_version_id") if dictionary.get("template_version_id") else APIHelper.SKIP
        campaign_id = dictionary.get("campaign_id") if "campaign_id" in dictionary.keys() else APIHelper.SKIP
        fsc = dictionary.get("fsc") if dictionary.get("fsc") else False
        status = dictionary.get("status") if dictionary.get("status") else APIHelper.SKIP
        failure_reason = dictionary.get("failure_reason") if "failure_reason" in dictionary.keys() else APIHelper.SKIP
        object = dictionary.get("object") if dictionary.get("object") else APIHelper.SKIP
        # Return an object of this model
        return cls(color,
                   to,
                   mfrom,
                   id,
                   use_type,
                   tracking_number,
                   tracking_events,
                   return_address,
                   description,
                   metadata,
                   merge_variables,
                   send_date,
                   mail_type,
                   double_sided,
                   address_placement,
                   return_envelope,
                   perforated_page,
                   custom_envelope,
                   thumbnails,
                   expected_delivery_date,
                   date_created,
                   date_modified,
                   deleted,
                   url,
                   template_id,
                   template_version_id,
                   campaign_id,
                   fsc,
                   status,
                   failure_reason,
                   object)

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
            return APIHelper.is_valid_type(value=dictionary.extra_service,
                                           type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.color,
                                            type_callable=lambda value: isinstance(value, bool)) \
                and APIHelper.is_valid_type(value=dictionary.to,
                                            type_callable=lambda value: isinstance(value, object)) \
                and APIHelper.is_valid_type(value=dictionary.carrier,
                                            type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.mfrom,
                                            type_callable=lambda value: isinstance(value, object)) \
                and APIHelper.is_valid_type(value=dictionary.id,
                                            type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.use_type,
                                            type_callable=lambda value: isinstance(value, object))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('extra_service'),
                                       type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('color'),
                                        type_callable=lambda value: isinstance(value, bool)) \
            and APIHelper.is_valid_type(value=dictionary.get('to'),
                                        type_callable=lambda value: isinstance(value, object)) \
            and APIHelper.is_valid_type(value=dictionary.get('carrier'),
                                        type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('from'),
                                        type_callable=lambda value: isinstance(value, object)) \
            and APIHelper.is_valid_type(value=dictionary.get('id'),
                                        type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('use_type'),
                                        type_callable=lambda value: isinstance(value, object))