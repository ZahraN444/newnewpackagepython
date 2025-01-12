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
from lob.models.beforeafter import Beforeafter
from lob.models.card_editable import CardEditable


class CardsControllerTests(ControllerTestBase):

    controller = None

    @classmethod
    def setUpClass(cls):
        super(CardsControllerTests, cls).setUpClass()
        cls.controller = cls.client.cards
        cls.response_catcher = cls.controller.http_call_back

    # Returns a list of your cards. The cards are returned sorted by creation date, with the most recently created addresses appearing first.
    def test_cards_list(self):
        # Parameters for the API call
        limit = 10
        before_after = None
        include = None

        # Perform the API call through the SDK function
        result = self.controller.cards_list(limit, before_after, include)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"data":[{"id":"card_7a6d73c5c8457fc","account_id":"fa9ea650fc7b31'
            'a89f92","description":null,"url":"https://lob-assets.com/cards/car'
            'd_c51ae96f5cebf3e.pdf?version=v1&expires=1636910992&signature=mnsD'
            'H2DAxdkN9VibdlLMxJC86sME5WYDqkNtmvGwdNsAaUWfbnv0rJhJ1mR8Ol4uxQq61j'
            '5wYZ0r3s-lBkQfDA","size":"2.125x3.375","auto_reorder":false,"reord'
            'er_quantity":null,"raw_url":"https://lob-assets.com/cards/card_c51'
            'ae96f5cebf3e_raw.pdf?version=v1&expires=1636910992&signature=-bZo3'
            '1FMAp2vmNaZKyXn_Qa4APqwtNinw76FrQ7uyQejFZw6VBQQYfoiQ642iXh0H2K5i2a'
            'Oo8_BAkt3UJdVDw","front_original_url":"https://lob-assets.com/card'
            's/card_c51ae96f5cebf3e_raw.pdf?version=v1&expires=1636910992&signa'
            'ture=-bZo31FMAp2vmNaZKyXn_Qa4APqwtNinw76FrQ7uyQejFZw6VBQQYfoiQ642i'
            'Xh0H2K5i2aOo8_BAkt3UJdVDw","back_original_url":"https://lob-assets'
            '.com/cards/card_c51ae96f5cebf3e_raw.pdf?version=v1&expires=1636910'
            '992&signature=-bZo31FMAp2vmNaZKyXn_Qa4APqwtNinw76FrQ7uyQejFZw6VBQQ'
            'YfoiQ642iXh0H2K5i2aOo8_BAkt3UJdVDw","thumbnails":[{"small":"https:'
            '//lob-assets.com/cards/card_c51ae96f5cebf3e_thumb_small_1.png?vers'
            'ion=v1&expires=1636910992&signature=mrv8JDvpZK4I8WUGH0tPdtK-My5oes'
            '0Ltj_gL7BDw96SpCTTeZFHkz81SzclyFP9dQRtlsvAsjcuGcTBvCvOCg","medium"'
            ':"https://lob-assets.com/cards/card_c51ae96f5cebf3e_thumb_medium_1'
            '.png?version=v1&expires=1636910992&signature=VgL_2Ckm_kxKiWGgWtdNo'
            'y9HHOn8dGYSVOn7UqyCbwdbVlUtx28TRN4Bo8Iru3n0keKp9He0YhKT1ILotznMDA"'
            ',"large":"https://lob-assets.com/cards/card_c51ae96f5cebf3e_thumb_'
            'large_1.png?version=v1&expires=1636910992&signature=FKSzymA13j-CQ0'
            'uk20cGHZTzT3vimzNBYrgp-xifLFg4mMdo1BZALR5O0aF_jVhsX614hKP35ONdYl47'
            'TQxXAw"}],"available_quantity":10000,"pending_quantity":0,"countri'
            'es":null,"status":"rendered","mode":"test","orientation":"horizont'
            'al","threshold_amount":0,"date_created":"2021-03-24T22:51:42.838Z"'
            ',"date_modified":"2021-03-24T22:51:42.838Z","send_date":"2021-03-2'
            '4T22:51:42.838Z","object":"card"}],"object":"list","previous_url":'
            'null,"next_url":null,"count":1}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

    # Creates a new card given information
    def test_card_create(self):
        # Parameters for the API call
        body = APIHelper.json_deserialize('{"description":"Test card","front":"https://s3-us-west-2.amazonaws'
            '.com/public.lob.com/assets/card_horizontal.pdf","back":"https://s3'
            '-us-west-2.amazonaws.com/public.lob.com/assets/card_horizontal.pdf'
            '","size":"2.125x3.375"}', CardEditable.from_dictionary)

        # Perform the API call through the SDK function
        result = self.controller.card_create(body)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"id":"card_7a6d73c5c8457fc","account_id":"fa9ea650fc7b31a89f92","'
            'description":"Test card","url":"https://lob-assets.com/cards/card_'
            'c51ae96f5cebf3e.pdf?version=v1&expires=1636910992&signature=mnsDH2'
            'DAxdkN9VibdlLMxJC86sME5WYDqkNtmvGwdNsAaUWfbnv0rJhJ1mR8Ol4uxQq61j5w'
            'YZ0r3s-lBkQfDA","size":"2.125x3.375","auto_reorder":false,"reorder'
            '_quantity":null,"raw_url":"https://lob-assets.com/cards/card_c51ae'
            '96f5cebf3e_raw.pdf?version=v1&expires=1636910992&signature=-bZo31F'
            'MAp2vmNaZKyXn_Qa4APqwtNinw76FrQ7uyQejFZw6VBQQYfoiQ642iXh0H2K5i2aOo'
            '8_BAkt3UJdVDw","front_original_url":"https://lob-assets.com/cards/'
            'card_c51ae96f5cebf3e_raw.pdf?version=v1&expires=1636910992&signatu'
            're=-bZo31FMAp2vmNaZKyXn_Qa4APqwtNinw76FrQ7uyQejFZw6VBQQYfoiQ642iXh'
            '0H2K5i2aOo8_BAkt3UJdVDw","back_original_url":"https://lob-assets.c'
            'om/cards/card_c51ae96f5cebf3e_raw.pdf?version=v1&expires=163691099'
            '2&signature=-bZo31FMAp2vmNaZKyXn_Qa4APqwtNinw76FrQ7uyQejFZw6VBQQYf'
            'oiQ642iXh0H2K5i2aOo8_BAkt3UJdVDw","thumbnails":[{"small":"https://'
            'lob-assets.com/cards/card_c51ae96f5cebf3e_thumb_small_1.png?versio'
            'n=v1&expires=1636910992&signature=mrv8JDvpZK4I8WUGH0tPdtK-My5oes0L'
            'tj_gL7BDw96SpCTTeZFHkz81SzclyFP9dQRtlsvAsjcuGcTBvCvOCg","medium":"'
            'https://lob-assets.com/cards/card_c51ae96f5cebf3e_thumb_medium_1.p'
            'ng?version=v1&expires=1636910992&signature=VgL_2Ckm_kxKiWGgWtdNoy9'
            'HHOn8dGYSVOn7UqyCbwdbVlUtx28TRN4Bo8Iru3n0keKp9He0YhKT1ILotznMDA","'
            'large":"https://lob-assets.com/cards/card_c51ae96f5cebf3e_thumb_la'
            'rge_1.png?version=v1&expires=1636910992&signature=FKSzymA13j-CQ0uk'
            '20cGHZTzT3vimzNBYrgp-xifLFg4mMdo1BZALR5O0aF_jVhsX614hKP35ONdYl47TQ'
            'xXAw"},{"small":"https://lob-assets.com/cards/card_c51ae96f5cebf3e'
            '_thumb_small_2.png?version=v1&expires=1636910992&signature=IWsmPa_'
            'ULlv2yyqjX564d_YfHHY_M7i9YxDnw-WXDr2jtOFcArmRZQbnHeE9g_rYxnddJbgos'
            'uv8-c2utiu7Cg","medium":"https://lob-assets.com/cards/card_c51ae96'
            'f5cebf3e_thumb_medium_2.png?version=v1&expires=1636910992&signatur'
            'e=zxK7VKGiTvz5Ywrkaydd0v3GcYf58R7A08J4tNfI7-aiNODDcTF3l0MqY13n9Pyc'
            '8RXSdD0XVBY-OpbA1VM-Ag","large":"https://lob-assets.com/cards/card'
            '_c51ae96f5cebf3e_thumb_large_2.png?version=v1&expires=1636910992&s'
            'ignature=r0OFUhh315ZwN0raMZdIwJd2oCIEYsz0BABaMxIuO1PKTD0ckGWrhcGdz'
            'k2dlWQ6vSvp0CUQ5k1RXGqkIIqkDw"}],"available_quantity":10000,"pendi'
            'ng_quantity":0,"countries":null,"status":"rendered","mode":"test",'
            '"orientation":"horizontal","threshold_amount":0,"date_created":"20'
            '21-03-24T22:51:42.838Z","date_modified":"2021-03-24T22:51:42.838Z"'
            ',"send_date":"2021-03-24T22:51:42.838Z","object":"card"}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

