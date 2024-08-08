
# Client Class Documentation

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| `http_client_instance` | `HttpClient` | The Http Client passed from the sdk user for making requests |
| `override_http_client_configuration` | `bool` | The value which determines to override properties of the passed Http Client from the sdk user |
| `http_call_back` | `HttpCallBack` | The callback value that is invoked before and after an HTTP call is made to an endpoint |
| `timeout` | `float` | The value to use for connection timeout. <br> **Default: 60** |
| `max_retries` | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 0** |
| `backoff_factor` | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 2** |
| `retry_statuses` | `Array of int` | The http statuses on which retry is to be done. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| `retry_methods` | `Array of string` | The http methods on which retry is to be done. <br> **Default: ['GET', 'PUT']** |
| `basic_auth_credentials` | [`BasicAuthCredentials`]($basicauth) | The credential object for Basic Authentication |

The API client can be initialized as follows:

```python
client = LobClient(
    basic_auth_credentials=BasicAuthCredentials(
        username='BasicAuthUserName',
        password='BasicAuthPassword'
    ),
    environment=Environment.PRODUCTION
)
```

## Lob Client

The gateway for the SDK. This class acts as a factory for the Controllers and also holds the configuration of the SDK.

## Controllers

| Name | Description |
|  --- | --- |
| addresses | Gets AddressesController |
| bank_accounts | Gets BankAccountsController |
| billing_groups | Gets BillingGroupsController |
| buckslip_orders | Gets BuckslipOrdersController |
| buckslips | Gets BuckslipsController |
| campaigns | Gets CampaignsController |
| card_orders | Gets CardOrdersController |
| cards | Gets CardsController |
| checks | Gets ChecksController |
| creatives | Gets CreativesController |
| identity_validation | Gets IdentityValidationController |
| intl_autocompletions | Gets IntlAutocompletionsController |
| intl_verifications | Gets IntlVerificationsController |
| letters | Gets LettersController |
| postcards | Gets PostcardsController |
| qr_codes | Gets QRCodesController |
| reverse_geocode_lookups | Gets ReverseGeocodeLookupsController |
| self_mailers | Gets SelfMailersController |
| template_versions | Gets TemplateVersionsController |
| templates | Gets TemplatesController |
| uploads | Gets UploadsController |
| url_shortener | Gets URLShortenerController |
| us_autocompletions | Gets USAutocompletionsController |
| us_verifications | Gets USVerificationsController |
| zip_lookups | Gets ZipLookupsController |

