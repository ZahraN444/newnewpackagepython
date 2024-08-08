# -*- coding: utf-8 -*-

"""
lob

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class LetterTypesEnum(object):

    """Implementation of the 'letter_types' enum.

    Unique identifier referring to status of letter

    Attributes:
        ENUM_LETTERCREATED: TODO: type description here.
        ENUM_LETTERRENDERED_PDF: TODO: type description here.
        ENUM_LETTERRENDERED_THUMBNAILS: TODO: type description here.
        ENUM_LETTERDELETED: TODO: type description here.
        ENUM_LETTERDELIVERED: TODO: type description here.
        ENUM_LETTERFAILED: TODO: type description here.
        ENUM_LETTERMAILED: TODO: type description here.
        ENUM_LETTERIN_TRANSIT: TODO: type description here.
        ENUM_LETTERIN_LOCAL_AREA: TODO: type description here.
        ENUM_LETTERINTERNATIONAL_EXIT: TODO: type description here.
        ENUM_LETTERPROCESSED_FOR_DELIVERY: TODO: type description here.
        ENUM_LETTERREROUTED: TODO: type description here.
        ENUM_LETTERRETURNED_TO_SENDER: TODO: type description here.
        ENUM_LETTERCERTIFIEDMAILED: TODO: type description here.
        ENUM_LETTERCERTIFIEDIN_TRANSIT: TODO: type description here.
        ENUM_LETTERCERTIFIEDIN_LOCAL_AREA: TODO: type description here.
        ENUM_LETTERCERTIFIEDPROCESSED_FOR_DELIVERY: TODO: type description
            here.
        ENUM_LETTERCERTIFIEDREROUTED: TODO: type description here.
        ENUM_LETTERCERTIFIEDRETURNED_TO_SENDER: TODO: type description here.
        ENUM_LETTERCERTIFIEDDELIVERED: TODO: type description here.
        ENUM_LETTERCERTIFIEDPICKUP_AVAILABLE: TODO: type description here.
        ENUM_LETTERCERTIFIEDISSUE: TODO: type description here.
        ENUM_LETTERRETURN_ENVELOPECREATED: TODO: type description here.
        ENUM_LETTERRETURN_ENVELOPEDELIVERED: TODO: type description here.
        ENUM_LETTERRETURN_ENVELOPEIN_TRANSIT: TODO: type description here.
        ENUM_LETTERRETURN_ENVELOPEIN_LOCAL_AREA: TODO: type description here.
        ENUM_LETTERRETURN_ENVELOPEINTERNATIONAL_EXIT: TODO: type description
            here.
        ENUM_LETTERRETURN_ENVELOPEPROCESSED_FOR_DELIVERY: TODO: type
            description here.
        ENUM_LETTERRETURN_ENVELOPERE_ROUTED: TODO: type description here.
        ENUM_LETTERRETURN_ENVELOPERETURNED_TO_SENDER: TODO: type description
            here.
        ENUM_LETTERVIEWED: TODO: type description here.

    """
    _all_values = ['letter.created', 'letter.rendered_pdf', 'letter.rendered_thumbnails', 'letter.deleted', 'letter.delivered', 'letter.failed', 'letter.mailed', 'letter.in_transit', 'letter.in_local_area', 'letter.international_exit', 'letter.processed_for_delivery', 'letter.re-routed', 'letter.returned_to_sender', 'letter.certified.mailed', 'letter.certified.in_transit', 'letter.certified.in_local_area', 'letter.certified.processed_for_delivery', 'letter.certified.re-routed', 'letter.certified.returned_to_sender', 'letter.certified.delivered', 'letter.certified.pickup_available', 'letter.certified.issue', 'letter.return_envelope.created', 'letter.return_envelope.delivered', 'letter.return_envelope.in_transit', 'letter.return_envelope.in_local_area', 'letter.return_envelope.international_exit', 'letter.return_envelope.processed_for_delivery', 'letter.return_envelope.re_routed', 'letter.return_envelope.returned_to_sender', 'letter.viewed']
    ENUM_LETTERCREATED = 'letter.created'

    ENUM_LETTERRENDERED_PDF = 'letter.rendered_pdf'

    ENUM_LETTERRENDERED_THUMBNAILS = 'letter.rendered_thumbnails'

    ENUM_LETTERDELETED = 'letter.deleted'

    ENUM_LETTERDELIVERED = 'letter.delivered'

    ENUM_LETTERFAILED = 'letter.failed'

    ENUM_LETTERMAILED = 'letter.mailed'

    ENUM_LETTERIN_TRANSIT = 'letter.in_transit'

    ENUM_LETTERIN_LOCAL_AREA = 'letter.in_local_area'

    ENUM_LETTERINTERNATIONAL_EXIT = 'letter.international_exit'

    ENUM_LETTERPROCESSED_FOR_DELIVERY = 'letter.processed_for_delivery'

    ENUM_LETTERREROUTED = 'letter.re-routed'

    ENUM_LETTERRETURNED_TO_SENDER = 'letter.returned_to_sender'

    ENUM_LETTERCERTIFIEDMAILED = 'letter.certified.mailed'

    ENUM_LETTERCERTIFIEDIN_TRANSIT = 'letter.certified.in_transit'

    ENUM_LETTERCERTIFIEDIN_LOCAL_AREA = 'letter.certified.in_local_area'

    ENUM_LETTERCERTIFIEDPROCESSED_FOR_DELIVERY = 'letter.certified.processed_for_delivery'

    ENUM_LETTERCERTIFIEDREROUTED = 'letter.certified.re-routed'

    ENUM_LETTERCERTIFIEDRETURNED_TO_SENDER = 'letter.certified.returned_to_sender'

    ENUM_LETTERCERTIFIEDDELIVERED = 'letter.certified.delivered'

    ENUM_LETTERCERTIFIEDPICKUP_AVAILABLE = 'letter.certified.pickup_available'

    ENUM_LETTERCERTIFIEDISSUE = 'letter.certified.issue'

    ENUM_LETTERRETURN_ENVELOPECREATED = 'letter.return_envelope.created'

    ENUM_LETTERRETURN_ENVELOPEDELIVERED = 'letter.return_envelope.delivered'

    ENUM_LETTERRETURN_ENVELOPEIN_TRANSIT = 'letter.return_envelope.in_transit'

    ENUM_LETTERRETURN_ENVELOPEIN_LOCAL_AREA = 'letter.return_envelope.in_local_area'

    ENUM_LETTERRETURN_ENVELOPEINTERNATIONAL_EXIT = 'letter.return_envelope.international_exit'

    ENUM_LETTERRETURN_ENVELOPEPROCESSED_FOR_DELIVERY = 'letter.return_envelope.processed_for_delivery'

    ENUM_LETTERRETURN_ENVELOPERE_ROUTED = 'letter.return_envelope.re_routed'

    ENUM_LETTERRETURN_ENVELOPERETURNED_TO_SENDER = 'letter.return_envelope.returned_to_sender'

    ENUM_LETTERVIEWED = 'letter.viewed'

    @classmethod
    def validate(cls, value):
        """Validates value contains in enum

        Args:
            value: the value to be validated

        Returns:
            boolean : if value is valid enum values.

        """
        return value in cls._all_values
   