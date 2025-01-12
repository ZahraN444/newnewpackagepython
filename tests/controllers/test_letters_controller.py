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
from lob.models.sort_by_1 import SortBy1


class LettersControllerTests(ControllerTestBase):

    controller = None

    @classmethod
    def setUpClass(cls):
        super(LettersControllerTests, cls).setUpClass()
        cls.controller = cls.client.letters
        cls.response_catcher = cls.controller.http_call_back

    # Returns a list of your letters. The letters are returned sorted by creation date, with the most recently created letters appearing first.
    def test_letters_list(self):
        # Parameters for the API call
        limit = 10
        before_after = None
        include = None
        date_created = None
        metadata = None
        color = None
        scheduled = None
        send_date = None
        mail_type = None
        sort_by = None

        # Perform the API call through the SDK function
        result = self.controller.letters_list(limit, before_after, include, date_created, metadata, color, scheduled, send_date, mail_type, sort_by)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"data":[{"id":"ltr_5ba44b462c79f07c","description":"Demo Letter",'
            '"metadata":{},"to":{"id":"adr_asdi2y3riuasasoi","description":"Har'
            'ry - Office","name":"Harry Zhang","company":"Lob","phone":"5555555'
            '555","email":"harry@lob.com","metadata":{},"address_line1":"370 WA'
            'TER ST","address_line2":"","address_city":"SUMMERSIDE","address_st'
            'ate":"PRINCE EDWARD ISLAND","address_zip":"C1N 1C4","address_count'
            'ry":"CANADA","recipient_moved":false,"date_created":"2019-09-20T00'
            ':14:00.361Z","date_modified":"2019-09-20T00:14:00.361Z","object":"'
            'address"},"from":{"id":"adr_210a8d4b0b76d77b","description":null,"'
            'name":"LEORE AVIDAR","company":null,"phone":null,"email":null,"add'
            'ress_line1":"210 KING ST STE 6100","address_line2":null,"address_c'
            'ity":"SAN FRANCISCO","address_state":"CA","address_zip":"94107-174'
            '1","address_country":"UNITED STATES","metadata":{},"date_created":'
            '"2018-12-08T03:01:07.651Z","date_modified":"2018-12-08T03:01:07.65'
            '1Z","object":"address"},"color":true,"double_sided":false,"address'
            '_placement":"top_first_page","return_envelope":false,"perforated_p'
            'age":null,"extra_service":"certified","custom_envelope":null,"temp'
            'late_id":"tmpl_a","template_version_id":"vrsn_a","mail_type":"usps'
            '_first_class","url":"https://lob-assets.com/letters/ltr_5ba44b462c'
            '79f07c.pdf?version=v1&expires=1568239830&signature=Ob-DUPLJLM4scWQ'
            'eCDNadPJ4j33MZw16pykOxwv2us-bA7utTYi6oZ8WrEtBYDBBo09XkapR3gdJf0NEr'
            '90xAA","merge_variables":null,"carrier":"USPS","tracking_number":"'
            '92071902358909000011275538","tracking_events":[{"id":"evnt_9e84094'
            'c9368cfb","type":"certified","name":"Delivered","details":{"event"'
            ':"delivered","description":"Package has been delivered.","notes":"'
            'Delivered, Front Desk/Reception/Mail Room","action_required":false'
            '},"location":"33408","time":"2019-10-08T19:41:00Z","date_created":'
            '"2019-10-08T19:41:00Z","date_modified":"2019-10-08T19:41:00Z","obj'
            'ect":"tracking_event"}],"thumbnails":[{"small":"https://lob-assets'
            '.com/letters/ltr_5ba44b462c79f07c_thumb_small_1.png?version=v1&exp'
            'ires=1568239830&signature=xZUmE8rq8wSECHPEb9c37cUDZBzGUO3XK5LsIPZh'
            'I6dOXgm6zJEn8_7tKuZ3JWBmvNJNXdTl_ufkNu4avjQUDw","medium":"https://'
            'lob-assets.com/letters/ltr_5ba44b462c79f07c_thumb_medium_1.png?ver'
            'sion=v1&expires=1568239830&signature=H7354Qpcm9S4aXbrMsBe6QJ6lSNi9'
            'IWPgMJtLWLi4Kyx9tHF8Mp9YEc_IL9x89Jfw4-yRzKDXA410X4W0PssBQ","large"'
            ':"https://lob-assets.com/letters/ltr_5ba44b462c79f07c_thumb_large_'
            '1.png?version=v1&expires=1568239830&signature=54LUIDKZyItA9pnC87d1'
            'pJVAuw8bhKLCsMpNWkB3LgdVWxPxxb_c1IyIWAbSR-dyOYEOlDBCc40J4Kns-O_mAg'
            '"}],"expected_delivery_date":"2019-08-16","date_created":"2019-08-'
            '08T17:09:14.514Z","date_modified":"2019-08-08T17:09:16.850Z","send'
            '_date":"2019-08-08","use_type":"marketing","fsc":false,"object":"l'
            'etter"},{"id":"ltr_da8267c6a6545cd6","description":"Demo Letter","'
            'metadata":{},"to":{"id":"adr_210a8d4b0b76d77b","description":null,'
            '"name":"LEORE AVIDAR","company":null,"phone":null,"email":null,"ad'
            'dress_line1":"210 KING ST STE 6100","address_line2":null,"address_'
            'city":"SAN FRANCISCO","address_state":"CA","address_zip":"94107-17'
            '41","address_country":"UNITED STATES","metadata":{},"date_created"'
            ':"2018-12-08T03:01:07.651Z","date_modified":"2018-12-08T03:01:07.6'
            '51Z","object":"address"},"from":{"id":"adr_210a8d4b0b76d77b","desc'
            'ription":null,"name":"LEORE AVIDAR","company":null,"phone":null,"e'
            'mail":null,"address_line1":"210 KING ST STE 6100","address_line2":'
            'null,"address_city":"SAN FRANCISCO","address_state":"CA","address_'
            'zip":"94107-1741","address_country":"UNITED STATES","metadata":{},'
            '"date_created":"2018-12-08T03:01:07.651Z","date_modified":"2018-12'
            '-08T03:01:07.651Z","object":"address"},"color":true,"double_sided"'
            ':false,"address_placement":"top_first_page","return_envelope":fals'
            'e,"perforated_page":null,"extra_service":null,"custom_envelope":nu'
            'll,"mail_type":"usps_first_class","url":"https://lob-assets.com/le'
            'tters/ltr_da8267c6a6545cd6.pdf?version=v1&expires=1568239830&signa'
            'ture=HH-5RnbD4x0eJcnEC9HhqKSvQGsbkjovzvqSKgBijUHKIXwEKQJ4CbYhKs_U2'
            'q2A1k20Xefcaw7bfdPKozuqCQ","merge_variables":null,"carrier":"USPS"'
            ',"tracking_number":null,"tracking_events":[],"thumbnails":[{"small'
            '":"https://lob-assets.com/letters/ltr_da8267c6a6545cd6_thumb_small'
            '_1.png?version=v1&expires=1568239830&signature=C1Rs83187HpWGhsg_pJ'
            'IOhDIKlDtC_IgBBxHiocCEzJ8CncJwqrq5yHke-p97Dv7o81G_pfhFmirai589O6DC'
            'w","medium":"https://lob-assets.com/letters/ltr_da8267c6a6545cd6_t'
            'humb_medium_1.png?version=v1&expires=1568239830&signature=gz63l0yi'
            '3sK_sXjYfIVdLSvkknJFr_O5TWRulo_iKIgS-PosIl6J0tDR6bx_Tv5Ab_w7DABg3q'
            'dKZ846MZ7TCw","large":"https://lob-assets.com/letters/ltr_da8267c6'
            'a6545cd6_thumb_large_1.png?version=v1&expires=1568239830&signature'
            '=4Y1OIymaWkSO3aBIHCeshFAVnF-pDcF2FFqkx_jovaUFuk4FT1SI24L7_POwTRXQH'
            'lETMGlzkP_CGgqselRUAA"}],"expected_delivery_date":"2019-08-16","da'
            'te_created":"2019-08-08T17:08:12.224Z","date_modified":"2019-08-08'
            'T17:08:13.990Z","send_date":"2019-08-08T17:08:12.224Z","cards":nul'
            'l,"use_type":"marketing","fsc":true,"object":"letter"}],"object":"'
            'list","next_url":"https://api.lob.com/v1/letters?limit=2&after=eyJ'
            'kYXRlT2Zmc2V0IjoiMjAxOS0wOC0wOFQxNzowODoxMi4yMjRaIiwiaWRPZmZzZXQiO'
            'iJsdHJfZGE4MjY3YzZhNjU0NWNkNiJ9","previous_url":null,"count":2}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

