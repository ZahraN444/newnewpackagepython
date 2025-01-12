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
from lob.models.creative import Creative
from lob.exceptions.domains_0_error_1_exception import Domains0Error1Exception


class CreativesController(BaseController):

    """A Controller to access Endpoints in the lob API."""
    def __init__(self, config):
        super(CreativesController, self).__init__(config)

    def creative_create(self,
                        body,
                        x_lang_output=None):
        """Does a POST request to /creatives.

        Creates a new creative with the provided properties

        Args:
            body (object): TODO: type description here.
            x_lang_output (XLangOutput1Enum, optional): * `native` - Translate
                response to the native language of the country in the request
                * `match` - match the response to the language in the request 
                Default response is in English.

        Returns:
            Creative: Response from the API. Creative created successfully

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/creatives')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('x-lang-output')
                          .value(x_lang_output))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('basicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Creative.from_dictionary)
            .local_error('default', 'Error', Domains0Error1Exception)
        ).execute()

    def creative_retrieve(self,
                          crv_id):
        """Does a GET request to /creatives/{crv_id}.

        Retrieves the details of an existing creative. You need only supply
        the unique creative identifier that was returned upon creative
        creation.

        Args:
            crv_id (str): id of the creative

        Returns:
            Creative: Response from the API. Returns a creative object

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/creatives/{crv_id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('crv_id')
                            .value(crv_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('basicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Creative.from_dictionary)
            .local_error('default', 'Error', Domains0Error1Exception)
        ).execute()

    def creative_update(self,
                        crv_id,
                        content_type,
                        mfrom=None,
                        description=None,
                        metadata=None):
        """Does a PATCH request to /creatives/{crv_id}.

        Update the details of an existing creative. You need only supply the
        unique identifier that was returned upon creative creation.

        Args:
            crv_id (str): id of the creative
            content_type (ContentTypeEnum): TODO: type description here.
            mfrom (typing.BinaryIO, optional): TODO: type description here.
            description (str, optional): An internal description that
                identifies this resource. Must be no longer than 255
                characters.
            metadata (Dict[str, str], optional): Use metadata to store custom
                information for tagging and labeling back to your internal
                systems. Must be an object with up to 20 key-value pairs. Keys
                must be at most 40 characters and values must be at most 500
                characters. Neither can contain the characters `"` and `\`.
                i.e. '{"customer_id" : "NEWYORK2015"}' Nested objects are not
                supported.  See [Metadata](#section/Metadata) for more
                information.

        Returns:
            Creative: Response from the API. Returns a creative object

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/creatives/{crv_id}')
            .http_method(HttpMethodEnum.PATCH)
            .template_param(Parameter()
                            .key('crv_id')
                            .value(crv_id)
                            .should_encode(True))
            .multipart_param(Parameter()
                             .key('from')
                             .value(mfrom)
                             .default_content_type('application/octet-stream'))
            .form_param(Parameter()
                        .key('description')
                        .value(description))
            .form_param(Parameter()
                        .key('metadata')
                        .value(metadata))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('basicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Creative.from_dictionary)
            .local_error('default', 'Error', Domains0Error1Exception)
        ).execute()
