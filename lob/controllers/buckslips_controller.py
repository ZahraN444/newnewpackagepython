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
from lob.models.buckslips_response import BuckslipsResponse
from lob.models.buckslip import Buckslip
from lob.models.buckslips_response_1 import BuckslipsResponse1
from lob.exceptions.domains_0_error_1_exception import Domains0Error1Exception


class BuckslipsController(BaseController):

    """A Controller to access Endpoints in the lob API."""
    def __init__(self, config):
        super(BuckslipsController, self).__init__(config)

    def buckslips_list(self,
                       limit=10,
                       before_after=None,
                       include=None):
        """Does a GET request to /buckslips.

        Returns a list of your buckslips. The buckslips are returned sorted by
        creation date, with the most recently created buckslips appearing
        first.

        Args:
            limit (int, optional): How many results to return.
            before_after (Beforeafter, optional): `before` and `after` are
                both optional but only one of them can be in the query at a
                time.
            include (List[str], optional): Request that the response include
                the total count by specifying `include=["total_count"]`.

        Returns:
            BuckslipsResponse: Response from the API. Returns a list of
                buckslip objects

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/buckslips')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('limit')
                         .value(limit))
            .query_param(Parameter()
                         .key('before/after')
                         .value(before_after))
            .query_param(Parameter()
                         .key('include')
                         .value(include))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('basicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(BuckslipsResponse.from_dictionary)
            .local_error('default', 'Error', Domains0Error1Exception)
        ).execute()

    def buckslip_create(self,
                        body):
        """Does a POST request to /buckslips.

        Creates a new buckslip given information

        Args:
            body (BuckslipEditable): TODO: type description here.

        Returns:
            Buckslip: Response from the API. Buckslip created successfully

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/buckslips')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('basicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Buckslip.from_dictionary)
            .local_error('default', 'Error', Domains0Error1Exception)
        ).execute()

    def buckslip_retrieve(self,
                          buckslip_id):
        """Does a GET request to /buckslips/{buckslip_id}.

        Retrieves the details of an existing buckslip. You need only supply
        the unique customer identifier that was returned upon buckslip
        creation.

        Args:
            buckslip_id (str): id of the buckslip

        Returns:
            Buckslip: Response from the API. Returns a buckslip object

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/buckslips/{buckslip_id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('buckslip_id')
                            .value(buckslip_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('basicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Buckslip.from_dictionary)
            .local_error('default', 'Error', Domains0Error1Exception)
        ).execute()

    def buckslip_update(self,
                        buckslip_id,
                        content_type,
                        description=None,
                        auto_reorder=None,
                        reorder_quantity=None):
        """Does a PATCH request to /buckslips/{buckslip_id}.

        Update the details of an existing buckslip. You need only supply the
        unique identifier that was returned upon buckslip creation.

        Args:
            buckslip_id (str): id of the buckslip
            content_type (ContentTypeEnum): TODO: type description here.
            description (str, optional): Description of the buckslip.
            auto_reorder (bool, optional): Allows for auto reordering
            reorder_quantity (float, optional): The quantity of items to be
                reordered (only required when auto_reorder is true).

        Returns:
            Buckslip: Response from the API. Returns a buckslip object

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/buckslips/{buckslip_id}')
            .http_method(HttpMethodEnum.PATCH)
            .template_param(Parameter()
                            .key('buckslip_id')
                            .value(buckslip_id)
                            .should_encode(True))
            .form_param(Parameter()
                        .key('description')
                        .value(description))
            .form_param(Parameter()
                        .key('auto_reorder')
                        .value(auto_reorder))
            .form_param(Parameter()
                        .key('reorder_quantity')
                        .value(reorder_quantity))
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
            .deserialize_into(Buckslip.from_dictionary)
            .local_error('default', 'Error', Domains0Error1Exception)
        ).execute()

    def buckslip_delete(self,
                        buckslip_id):
        """Does a DELETE request to /buckslips/{buckslip_id}.

        Delete an existing buckslip. You need only supply the unique
        identifier that was returned upon buckslip creation.

        Args:
            buckslip_id (str): id of the buckslip

        Returns:
            BuckslipsResponse1: Response from the API. Deleted the buckslip

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/buckslips/{buckslip_id}')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('buckslip_id')
                            .value(buckslip_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('basicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(BuckslipsResponse1.from_dictionary)
            .local_error('default', 'Error', Domains0Error1Exception)
        ).execute()
