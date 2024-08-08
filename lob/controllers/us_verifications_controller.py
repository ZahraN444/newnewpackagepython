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
from lob.models.us_verifications import UsVerifications
from lob.models.us_verification import UsVerification
from lob.exceptions.domains_0_error_1_exception import Domains0Error1Exception


class USVerificationsController(BaseController):

    """A Controller to access Endpoints in the lob API."""
    def __init__(self, config):
        super(USVerificationsController, self).__init__(config)

    def bulk_us_verifications(self,
                              content_type,
                              addresses,
                              case=None):
        """Does a POST request to /bulk/us_verifications.

        Verify a list of US or US territory addresses _with a live API key_.
        Requests to this endpoint with a test API key will return a dummy
        response based on the primary line you input.

        Args:
            content_type (ContentTypeEnum): TODO: type description here.
            addresses (List[MultipleComponents]): TODO: type description
                here.
            case (Case2Enum, optional): Casing of the verified address.
                Possible values are `upper` and `proper` for uppercased (e.g.
                "PO BOX") and proper-cased (e.g. "PO Box"), respectively. Only
                affects `recipient`, `primary_line`, `secondary_line`,
                `urbanization`, and `last_line`. Default casing is `upper`.

        Returns:
            UsVerifications: Response from the API. Returns a list of US
                verification objects.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/bulk/us_verifications')
            .http_method(HttpMethodEnum.POST)
            .form_param(Parameter()
                        .key('addresses')
                        .value(addresses))
            .query_param(Parameter()
                         .key('case')
                         .value(case))
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
            .deserialize_into(UsVerifications.from_dictionary)
            .local_error('default', 'Error', Domains0Error1Exception)
        ).execute()

    def us_verification(self,
                        body,
                        case=None):
        """Does a POST request to /us_verifications.

        Verify a US or US territory address _with a live API key_. The address
        can be in components (e.g. `primary_line` is "210 King Street",
        `zip_code` is "94107") or as a single string (e.g. "210 King Street
        94107"), but not as both. Requests using a test API key validate
        required fields but return empty values unless specific `primary_line`
        values are provided. See the [US Verifications Test
        Environment](#section/US-Verifications-Test-Env) for details.

        Args:
            body (object): TODO: type description here.
            case (Case2Enum, optional): Casing of the verified address.
                Possible values are `upper` and `proper` for uppercased (e.g.
                "PO BOX") and proper-cased (e.g. "PO Box"), respectively. Only
                affects `recipient`, `primary_line`, `secondary_line`,
                `urbanization`, and `last_line`. Default casing is `upper`.

        Returns:
            UsVerification: Response from the API. Returns a US verification
                object.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/us_verifications')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .query_param(Parameter()
                         .key('case')
                         .value(case))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('basicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(UsVerification.from_dictionary)
            .local_error('default', 'Error', Domains0Error1Exception)
        ).execute()