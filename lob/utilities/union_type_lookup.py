# -*- coding: utf-8 -*-

"""
lob

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from apimatic_core.types.union_types.any_of import AnyOf
from apimatic_core.types.union_types.leaf_type import LeafType
from apimatic_core.types.union_types.one_of import OneOf
from apimatic_core.types.union_types.union_type_context import UnionTypeContext as Context
from lob.models.address_intl import AddressIntl
from lob.models.address_types_enum import AddressTypesEnum
from lob.models.address_us import AddressUs
from lob.models.addressobjwithcompanydefined import Addressobjwithcompanydefined
from lob.models.addressobjwithnamedefined import Addressobjwithnamedefined
from lob.models.bank_account_types_enum import BankAccountTypesEnum
from lob.models.certified import Certified
from lob.models.check_types_enum import CheckTypesEnum
from lob.models.company_validation import CompanyValidation
from lob.models.error import Error
from lob.models.inline_address_intl import InlineAddressIntl
from lob.models.inline_address_us import InlineAddressUs
from lob.models.intl_verification import IntlVerification
from lob.models.letter_types_enum import LetterTypesEnum
from lob.models.no_extra_service import NoExtraService
from lob.models.postcard_types_enum import PostcardTypesEnum
from lob.models.recipient_validation import RecipientValidation
from lob.models.registered import Registered
from lob.models.self_mailer_types_enum import SelfMailerTypesEnum
from lob.models.us_verification import UsVerification


class UnionTypeLookUp:

    """The `UnionTypeLookUp` class serves as a utility class for 
    storing and managing type combinator templates.It acts as a container for the templates 
    used in handling various data types within the application.

    """
    _templates = {
        'address': OneOf(
            [
                LeafType(AddressUs),
                LeafType(AddressIntl)
            ]
        ),
        'identity_validation': OneOf(
            [
                LeafType(RecipientValidation),
                LeafType(CompanyValidation)
            ]
        ),
        'BuckslipEditableFront': OneOf(
            [
                LeafType(str)
            ]
        ),
        'BuckslipEditableBack': OneOf(
            [
                LeafType(str)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'UsVerificationsAddresses': OneOf(
            [
                LeafType(UsVerification),
                LeafType(Error)
            ],
            Context.create(
               is_array=True
            )
        ),
        'IntlVerificationsAddresses': OneOf(
            [
                LeafType(IntlVerification),
                LeafType(Error)
            ],
            Context.create(
               is_array=True
            )
        ),
        'CreativeFrom': OneOf(
            [
                LeafType(str),
                LeafType(InlineAddressUs)
            ]
        ),
        'CardEditableFront': OneOf(
            [
                LeafType(str)
            ]
        ),
        'CardEditableBack': OneOf(
            [
                LeafType(str)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'inline_address_us_chk11': AnyOf(
            [
                LeafType(Addressobjwithnamedefined),
                LeafType(Addressobjwithcompanydefined)
            ]
        ),
        'CheckInputToTo': OneOf(
            [
                LeafType(str),
                AnyOf(
                    [
                        LeafType(Addressobjwithnamedefined),
                        LeafType(Addressobjwithcompanydefined)
                    ]
                )
            ],
            Context.create(
               is_optional=True
            )
        ),
        'CheckEditablePropsTo': OneOf(
            [
                LeafType(str),
                AnyOf(
                    [
                        LeafType(Addressobjwithnamedefined),
                        LeafType(Addressobjwithcompanydefined)
                    ]
                )
            ]
        ),
        'CheckEditablePropsFrom': OneOf(
            [
                LeafType(str),
                LeafType(InlineAddressUs)
            ]
        ),
        'CheckEditablePropsLogo': OneOf(
            [
                LeafType(str)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'CheckEditablePropsAttachment': OneOf(
            [
                LeafType(str)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'QrCodeCampaignsRedirectUrl': OneOf(
            [
                LeafType(str)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'inline_address': OneOf(
            [
                LeafType(InlineAddressUs),
                LeafType(InlineAddressIntl)
            ]
        ),
        'InputToTo': OneOf(
            [
                LeafType(str),
                OneOf(
                    [
                        LeafType(InlineAddressUs),
                        LeafType(InlineAddressIntl)
                    ]
                )
            ],
            Context.create(
               is_optional=True
            )
        ),
        'InputFromFrom': OneOf(
            [
                LeafType(str),
                OneOf(
                    [
                        LeafType(InlineAddressUs),
                        LeafType(InlineAddressIntl)
                    ]
                )
            ],
            Context.create(
               is_optional=True
            )
        ),
        'LetterEditableTo': OneOf(
            [
                LeafType(str),
                OneOf(
                    [
                        LeafType(InlineAddressUs),
                        LeafType(InlineAddressIntl)
                    ]
                )
            ]
        ),
        'LetterEditableFrom': OneOf(
            [
                LeafType(str),
                OneOf(
                    [
                        LeafType(InlineAddressUs),
                        LeafType(InlineAddressIntl)
                    ]
                )
            ]
        ),
        'InputFromUsFrom': OneOf(
            [
                LeafType(str),
                LeafType(InlineAddressUs)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'PostcardEditableTo': OneOf(
            [
                LeafType(str),
                OneOf(
                    [
                        LeafType(InlineAddressUs),
                        LeafType(InlineAddressIntl)
                    ]
                )
            ]
        ),
        'PostcardEditableFrom': OneOf(
            [
                LeafType(str),
                LeafType(InlineAddressUs)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'SelfMailerEditableTo': OneOf(
            [
                LeafType(str),
                OneOf(
                    [
                        LeafType(InlineAddressUs),
                        LeafType(InlineAddressIntl)
                    ]
                )
            ]
        ),
        'SelfMailerEditableFrom': OneOf(
            [
                LeafType(str),
                LeafType(InlineAddressUs)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'SelfMailerEditableInside': OneOf(
            [
                LeafType(str)
            ]
        ),
        'SelfMailerEditableOutside': OneOf(
            [
                LeafType(str)
            ]
        ),
        'EventTypeId': OneOf(
            [
                LeafType(PostcardTypesEnum),
                LeafType(SelfMailerTypesEnum),
                LeafType(LetterTypesEnum),
                LeafType(CheckTypesEnum),
                LeafType(AddressTypesEnum),
                LeafType(BankAccountTypesEnum)
            ]
        ),
        'address2': OneOf(
            [
                LeafType(AddressUs),
                LeafType(AddressIntl)
            ],
            Context.create(
               is_array=True,
               is_optional=True
            )
        ),
        'letter': OneOf(
            [
                LeafType(NoExtraService),
                LeafType(Registered),
                LeafType(Certified)
            ],
            Context.create(
               is_array=True,
               is_optional=True
            )
        ),
        'ImageatcheckbottomTo': OneOf(
            [
                LeafType(str),
                AnyOf(
                    [
                        LeafType(Addressobjwithnamedefined),
                        LeafType(Addressobjwithcompanydefined)
                    ]
                )
            ]
        ),
        'ImageatcheckbottomFrom': OneOf(
            [
                LeafType(str),
                LeafType(InlineAddressUs)
            ]
        ),
        'ImageatcheckbottomLogo': OneOf(
            [
                LeafType(str)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'ImageatcheckbottomAttachment': OneOf(
            [
                LeafType(str)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'ValidationErrorLoc': AnyOf(
            [
                LeafType(str),
                LeafType(int)
            ],
            Context.create(
               is_array=True
            )
        ),
        'WordsatcheckbottomTo': OneOf(
            [
                LeafType(str),
                AnyOf(
                    [
                        LeafType(Addressobjwithnamedefined),
                        LeafType(Addressobjwithcompanydefined)
                    ]
                )
            ]
        ),
        'WordsatcheckbottomFrom': OneOf(
            [
                LeafType(str),
                LeafType(InlineAddressUs)
            ]
        ),
        'WordsatcheckbottomLogo': OneOf(
            [
                LeafType(str)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'WordsatcheckbottomAttachment': OneOf(
            [
                LeafType(str)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'QrCode1RedirectUrl': OneOf(
            [
                LeafType(str)
            ],
            Context.create(
               is_optional=True
            )
        )
    }

    @staticmethod
    def get(name):
        return UnionTypeLookUp._templates[name]

