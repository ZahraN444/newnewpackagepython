# -*- coding: utf-8 -*-

"""
lob

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from apimatic_core.configurations.global_configuration import GlobalConfiguration
from apimatic_core.decorators.lazy_property import LazyProperty
from lob.configuration import Configuration
from lob.controllers.base_controller import BaseController
from lob.configuration import Environment
from lob.http.auth.basic_auth import BasicAuth
from lob.controllers.addresses_controller import AddressesController
from lob.controllers.bank_accounts_controller import BankAccountsController
from lob.controllers.billing_groups_controller import BillingGroupsController
from lob.controllers.buckslip_orders_controller import BuckslipOrdersController
from lob.controllers.buckslips_controller import BuckslipsController
from lob.controllers.campaigns_controller import CampaignsController
from lob.controllers.card_orders_controller import CardOrdersController
from lob.controllers.cards_controller import CardsController
from lob.controllers.checks_controller import ChecksController
from lob.controllers.creatives_controller import CreativesController
from lob.controllers.identity_validation_controller\
    import IdentityValidationController
from lob.controllers.intl_autocompletions_controller\
    import IntlAutocompletionsController
from lob.controllers.intl_verifications_controller\
    import IntlVerificationsController
from lob.controllers.letters_controller import LettersController
from lob.controllers.postcards_controller import PostcardsController
from lob.controllers.qr_codes_controller import QRCodesController
from lob.controllers.reverse_geocode_lookups_controller\
    import ReverseGeocodeLookupsController
from lob.controllers.self_mailers_controller import SelfMailersController
from lob.controllers.template_versions_controller\
    import TemplateVersionsController
from lob.controllers.templates_controller import TemplatesController
from lob.controllers.uploads_controller import UploadsController
from lob.controllers.url_shortener_controller import URLShortenerController
from lob.controllers.us_autocompletions_controller\
    import USAutocompletionsController
from lob.controllers.us_verifications_controller\
    import USVerificationsController
from lob.controllers.zip_lookups_controller import ZipLookupsController


class LobClient(object):
    @LazyProperty
    def addresses(self):
        return AddressesController(self.global_configuration)

    @LazyProperty
    def bank_accounts(self):
        return BankAccountsController(self.global_configuration)

    @LazyProperty
    def billing_groups(self):
        return BillingGroupsController(self.global_configuration)

    @LazyProperty
    def buckslip_orders(self):
        return BuckslipOrdersController(self.global_configuration)

    @LazyProperty
    def buckslips(self):
        return BuckslipsController(self.global_configuration)

    @LazyProperty
    def campaigns(self):
        return CampaignsController(self.global_configuration)

    @LazyProperty
    def card_orders(self):
        return CardOrdersController(self.global_configuration)

    @LazyProperty
    def cards(self):
        return CardsController(self.global_configuration)

    @LazyProperty
    def checks(self):
        return ChecksController(self.global_configuration)

    @LazyProperty
    def creatives(self):
        return CreativesController(self.global_configuration)

    @LazyProperty
    def identity_validation(self):
        return IdentityValidationController(self.global_configuration)

    @LazyProperty
    def intl_autocompletions(self):
        return IntlAutocompletionsController(self.global_configuration)

    @LazyProperty
    def intl_verifications(self):
        return IntlVerificationsController(self.global_configuration)

    @LazyProperty
    def letters(self):
        return LettersController(self.global_configuration)

    @LazyProperty
    def postcards(self):
        return PostcardsController(self.global_configuration)

    @LazyProperty
    def qr_codes(self):
        return QRCodesController(self.global_configuration)

    @LazyProperty
    def reverse_geocode_lookups(self):
        return ReverseGeocodeLookupsController(self.global_configuration)

    @LazyProperty
    def self_mailers(self):
        return SelfMailersController(self.global_configuration)

    @LazyProperty
    def template_versions(self):
        return TemplateVersionsController(self.global_configuration)

    @LazyProperty
    def templates(self):
        return TemplatesController(self.global_configuration)

    @LazyProperty
    def uploads(self):
        return UploadsController(self.global_configuration)

    @LazyProperty
    def url_shortener(self):
        return URLShortenerController(self.global_configuration)

    @LazyProperty
    def us_autocompletions(self):
        return USAutocompletionsController(self.global_configuration)

    @LazyProperty
    def us_verifications(self):
        return USVerificationsController(self.global_configuration)

    @LazyProperty
    def zip_lookups(self):
        return ZipLookupsController(self.global_configuration)

    def __init__(self, http_client_instance=None,
                 override_http_client_configuration=False, http_call_back=None,
                 timeout=60, max_retries=0, backoff_factor=2,
                 retry_statuses=None, retry_methods=None,
                 environment=Environment.PRODUCTION, basic_auth_user_name=None,
                 basic_auth_password=None, basic_auth_credentials=None,
                 config=None):
        self.config = config or Configuration(
            http_client_instance=http_client_instance,
            override_http_client_configuration=override_http_client_configuration,
            http_call_back=http_call_back, timeout=timeout,
            max_retries=max_retries, backoff_factor=backoff_factor,
            retry_statuses=retry_statuses, retry_methods=retry_methods,
            environment=environment, basic_auth_user_name=basic_auth_user_name,
            basic_auth_password=basic_auth_password,
            basic_auth_credentials=basic_auth_credentials)

        self.global_configuration = GlobalConfiguration(self.config)\
            .global_errors(BaseController.global_errors())\
            .base_uri_executor(self.config.get_base_uri)\
            .user_agent(BaseController.user_agent(), BaseController.user_agent_parameters())

        self.auth_managers = {key: None for key in ['basicAuth']}
        self.auth_managers['basicAuth'] = BasicAuth(
            self.config.basic_auth_credentials)
        self.global_configuration = self.global_configuration.auth_managers(self.auth_managers)

