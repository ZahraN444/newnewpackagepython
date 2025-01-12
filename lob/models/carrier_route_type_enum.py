# -*- coding: utf-8 -*-

"""
lob

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class CarrierRouteTypeEnum(object):

    """Implementation of the 'CarrierRouteType' enum.

    The type of `components[carrier_route]`. For more detailed information
    about
    each carrier route type, see [US Verification
    Details](#tag/US-Verification-Types).

    Attributes:
        CITY_DELIVERY: TODO: type description here.
        RURAL_ROUTE: TODO: type description here.
        HIGHWAY_CONTRACT: TODO: type description here.
        PO_BOX: TODO: type description here.
        GENERAL_DELIVERY: TODO: type description here.

    """
    _all_values = ['city_delivery', 'rural_route', 'highway_contract', 'po_box', 'general_delivery']
    CITY_DELIVERY = 'city_delivery'

    RURAL_ROUTE = 'rural_route'

    HIGHWAY_CONTRACT = 'highway_contract'

    PO_BOX = 'po_box'

    GENERAL_DELIVERY = 'general_delivery'

    @classmethod
    def validate(cls, value):
        """Validates value contains in enum

        Args:
            value: the value to be validated

        Returns:
            boolean : if value is valid enum values.

        """
        return value in cls._all_values
   