# -*- coding: utf-8 -*-

"""
lob

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class FailureStatusCodeEnum(object):

    """Implementation of the 'failure_status_code' enum.

    A conventional HTTP status code:
      * `401` - Authorization error with your API key or account
      * `403` - Forbidden error with your API key or account
      * `404` - The requested item does not exist
      * `413` - Payload too large
      * `422` - The query or body parameters did not pass validation
      * `429` - Too many requests have been sent with an API key in a given
      amount of time
      * `500` - An internal server error occurred, please contact
      support@lob.com

    Attributes:
        ENUM_401: TODO: type description here.
        ENUM_403: TODO: type description here.
        ENUM_404: TODO: type description here.
        ENUM_413: TODO: type description here.
        ENUM_422: TODO: type description here.
        ENUM_429: TODO: type description here.
        ENUM_500: TODO: type description here.

    """
    _all_values = [401, 403, 404, 413, 422, 429, 500]
    ENUM_401 = 401

    ENUM_403 = 403

    ENUM_404 = 404

    ENUM_413 = 413

    ENUM_422 = 422

    ENUM_429 = 429

    ENUM_500 = 500

    @classmethod
    def validate(cls, value):
        """Validates value contains in enum

        Args:
            value: the value to be validated

        Returns:
            boolean : if value is valid enum values.

        """
        return value in cls._all_values
   