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
from lob.models.qr_code_analytics_response import QrCodeAnalyticsResponse


class QRCodesController(BaseController):

    """A Controller to access Endpoints in the lob API."""
    def __init__(self, config):
        super(QRCodesController, self).__init__(config)

    def qr_codes_list(self,
                      limit=10,
                      offset=0,
                      include=None,
                      date_created=None,
                      scanned=None,
                      resource_ids=None):
        """Does a GET request to /qr_code_analytics.

        Returns a list of your QR codes. The QR codes are returned sorted by
        scan date, with the most recently scanned QR codes appearing first.

        Args:
            limit (int, optional): How many results to return.
            offset (int, optional): An integer that designates the offset at
                which to begin returning results. Defaults to 0.
            include (List[str], optional): Request that the response include
                the total count by specifying `include=["total_count"]`.
            date_created (Dict[str, str], optional): Filter by date created.
                Accepted formats are ISO-8601 date or datetime, e.g. `{ "gt":
                "2012-01-01", "lt": "2012-01-31T12:34:56Z" }` where `gt` is >,
                `lt` is <, `gte` is ≥, and `lte` is ≤.
            scanned (bool, optional): Filter list of responses to only include
                QR codes with at least one scan event.
            resource_ids (List[object], optional): Filter by the resource ID.

        Returns:
            QrCodeAnalyticsResponse: Response from the API. Returns a list of
                QR Codes and their analytics.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/qr_code_analytics')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('limit')
                         .value(limit))
            .query_param(Parameter()
                         .key('offset')
                         .value(offset))
            .query_param(Parameter()
                         .key('include')
                         .value(include))
            .query_param(Parameter()
                         .key('date_created')
                         .value(date_created))
            .query_param(Parameter()
                         .key('scanned')
                         .value(scanned))
            .query_param(Parameter()
                         .key('resource_ids')
                         .value(resource_ids))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('basicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(QrCodeAnalyticsResponse.from_dictionary)
        ).execute()