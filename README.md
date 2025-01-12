
# Getting Started with Lob

## Introduction

The Lob API is organized around REST. Our API is designed to have predictable, resource-oriented URLs and uses HTTP response codes to indicate any API errors. <p>

## Install the Package

The package is compatible with Python versions `3 >=3.7, <= 3.11`.
Install the package from PyPi using the following pip command:

```python
pip install my-package-sdkwewqe==4.5.5
```

You can also view the package at:
https://pypi.python.org/pypi/my-package-sdkwewqe/4.5.5

## Test the SDK

You can test the generated SDK and the server with test cases. `unittest` is used as the testing framework and `pytest` is used as the test runner. You can run the tests as follows:

Navigate to the root directory of the SDK and run the following commands

```
pip install -r test-requirements.txt
pytest
```

## Initialize the API Client

**_Note:_** Documentation for the client can be found [here.](https://www.github.com/ZahraN444/newnewpackagepython/tree/4.5.5/doc/client.md)

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

## Authorization

This API uses the following authentication schemes.

* [`basicAuth (Basic Authentication)`](https://www.github.com/ZahraN444/newnewpackagepython/tree/4.5.5/doc/$basicauth)

## List of APIs

* [Bank Accounts](https://www.github.com/ZahraN444/newnewpackagepython/tree/4.5.5/doc/controllers/bank-accounts.md)
* [Billing Groups](https://www.github.com/ZahraN444/newnewpackagepython/tree/4.5.5/doc/controllers/billing-groups.md)
* [Buckslip Orders](https://www.github.com/ZahraN444/newnewpackagepython/tree/4.5.5/doc/controllers/buckslip-orders.md)
* [Card Orders](https://www.github.com/ZahraN444/newnewpackagepython/tree/4.5.5/doc/controllers/card-orders.md)
* [Identity Validation](https://www.github.com/ZahraN444/newnewpackagepython/tree/4.5.5/doc/controllers/identity-validation.md)
* [Intl Autocompletions](https://www.github.com/ZahraN444/newnewpackagepython/tree/4.5.5/doc/controllers/intl-autocompletions.md)
* [Intl Verifications](https://www.github.com/ZahraN444/newnewpackagepython/tree/4.5.5/doc/controllers/intl-verifications.md)
* [QR Codes](https://www.github.com/ZahraN444/newnewpackagepython/tree/4.5.5/doc/controllers/qr-codes.md)
* [Reverse Geocode Lookups](https://www.github.com/ZahraN444/newnewpackagepython/tree/4.5.5/doc/controllers/reverse-geocode-lookups.md)
* [Self Mailers](https://www.github.com/ZahraN444/newnewpackagepython/tree/4.5.5/doc/controllers/self-mailers.md)
* [Template Versions](https://www.github.com/ZahraN444/newnewpackagepython/tree/4.5.5/doc/controllers/template-versions.md)
* [URL Shortener](https://www.github.com/ZahraN444/newnewpackagepython/tree/4.5.5/doc/controllers/url-shortener.md)
* [US Autocompletions](https://www.github.com/ZahraN444/newnewpackagepython/tree/4.5.5/doc/controllers/us-autocompletions.md)
* [US Verifications](https://www.github.com/ZahraN444/newnewpackagepython/tree/4.5.5/doc/controllers/us-verifications.md)
* [Zip Lookups](https://www.github.com/ZahraN444/newnewpackagepython/tree/4.5.5/doc/controllers/zip-lookups.md)
* [Addresses](https://www.github.com/ZahraN444/newnewpackagepython/tree/4.5.5/doc/controllers/addresses.md)
* [Buckslips](https://www.github.com/ZahraN444/newnewpackagepython/tree/4.5.5/doc/controllers/buckslips.md)
* [Campaigns](https://www.github.com/ZahraN444/newnewpackagepython/tree/4.5.5/doc/controllers/campaigns.md)
* [Cards](https://www.github.com/ZahraN444/newnewpackagepython/tree/4.5.5/doc/controllers/cards.md)
* [Checks](https://www.github.com/ZahraN444/newnewpackagepython/tree/4.5.5/doc/controllers/checks.md)
* [Creatives](https://www.github.com/ZahraN444/newnewpackagepython/tree/4.5.5/doc/controllers/creatives.md)
* [Letters](https://www.github.com/ZahraN444/newnewpackagepython/tree/4.5.5/doc/controllers/letters.md)
* [Postcards](https://www.github.com/ZahraN444/newnewpackagepython/tree/4.5.5/doc/controllers/postcards.md)
* [Templates](https://www.github.com/ZahraN444/newnewpackagepython/tree/4.5.5/doc/controllers/templates.md)
* [Uploads](https://www.github.com/ZahraN444/newnewpackagepython/tree/4.5.5/doc/controllers/uploads.md)

## Classes Documentation

* [Utility Classes](https://www.github.com/ZahraN444/newnewpackagepython/tree/4.5.5/doc/utility-classes.md)
* [HttpResponse](https://www.github.com/ZahraN444/newnewpackagepython/tree/4.5.5/doc/http-response.md)
* [HttpRequest](https://www.github.com/ZahraN444/newnewpackagepython/tree/4.5.5/doc/http-request.md)

