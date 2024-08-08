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


class UploadsControllerTests(ControllerTestBase):

    controller = None

    @classmethod
    def setUpClass(cls):
        super(UploadsControllerTests, cls).setUpClass()
        cls.controller = cls.client.uploads
        cls.response_catcher = cls.controller.http_call_back

    # Returns a list of your uploads. Optionally, filter uploads by campaign.
    def test_uploads_list(self):
        # Parameters for the API call
        campaign_id = None

        # Perform the API call through the SDK function
        result = self.controller.uploads_list(campaign_id)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('[{"id":"upl_71be866e430b11e9","accountId":"fa9ea650fc7b31a89f92","'
            'campaignId":"cmp_1933ad629bae1408","mode":"test","failuresUrl":"ht'
            'tps://www.example.com","originalFilename":"my_audience.csv","state'
            '":"Draft","totalMailpieces":100,"failedMailpieces":5,"validatedMai'
            'lpieces":95,"bytesProcessed":17268,"dateCreated":"2017-09-05T17:47'
            ':53.767Z","dateModified":"2017-09-05T17:47:53.767Z","requiredAddre'
            'ssColumnMapping":{"name":"recipient_name","address_line1":"primary'
            '_line","address_city":"city","address_state":"state","address_zip"'
            ':"zip_code"},"optionalAddressColumnMapping":{"address_line2":"seco'
            'ndary_line","company":"company","address_country":"country"},"merg'
            'eVariableColumnMapping":{"gift_code":"code"},"metadata":{"columns"'
            ':["recipient_name","zip_code"]}}]')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

