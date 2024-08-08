# -*- coding: utf-8 -*-

"""
lob

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

import json

from tests.controllers.controller_test_base import ControllerTestBase
from apimatic_core.utilities.comparison_helper import ComparisonHelper
from lob.api_helper import APIHelper


class QRCodesControllerTests(ControllerTestBase):

    controller = None

    @classmethod
    def setUpClass(cls):
        super(QRCodesControllerTests, cls).setUpClass()
        cls.controller = cls.client.qr_codes
        cls.response_catcher = cls.controller.http_call_back

    # Returns a list of your QR codes. The QR codes are returned sorted by scan date, with the most recently scanned QR codes appearing first.
    def test_qr_codes_list(self):
        # Parameters for the API call
        limit = 10
        offset = 0
        include = None
        date_created = None
        scanned = None
        resource_ids = None

        # Perform the API call through the SDK function
        result = self.controller.qr_codes_list(limit, offset, include, date_created, scanned, resource_ids)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"data":[{"resource_id":"ltr_d5a5a89da9106f8","date_created":"2019'
            '-07-27T23:49:01.511Z","number_of_scans":2,"scans":[{"ip_location":'
            '"127.0.0.1","scan_date":"2022-07-27T23:49:01.511Z"},{"ip_location"'
            ':"127.0.0.1","scan_date":"2022-07-29T23:45:00.436Z"}]},{"resource_'
            'id":"psc_d5a5a89da9106f8","date_created":"2022-09-27T23:49:01.511Z'
            '","number_of_scans":1,"scans":[{"ip_location":"127.0.0.1","scan_da'
            'te":"2022-09-27T23:49:01.511Z"}]}],"object":"list","count":2,"scan'
            'ned_count":2,"total_count":2}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

