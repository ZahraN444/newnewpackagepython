# -*- coding: utf-8 -*-

"""
lob

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from lob.api_helper import APIHelper
from lob.models.qr_code_4 import QrCode4


class PostcardEditable(object):

    """Implementation of the 'postcard_editable' model.

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
        size (PostcardSizeEnum): TODO: type description here.
        to (str | InlineAddressUs | InlineAddressIntl): Must either be an
            address ID or an inline object with correct address parameters. If
            an object is used, an address will be created, corrected, and
            standardized for free whenever possible using our US Address
            Verification engine (if it is a US address), and returned back
            with an ID. Depending on your <a
            href="https://dashboard.lob.com/#/settings/editions"
            target="_blank">Print & Mail Edition</a>, US addresses may also be
            run through <a href="#tag/National-Change-of-Address">National
            Change of Address Linkage(NCOALink)</a>. Non-US addresses will be
            standardized into uppercase only. If a US address used does not
            meet your account’s <a
            href="https://dashboard.lob.com/#/settings/account"
            target="_blank">US Mail strictness setting</a>, the request will
            fail. <a
            href="https://help.lob.com/print-and-mail/all-about-addresses"
            target="_blank">Lob Guide: Verification of Mailing Addresses</a>
        mfrom (str | InlineAddressUs | None): *Required* if `to` address is
            international. Must either be an address ID or an inline object
            with correct address parameters. Must either be an address ID or
            an inline object with correct address parameters. All addresses
            will be standardized into uppercase without being modified by
            verification.
        front (object): TODO: type description here.
        back (object): TODO: type description here.
        billing_group_id (str): An optional string with the billing group ID
            to tag your usage with. Is used for billing purposes. Requires
            special activation to use. See <a
            href="#tag/Billing-Groups">Billing Group API</a> for more
            information.
        qr_code (QrCode4): TODO: type description here.
        use_type (object): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "to": 'to',
        "front": 'front',
        "back": 'back',
        "use_type": 'use_type',
        "description": 'description',
        "metadata": 'metadata',
        "mail_type": 'mail_type',
        "merge_variables": 'merge_variables',
        "send_date": 'send_date',
        "size": 'size',
        "mfrom": 'from',
        "billing_group_id": 'billing_group_id',
        "qr_code": 'qr_code'
    }

    _optionals = [
        'description',
        'metadata',
        'mail_type',
        'merge_variables',
        'send_date',
        'size',
        'mfrom',
        'billing_group_id',
        'qr_code',
    ]

    _nullables = [
        'description',
        'merge_variables',
    ]

    def __init__(self,
                 to=None,
                 front=None,
                 back=None,
                 use_type=None,
                 description=APIHelper.SKIP,
                 metadata=APIHelper.SKIP,
                 mail_type=APIHelper.SKIP,
                 merge_variables=APIHelper.SKIP,
                 send_date=APIHelper.SKIP,
                 size=APIHelper.SKIP,
                 mfrom=APIHelper.SKIP,
                 billing_group_id=APIHelper.SKIP,
                 qr_code=APIHelper.SKIP):
        """Constructor for the PostcardEditable class"""

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
        if mfrom is not APIHelper.SKIP:
            self.mfrom = mfrom 
        self.front = front 
        self.back = back 
        if billing_group_id is not APIHelper.SKIP:
            self.billing_group_id = billing_group_id 
        if qr_code is not APIHelper.SKIP:
            self.qr_code = qr_code 
        self.use_type = use_type 

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
        to = APIHelper.deserialize_union_type(UnionTypeLookUp.get('PostcardEditableTo'), dictionary.get('to'), False) if dictionary.get('to') is not None else None
        front = dictionary.get("front") if dictionary.get("front") else None
        back = dictionary.get("back") if dictionary.get("back") else None
        use_type = dictionary.get("use_type") if dictionary.get("use_type") else None
        description = dictionary.get("description") if "description" in dictionary.keys() else APIHelper.SKIP
        metadata = dictionary.get("metadata") if dictionary.get("metadata") else APIHelper.SKIP
        mail_type = dictionary.get("mail_type") if dictionary.get("mail_type") else APIHelper.SKIP
        merge_variables = dictionary.get("merge_variables") if "merge_variables" in dictionary.keys() else APIHelper.SKIP
        send_date = dictionary.get("send_date") if dictionary.get("send_date") else APIHelper.SKIP
        size = dictionary.get("size") if dictionary.get("size") else APIHelper.SKIP
        mfrom = APIHelper.deserialize_union_type(UnionTypeLookUp.get('PostcardEditableFrom'), dictionary.get('from'), False) if dictionary.get('from') is not None else APIHelper.SKIP
        billing_group_id = dictionary.get("billing_group_id") if dictionary.get("billing_group_id") else APIHelper.SKIP
        qr_code = QrCode4.from_dictionary(dictionary.get('qr_code')) if 'qr_code' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(to,
                   front,
                   back,
                   use_type,
                   description,
                   metadata,
                   mail_type,
                   merge_variables,
                   send_date,
                   size,
                   mfrom,
                   billing_group_id,
                   qr_code)

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
            return UnionTypeLookUp.get('PostcardEditableTo').validate(dictionary.to).is_valid \
                and APIHelper.is_valid_type(value=dictionary.front,
                                            type_callable=lambda value: isinstance(value, object)) \
                and APIHelper.is_valid_type(value=dictionary.back,
                                            type_callable=lambda value: isinstance(value, object)) \
                and APIHelper.is_valid_type(value=dictionary.use_type,
                                            type_callable=lambda value: isinstance(value, object))

        if not isinstance(dictionary, dict):
            return False

        return UnionTypeLookUp.get('PostcardEditableTo').validate(dictionary.get('to')).is_valid \
            and APIHelper.is_valid_type(value=dictionary.get('front'),
                                        type_callable=lambda value: isinstance(value, object)) \
            and APIHelper.is_valid_type(value=dictionary.get('back'),
                                        type_callable=lambda value: isinstance(value, object)) \
            and APIHelper.is_valid_type(value=dictionary.get('use_type'),
                                        type_callable=lambda value: isinstance(value, object))
