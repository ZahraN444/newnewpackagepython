# -*- coding: utf-8 -*-

"""
lob

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from lob.api_helper import APIHelper
from lob.configuration import Server
from lob.utilities.file_wrapper import FileWrapper
from lob.controllers.base_controller import BaseController
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from lob.http.http_method_enum import HttpMethodEnum
from apimatic_core.authentication.multiple.single_auth import Single
from lob.models.all_campaigns import AllCampaigns
from lob.models.campaign import Campaign
from lob.models.campaigns_response_4 import CampaignsResponse4
from lob.exceptions.domains_0_error_1_exception import Domains0Error1Exception


class CampaignsController(BaseController):

    """A Controller to access Endpoints in the lob API."""
    def __init__(self, config):
        super(CampaignsController, self).__init__(config)

    def campaigns_list(self,
                       limit=10,
                       include=None,
                       before_after=None):
        """Does a GET request to /campaigns.

        Returns a list of your campaigns. The campaigns are returned sorted by
        creation date, with the most recently created campaigns appearing
        first.

        Args:
            limit (int, optional): How many results to return.
            include (List[str], optional): Request that the response include
                the total count by specifying `include=["total_count"]`.
            before_after (Beforeafter, optional): `before` and `after` are
                both optional but only one of them can be in the query at a
                time.

        Returns:
            AllCampaigns: Response from the API. A dictionary with a data
                property that contains an array of up to `limit` campaigns.
                Each entry in the array is a separate campaign. The previous
                and next page of campaigns can be retrieved by calling the
                endpoint contained in the `previous_url` and `next_url` fields
                in the API response respectively.<br>If no more campaigns are
                available beyond the current set of returned results, the
                `next_url` field will be empty.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/campaigns')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('limit')
                         .value(limit))
            .query_param(Parameter()
                         .key('include')
                         .value(include))
            .query_param(Parameter()
                         .key('before/after')
                         .value(before_after))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('basicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(AllCampaigns.from_dictionary)
        ).execute()

    def campaign_create(self,
                        content_type,
                        name,
                        schedule_type,
                        use_type,
                        x_lang_output=None,
                        billing_group_id=None,
                        description=None,
                        target_delivery_date=None,
                        send_date=None,
                        cancel_window_campaign_minutes=None,
                        metadata=None,
                        auto_cancel_if_ncoa=None):
        """Does a POST request to /campaigns.

        Creates a new campaign with the provided properties. See how to launch
        your first campaign
        [here](https://help.lob.com/print-and-mail/building-a-mail-strategy/cam
        paign-or-triggered-sends/launch-your-first-campaign).

        Args:
            content_type (ContentTypeEnum): TODO: type description here.
            name (str): Name of the campaign.
            schedule_type (CmpScheduleTypeEnum): TODO: type description here.
            use_type (typing.BinaryIO): TODO: type description here.
            x_lang_output (XLangOutput1Enum, optional): * `native` - Translate
                response to the native language of the country in the request
                * `match` - match the response to the language in the request 
                Default response is in English.
            billing_group_id (str, optional): Unique identifier prefixed with
                `bg_`.
            description (str, optional): An internal description that
                identifies this resource. Must be no longer than 255
                characters.
            target_delivery_date (datetime, optional): If `schedule_type` is
                `target_delivery_date`, provide a targeted delivery date for
                mail pieces in this campaign.
            send_date (datetime, optional): If `schedule_type` is
                `scheduled_send_date`, provide a date to send this campaign.
            cancel_window_campaign_minutes (int, optional): A window, in
                minutes, within which the campaign can be canceled.
            metadata (Dict[str, str], optional): Use metadata to store custom
                information for tagging and labeling back to your internal
                systems. Must be an object with up to 20 key-value pairs. Keys
                must be at most 40 characters and values must be at most 500
                characters. Neither can contain the characters `"` and `\`.
                i.e. '{"customer_id" : "NEWYORK2015"}' Nested objects are not
                supported.  See [Metadata](#section/Metadata) for more
                information.
            auto_cancel_if_ncoa (bool, optional): Whether or not a mail piece
                should be automatically canceled and not sent if the address
                is updated via NCOA.

        Returns:
            Campaign: Response from the API. Campaign created successfully

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/campaigns')
            .http_method(HttpMethodEnum.POST)
            .form_param(Parameter()
                        .key('name')
                        .value(name))
            .form_param(Parameter()
                        .key('schedule_type')
                        .value(schedule_type))
            .multipart_param(Parameter()
                             .key('use_type')
                             .value(use_type)
                             .default_content_type('application/octet-stream'))
            .header_param(Parameter()
                          .key('x-lang-output')
                          .value(x_lang_output))
            .form_param(Parameter()
                        .key('billing_group_id')
                        .value(billing_group_id))
            .form_param(Parameter()
                        .key('description')
                        .value(description))
            .form_param(Parameter()
                        .key('target_delivery_date')
                        .value(APIHelper.when_defined(APIHelper.RFC3339DateTime, target_delivery_date)))
            .form_param(Parameter()
                        .key('send_date')
                        .value(APIHelper.when_defined(APIHelper.RFC3339DateTime, send_date)))
            .form_param(Parameter()
                        .key('cancel_window_campaign_minutes')
                        .value(cancel_window_campaign_minutes))
            .form_param(Parameter()
                        .key('metadata')
                        .value(metadata))
            .form_param(Parameter()
                        .key('auto_cancel_if_ncoa')
                        .value(auto_cancel_if_ncoa))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('basicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Campaign.from_dictionary)
            .local_error('default', 'Error', Domains0Error1Exception)
        ).execute()

    def campaign_retrieve(self,
                          cmp_id):
        """Does a GET request to /campaigns/{cmp_id}.

        Retrieves the details of an existing campaign. You need only supply
        the unique campaign identifier that was returned upon campaign
        creation.

        Args:
            cmp_id (str): id of the campaign

        Returns:
            Campaign: Response from the API. Returns a campaign object

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/campaigns/{cmp_id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('cmp_id')
                            .value(cmp_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('basicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Campaign.from_dictionary)
            .local_error('default', 'Error', Domains0Error1Exception)
        ).execute()

    def campaign_update(self,
                        cmp_id,
                        content_type,
                        name=None,
                        description=None,
                        schedule_type=None,
                        target_delivery_date=None,
                        send_date=None,
                        cancel_window_campaign_minutes=None,
                        metadata=None,
                        is_draft=None,
                        use_type=None,
                        auto_cancel_if_ncoa=None):
        """Does a PATCH request to /campaigns/{cmp_id}.

        Update the details of an existing campaign. You need only supply the
        unique identifier that was returned upon campaign creation.

        Args:
            cmp_id (str): id of the campaign
            content_type (ContentTypeEnum): TODO: type description here.
            name (str, optional): TODO: type description here.
            description (str, optional): An internal description that
                identifies this resource. Must be no longer than 255
                characters.
            schedule_type (CmpScheduleTypeEnum, optional): TODO: type
                description here.
            target_delivery_date (datetime, optional): If `schedule_type` is
                `target_delivery_date`, provide a targeted delivery date for
                mail pieces in this campaign.
            send_date (datetime, optional): If `schedule_type` is
                `scheduled_send_date`, provide a date to send this campaign.
            cancel_window_campaign_minutes (int, optional): A window, in
                minutes, within which the campaign can be canceled.
            metadata (Dict[str, str], optional): Use metadata to store custom
                information for tagging and labeling back to your internal
                systems. Must be an object with up to 20 key-value pairs. Keys
                must be at most 40 characters and values must be at most 500
                characters. Neither can contain the characters `"` and `\`.
                i.e. '{"customer_id" : "NEWYORK2015"}' Nested objects are not
                supported.  See [Metadata](#section/Metadata) for more
                information.
            is_draft (bool, optional): Whether or not the campaign is still a
                draft. Can either be excluded or `false`.
            use_type (typing.BinaryIO, optional): TODO: type description
                here.
            auto_cancel_if_ncoa (bool, optional): Whether or not a mail piece
                should be automatically canceled and not sent if the address
                is updated via NCOA.

        Returns:
            Campaign: Response from the API. Returns a campaign object

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/campaigns/{cmp_id}')
            .http_method(HttpMethodEnum.PATCH)
            .template_param(Parameter()
                            .key('cmp_id')
                            .value(cmp_id)
                            .should_encode(True))
            .form_param(Parameter()
                        .key('name')
                        .value(name))
            .form_param(Parameter()
                        .key('description')
                        .value(description))
            .form_param(Parameter()
                        .key('schedule_type')
                        .value(schedule_type))
            .form_param(Parameter()
                        .key('target_delivery_date')
                        .value(APIHelper.when_defined(APIHelper.RFC3339DateTime, target_delivery_date)))
            .form_param(Parameter()
                        .key('send_date')
                        .value(APIHelper.when_defined(APIHelper.RFC3339DateTime, send_date)))
            .form_param(Parameter()
                        .key('cancel_window_campaign_minutes')
                        .value(cancel_window_campaign_minutes))
            .form_param(Parameter()
                        .key('metadata')
                        .value(metadata))
            .form_param(Parameter()
                        .key('is_draft')
                        .value(is_draft))
            .multipart_param(Parameter()
                             .key('use_type')
                             .value(use_type)
                             .default_content_type('application/octet-stream'))
            .form_param(Parameter()
                        .key('auto_cancel_if_ncoa')
                        .value(auto_cancel_if_ncoa))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('basicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Campaign.from_dictionary)
            .local_error('default', 'Error', Domains0Error1Exception)
        ).execute()

    def campaign_delete(self,
                        cmp_id):
        """Does a DELETE request to /campaigns/{cmp_id}.

        Delete an existing campaign. You need only supply the unique
        identifier that was returned upon campaign creation. Deleting a
        campaign also deletes any associated mail pieces that have been
        created but not sent. A campaign's `send_date` matches its associated
        mail pieces' `send_date`s.

        Args:
            cmp_id (str): id of the campaign

        Returns:
            CampaignsResponse4: Response from the API. Deleted the campaign.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/campaigns/{cmp_id}')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('cmp_id')
                            .value(cmp_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('basicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(CampaignsResponse4.from_dictionary)
            .local_error('default', 'Error', Domains0Error1Exception)
        ).execute()

    def campaign_send(self,
                      cmp_id):
        """Does a POST request to /campaigns/{cmp_id}/send.

        Sends a campaign. You need only supply the unique campaign identifier
        that was returned upon campaign creation.

        Args:
            cmp_id (str): id of the campaign

        Returns:
            Campaign: Response from the API. Returns a campaign object

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/campaigns/{cmp_id}/send')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('cmp_id')
                            .value(cmp_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('basicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Campaign.from_dictionary)
            .local_error('default', 'Error', Domains0Error1Exception)
        ).execute()
