# -*- coding: utf-8 -*-

"""
lob

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from lob.api_helper import APIHelper


class Editable(object):

    """Implementation of the 'editable' model.

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

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "description": 'description',
        "metadata": 'metadata',
        "mail_type": 'mail_type',
        "merge_variables": 'merge_variables',
        "send_date": 'send_date'
    }

    _optionals = [
        'description',
        'metadata',
        'mail_type',
        'merge_variables',
        'send_date',
    ]

    _nullables = [
        'description',
        'merge_variables',
    ]

    def __init__(self,
                 description=APIHelper.SKIP,
                 metadata=APIHelper.SKIP,
                 mail_type=APIHelper.SKIP,
                 merge_variables=APIHelper.SKIP,
                 send_date=APIHelper.SKIP):
        """Constructor for the Editable class"""

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
        description = dictionary.get("description") if "description" in dictionary.keys() else APIHelper.SKIP
        metadata = dictionary.get("metadata") if dictionary.get("metadata") else APIHelper.SKIP
        mail_type = dictionary.get("mail_type") if dictionary.get("mail_type") else APIHelper.SKIP
        merge_variables = dictionary.get("merge_variables") if "merge_variables" in dictionary.keys() else APIHelper.SKIP
        send_date = dictionary.get("send_date") if dictionary.get("send_date") else APIHelper.SKIP
        # Return an object of this model
        return cls(description,
                   metadata,
                   mail_type,
                   merge_variables,
                   send_date)
