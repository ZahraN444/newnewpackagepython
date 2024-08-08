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
from lob.models.all_checks import AllChecks
from lob.models.check import Check
from lob.models.checks_response import ChecksResponse
from lob.exceptions.domains_0_error_1_exception import Domains0Error1Exception


class ChecksController(BaseController):

    """A Controller to access Endpoints in the lob API."""
    def __init__(self, config):
        super(ChecksController, self).__init__(config)

    def checks_list(self,
                    limit=10,
                    before_after=None,
                    include=None,
                    date_created=None,
                    metadata=None,
                    scheduled=None,
                    send_date=None,
                    mail_type=None,
                    sort_by=None):
        """Does a GET request to /checks.

        Returns a list of your checks. The checks are returned sorted by
        creation date, with the most recently created checks appearing first.

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
            scheduled (bool, optional): * `true` - only return orders (past or
                future) where `send_date` is greater than `date_created` *
                `false` - only return orders where `send_date` is equal to
                `date_created`
            send_date (object, optional): Filter by ISO-8601 date or datetime,
                e.g. `{ "gt": "2012-01-01", "lt": "2012-01-31T12:34:56Z" }`
                where `gt` is >, `lt` is <, `gte` is ≥, and `lte` is ≤.
            mail_type (MailTypeEnum, optional): A string designating the mail
                postage type: * `usps_first_class` - (default) *
                `usps_standard` - a <a
                href="https://lob.com/pricing/print-mail#compare"
                target="_blank">cheaper option</a> which is less predictable
                and takes longer to deliver. `usps_standard` cannot be used
                with `4x6` postcards or for any postcards sent outside of the
                United States.
            sort_by (SortBy1, optional): Sorts items by ascending or
                descending dates. Use either `date_created` or `send_date`,
                not both.

        Returns:
            AllChecks: Response from the API. A dictionary with a data
                property that contains an array of up to `limit` checks. Each
                entry in the array is a separate check. The previous and next
                page of checks can be retrieved by calling the endpoint
                contained in the `previous_url` and `next_url` fields in the
                API response respectively.<br>If no more checks are available
                beyond the current set of returned results, the `next_url`
                field will be empty.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/checks')
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
            .query_param(Parameter()
                         .key('scheduled')
                         .value(scheduled))
            .query_param(Parameter()
                         .key('send_date')
                         .value(send_date))
            .query_param(Parameter()
                         .key('mail_type')
                         .value(mail_type))
            .query_param(Parameter()
                         .key('sort_by')
                         .value(sort_by))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('basicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(AllChecks.from_dictionary)
            .local_error('default', 'Error', Domains0Error1Exception)
        ).execute()

    def check_create(self,
                     body,
                     idempotency_key=None,
                     idempotency_key_2=None):
        """Does a POST request to /checks.

        Creates a new check with the provided properties.

        Args:
            body (object): TODO: type description here.
            idempotency_key (str, optional): A string of no longer than 256
                characters that uniquely identifies this resource. For more
                help integrating idempotency keys, refer to our <a
                href="https://help.lob.com/print-and-mail/building-a-mail-strat
                egy/managing-mail-settings#idempotent-requests-12"
                target="_blank">implementation guide</a>.
            idempotency_key_2 (str, optional): A string of no longer than 256
                characters that uniquely identifies this resource. For more
                help integrating idempotency keys, refer to our <a
                href="https://help.lob.com/print-and-mail/building-a-mail-strat
                egy/managing-mail-settings#idempotent-requests-12"
                target="_blank">implementation guide</a>.

        Returns:
            Check: Response from the API. Returns a check object

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/checks')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('Idempotency-Key')
                          .value(idempotency_key))
            .query_param(Parameter()
                         .key('idempotency_key2')
                         .value(idempotency_key_2))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('basicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Check.from_dictionary)
            .local_error('default', 'Error', Domains0Error1Exception)
        ).execute()

    def check_retrieve(self,
                       chk_id):
        """Does a GET request to /checks/{chk_id}.

        Retrieves the details of an existing check. You need only supply the
        unique check identifier that was returned upon check creation.

        Args:
            chk_id (str): id of the check

        Returns:
            Check: Response from the API. Returns a check object

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/checks/{chk_id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('chk_id')
                            .value(chk_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('basicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Check.from_dictionary)
            .local_error('default', 'Error', Domains0Error1Exception)
        ).execute()

    def check_cancel(self,
                     chk_id):
        """Does a DELETE request to /checks/{chk_id}.

        Completely removes a check from production. This can only be done if
        the check has a `send_date` and the `send_date` has not yet passed. If
        the check is successfully canceled, you will not be charged for it.
        Read more on [cancellation windows](#section/Cancellation-Windows) and
        [scheduling](#section/Scheduled-Mailings). Scheduling and cancellation
        is a premium feature. Upgrade to the appropriate <a
        href="https://dashboard.lob.com/#/settings/editions"
        target="_blank">Print & Mail Edition</a> to gain access.

        Args:
            chk_id (str): id of the check

        Returns:
            ChecksResponse: Response from the API. Deleted

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/checks/{chk_id}')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('chk_id')
                            .value(chk_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('basicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ChecksResponse.from_dictionary)
            .local_error('default', 'Error', Domains0Error1Exception)
        ).execute()
