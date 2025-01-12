# -*- coding: utf-8 -*-

"""
lob

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from lob.api_helper import APIHelper
from lob.configuration import Server
from lob.controllers.base_controller import BaseController
from lob.utilities.union_type_lookup import UnionTypeLookUp
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from lob.http.http_method_enum import HttpMethodEnum
from apimatic_core.authentication.multiple.single_auth import Single
from lob.models.all_addresses import AllAddresses
from lob.models.addresses_response_1 import AddressesResponse1
from lob.exceptions.domains_0_error_1_exception import Domains0Error1Exception


class AddressesController(BaseController):

    """A Controller to access Endpoints in the lob API."""
    def __init__(self, config):
        super(AddressesController, self).__init__(config)

    def addresses_list(self,
                       limit=10,
                       before_after=None,
                       include=None,
                       date_created=None,
                       metadata=None):
        """Does a GET request to /addresses.

        Returns a list of your addresses. The addresses are returned sorted by
        creation date, with the most recently created addresses appearing
        first.

        Args:
            limit (int, optional): How many results to return.
            before_after (Beforeafter, optional): `before` and `after` are
                both optional but only one of them can be in the query at a
                time.
            include (List[str], optional): Request that the response include
                the total count by specifying `include=["total_count"]`.
            date_created (Dict[str, str], optional): Filter by date created.
                Accepted formats are ISO-8601 date or datetime, e.g. `{ "gt":
                "2012-01-01", "lt": "2012-01-31T12:34:56Z" }` where `gt` is >,
                `lt` is <, `gte` is ≥, and `lte` is ≤.
            metadata (Dict[str, str], optional): Filter by metadata key-value
                pair`.

        Returns:
            AllAddresses: Response from the API. A dictionary with a data
                property that contains an array of up to `limit` addresses.
                Each entry in the array is a separate address object. The
                previous and next page of address entries can be retrieved by
                calling the endpoint contained in the `previous_url` and
                `next_url` fields in the API response respectively.<br>If no
                more addresses are available beyond the current set of
                returned results, the `next_url` field will be empty.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/addresses')
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
            .query_param(Parameter()
                         .key('date_created')
                         .value(date_created))
            .query_param(Parameter()
                         .key('metadata')
                         .value(metadata))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('basicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(AllAddresses.from_dictionary)
            .local_error('default', 'Error', Domains0Error1Exception)
        ).execute()

    def address_create(self,
                       body):
        """Does a POST request to /addresses.

        Creates a new address given information

        Args:
            body (object): TODO: type description here.

        Returns:
            object: Response from the API. Echos the writable fields of a
                newly created address object.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/addresses')
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
            .local_error('default', 'Error', Domains0Error1Exception)
        ).execute()

    def address_retrieve(self,
                         adr_id):
        """Does a GET request to /addresses/{adr_id}.

        Retrieves the details of an existing address. You need only supply the
        unique identifier that was returned upon address creation.

        Args:
            adr_id (str): id of the address

        Returns:
            AddressUs | AddressIntl: Response from the API. Returns an address
                object if a valid identifier was provided.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/addresses/{adr_id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('adr_id')
                            .value(adr_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('basicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(lambda value: APIHelper.deserialize_union_type(
                 UnionTypeLookUp.get('address'), value))
            .local_error('default', 'Error', Domains0Error1Exception)
        ).execute()

    def address_delete(self,
                       adr_id):
        """Does a DELETE request to /addresses/{adr_id}.

        Deletes the details of an existing address. You need only supply the
        unique identifier that was returned upon address creation.

        Args:
            adr_id (str): id of the address

        Returns:
            AddressesResponse1: Response from the API. Deleted

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/addresses/{adr_id}')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('adr_id')
                            .value(adr_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('basicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(AddressesResponse1.from_dictionary)
            .local_error('default', 'Error', Domains0Error1Exception)
        ).execute()
