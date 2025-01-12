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
from lob.models.reverse_geocode import ReverseGeocode
from lob.exceptions.domains_0_error_1_exception import Domains0Error1Exception


class ReverseGeocodeLookupsController(BaseController):

    """A Controller to access Endpoints in the lob API."""
    def __init__(self, config):
        super(ReverseGeocodeLookupsController, self).__init__(config)

    def reverse_geocode_lookup(self,
                               content_type,
                               latitude,
                               longitude,
                               size=5):
        """Does a POST request to /us_reverse_geocode_lookups.

        Reverse geocode a valid US location with a live API key.

        Args:
            content_type (ContentTypeEnum): TODO: type description here.
            latitude (float): A positive or negative decimal indicating the
                geographic latitude of the address, specifying the
                north-to-south position of a location. This should be input
                with `longitude` to pinpoint locations on a map.
            longitude (float): A positive or negative decimal indicating the
                geographic longitude of the address, specifying the
                north-to-south position of a location. This should be input
                with `latitude` to pinpoint locations on a map.
            size (int, optional): Determines the number of locations returned.
                Possible values are between 1 and 50 and any number higher
                will be rounded down to 50. Default size is a list of 5
                reverse geocoded locations.

        Returns:
            ReverseGeocode: Response from the API. Returns a zip lookup object
                if a valid zip was provided.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/us_reverse_geocode_lookups')
            .http_method(HttpMethodEnum.POST)
            .form_param(Parameter()
                        .key('latitude')
                        .value(latitude))
            .form_param(Parameter()
                        .key('longitude')
                        .value(longitude))
            .query_param(Parameter()
                         .key('size')
                         .value(size))
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
            .deserialize_into(ReverseGeocode.from_dictionary)
            .local_error('default', 'Error', Domains0Error1Exception)
        ).execute()
