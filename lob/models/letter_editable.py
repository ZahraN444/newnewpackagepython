# -*- coding: utf-8 -*-

"""
lob

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from lob.api_helper import APIHelper
from lob.models.qr_code_4 import QrCode4


class LetterEditable(object):

    """Implementation of the 'letter_editable' model.

    TODO: type model description here.

    Attributes:
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
        mfrom (str | InlineAddressUs | InlineAddressIntl): Must either be an
            address ID or an inline object with correct address parameters.
            Must be a US address unless using a `custom_envelope`. All
            addresses will be standardized into uppercase without being
            modified by verification.
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
        file (object): TODO: type description here.
        extra_service (object): TODO: type description here.
        cards (List[str]): A single-element array containing an existing card
            id in a string format. See [cards](#tag/Cards) for more
            information.
        color (bool): TODO: type description here.
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
        custom_envelope (str): Accepts an envelope ID for any customized
            envelope with available inventory. If no inventory is available
            for the specified ID, the letter will not be sent, and an error
            will be returned. If the letter has more than 6 sheets, it will be
            sent in a blank flat envelope. Custom envelopes may be created and
            ordered from the dashboard. This feature is exclusive to certain
            customers. Upgrade to the appropriate <a
            href="https://dashboard.lob.com/#/settings/editions"
            target="_blank">Print & Mail Edition</a> to gain access.
        billing_group_id (str): An optional string with the billing group ID
            to tag your usage with. Is used for billing purposes. Requires
            special activation to use. See <a
            href="#tag/Billing-Groups">Billing Group API</a> for more
            information.
        qr_code (QrCode4): TODO: type description here.
        use_type (object): TODO: type description here.
        fsc (bool): This is in beta. Contact support@lob.com or your account
            contact to learn more. Not available for `A4` letter size.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "to": 'to',
        "mfrom": 'from',
        "file": 'file',
        "color": 'color',
        "use_type": 'use_type',
        "description": 'description',
        "metadata": 'metadata',
        "mail_type": 'mail_type',
        "merge_variables": 'merge_variables',
        "send_date": 'send_date',
        "extra_service": 'extra_service',
        "cards": 'cards',
        "double_sided": 'double_sided',
        "address_placement": 'address_placement',
        "return_envelope": 'return_envelope',
        "perforated_page": 'perforated_page',
        "custom_envelope": 'custom_envelope',
        "billing_group_id": 'billing_group_id',
        "qr_code": 'qr_code',
        "fsc": 'fsc'
    }

    _optionals = [
        'description',
        'metadata',
        'mail_type',
        'merge_variables',
        'send_date',
        'extra_service',
        'cards',
        'double_sided',
        'address_placement',
        'return_envelope',
        'perforated_page',
        'custom_envelope',
        'billing_group_id',
        'qr_code',
        'fsc',
    ]

    _nullables = [
        'description',
        'merge_variables',
        'cards',
        'perforated_page',
        'custom_envelope',
    ]

    def __init__(self,
                 to=None,
                 mfrom=None,
                 file=None,
                 color=None,
                 use_type=None,
                 description=APIHelper.SKIP,
                 metadata=APIHelper.SKIP,
                 mail_type=APIHelper.SKIP,
                 merge_variables=APIHelper.SKIP,
                 send_date=APIHelper.SKIP,
                 extra_service=APIHelper.SKIP,
                 cards=APIHelper.SKIP,
                 double_sided=True,
                 address_placement=APIHelper.SKIP,
                 return_envelope=APIHelper.SKIP,
                 perforated_page=APIHelper.SKIP,
                 custom_envelope=APIHelper.SKIP,
                 billing_group_id=APIHelper.SKIP,
                 qr_code=APIHelper.SKIP,
                 fsc=False):
        """Constructor for the LetterEditable class"""

        # Initialize members of the class
        self.to = to 
        self.mfrom = mfrom 
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
        self.file = file 
        if extra_service is not APIHelper.SKIP:
            self.extra_service = extra_service 
        if cards is not APIHelper.SKIP:
            self.cards = cards 
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
        if billing_group_id is not APIHelper.SKIP:
            self.billing_group_id = billing_group_id 
        if qr_code is not APIHelper.SKIP:
            self.qr_code = qr_code 
        self.use_type = use_type 
        self.fsc = fsc 

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
        to = APIHelper.deserialize_union_type(UnionTypeLookUp.get('LetterEditableTo'), dictionary.get('to'), False) if dictionary.get('to') is not None else None
        mfrom = APIHelper.deserialize_union_type(UnionTypeLookUp.get('LetterEditableFrom'), dictionary.get('from'), False) if dictionary.get('from') is not None else None
        file = dictionary.get("file") if dictionary.get("file") else None
        color = dictionary.get("color") if "color" in dictionary.keys() else None
        use_type = dictionary.get("use_type") if dictionary.get("use_type") else None
        description = dictionary.get("description") if "description" in dictionary.keys() else APIHelper.SKIP
        metadata = dictionary.get("metadata") if dictionary.get("metadata") else APIHelper.SKIP
        mail_type = dictionary.get("mail_type") if dictionary.get("mail_type") else APIHelper.SKIP
        merge_variables = dictionary.get("merge_variables") if "merge_variables" in dictionary.keys() else APIHelper.SKIP
        send_date = dictionary.get("send_date") if dictionary.get("send_date") else APIHelper.SKIP
        extra_service = dictionary.get("extra_service") if dictionary.get("extra_service") else APIHelper.SKIP
        cards = dictionary.get("cards") if "cards" in dictionary.keys() else APIHelper.SKIP
        double_sided = dictionary.get("double_sided") if dictionary.get("double_sided") else True
        address_placement = dictionary.get("address_placement") if dictionary.get("address_placement") else APIHelper.SKIP
        return_envelope = dictionary.get("return_envelope") if dictionary.get("return_envelope") else APIHelper.SKIP
        perforated_page = dictionary.get("perforated_page") if "perforated_page" in dictionary.keys() else APIHelper.SKIP
        custom_envelope = dictionary.get("custom_envelope") if "custom_envelope" in dictionary.keys() else APIHelper.SKIP
        billing_group_id = dictionary.get("billing_group_id") if dictionary.get("billing_group_id") else APIHelper.SKIP
        qr_code = QrCode4.from_dictionary(dictionary.get('qr_code')) if 'qr_code' in dictionary.keys() else APIHelper.SKIP
        fsc = dictionary.get("fsc") if dictionary.get("fsc") else False
        # Return an object of this model
        return cls(to,
                   mfrom,
                   file,
                   color,
                   use_type,
                   description,
                   metadata,
                   mail_type,
                   merge_variables,
                   send_date,
                   extra_service,
                   cards,
                   double_sided,
                   address_placement,
                   return_envelope,
                   perforated_page,
                   custom_envelope,
                   billing_group_id,
                   qr_code,
                   fsc)

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
            return UnionTypeLookUp.get('LetterEditableTo').validate(dictionary.to).is_valid \
                and UnionTypeLookUp.get('LetterEditableFrom').validate(dictionary.mfrom).is_valid \
                and APIHelper.is_valid_type(value=dictionary.file,
                                            type_callable=lambda value: isinstance(value, object)) \
                and APIHelper.is_valid_type(value=dictionary.color,
                                            type_callable=lambda value: isinstance(value, bool)) \
                and APIHelper.is_valid_type(value=dictionary.use_type,
                                            type_callable=lambda value: isinstance(value, object))

        if not isinstance(dictionary, dict):
            return False

        return UnionTypeLookUp.get('LetterEditableTo').validate(dictionary.get('to')).is_valid \
            and UnionTypeLookUp.get('LetterEditableFrom').validate(dictionary.get('from')).is_valid \
            and APIHelper.is_valid_type(value=dictionary.get('file'),
                                        type_callable=lambda value: isinstance(value, object)) \
            and APIHelper.is_valid_type(value=dictionary.get('color'),
                                        type_callable=lambda value: isinstance(value, bool)) \
            and APIHelper.is_valid_type(value=dictionary.get('use_type'),
                                        type_callable=lambda value: isinstance(value, object))
