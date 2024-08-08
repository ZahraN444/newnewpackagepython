# -*- coding: utf-8 -*-

"""
lob

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from lob.api_helper import APIHelper
from lob.configuration import Server
from lob.controllers.base_controller import BaseController
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from lob.http.http_method_enum import HttpMethodEnum
from apimatic_core.authentication.multiple.single_auth import Single
from lob.models.intl_autocompletions import IntlAutocompletions
from lob.exceptions.domains_0_error_1_exception import Domains0Error1Exception


class IntlAutocompletionsController(BaseController):

    """A Controller to access Endpoints in the lob API."""
    def __init__(self, config):
        super(IntlAutocompletionsController, self).__init__(config)

    def intl_autocompletions(self,
                             content_type,
                             address_prefix,
                             country,
                             x_lang_output=None,
                             city=None,
                             state=None,
                             zip_code=None,
                             geo_ip_sort=None):
        """Does a POST request to /intl_autocompletions.

        Given an address prefix consisting of a partial primary line and
        country, as well as optional input of city, state, and zip code, this
        functionality returns up to 10 full International address suggestions.
        Not all of them will turn out to be valid addresses; they'll need to
        be [verified](#operation/intl_verification).

        Args:
            content_type (ContentTypeEnum): TODO: type description here.
            address_prefix (str): Only accepts numbers and street names in an
                alphanumeric format.
            country (CountryExtendedEnum): TODO: type description here.
            x_lang_output (XLangOutput1Enum, optional): * `native` - Translate
                response to the native language of the country in the request
                * `match` - match the response to the language in the request 
                Default response is in English.
            city (str, optional): An optional city input used to filter
                suggestions. Case insensitive and does not match partial
                abbreviations.
            state (str, optional): An optional state input used to filter
                suggestions. Case insensitive and does not match partial
                abbreviations.
            zip_code (str, optional): An optional Zip Code input used to
                filter suggestions. Matches partial entries.
            geo_ip_sort (bool, optional): If `true`, sort suggestions by
                proximity to the IP set in the `X-Forwarded-For` header.

        Returns:
            IntlAutocompletions: Response from the API. Returns an
                international autocompletions object.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/intl_autocompletions')
            .http_method(HttpMethodEnum.POST)
            .form_param(Parameter()
                        .key('address_prefix')
                        .value(address_prefix))
            .form_param(Parameter()
                        .key('country')
                        .value(country))
            .header_param(Parameter()
                          .key('x-lang-output')
                          .value(x_lang_output))
            .form_param(Parameter()
                        .key('city')
                        .value(city))
            .form_param(Parameter()
                        .key('state')
                        .value(state))
            .form_param(Parameter()
                        .key('zip_code')
                        .value(zip_code))
            .form_param(Parameter()
                        .key('geo_ip_sort')
                        .value(geo_ip_sort))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/x-www-form-urlencoded'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('basicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(IntlAutocompletions.from_dictionary)
            .local_error('default', 'Error', Domains0Error1Exception)
        ).execute()