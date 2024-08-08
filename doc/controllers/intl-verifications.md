# Intl Verifications

```python
intl_verifications_controller = client.intl_verifications
```

## Class Name

`IntlVerificationsController`

## Methods

* [Bulk Intl Verifications](../../doc/controllers/intl-verifications.md#bulk-intl-verifications)
* [Intl Verification](../../doc/controllers/intl-verifications.md#intl-verification)


# Bulk Intl Verifications

Verify a list of international (except US or US territories) address _with a live API key_. Requests to this endpoint with a test API key will return a dummy response based on the primary line you input.

```python
def bulk_intl_verifications(self,
                           content_type,
                           addresses)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `content_type` | [`ContentTypeEnum`](../../doc/models/content-type-enum.md) | Header, Required | - |
| `addresses` | [`List[MultipleComponentsIntl]`](../../doc/models/multiple-components-intl.md) | Form, Required | - |

## Response Type

[`IntlVerifications`](../../doc/models/intl-verifications.md)

## Example Usage

```python
content_type = ContentTypeEnum.ENUM_APPLICATIONXWWWFORMURLENCODED

addresses = [
    MultipleComponentsIntl(
        primary_line='370 Water St',
        country=CountryExtendedEnum.CA,
        recipient='John Doe',
        secondary_line='',
        city='Summerside',
        state='Prince Edwards Island',
        postal_code='C1N 1C4'
    ),
    MultipleComponentsIntl(
        primary_line='UL. DOLSKAYA 1',
        country=CountryExtendedEnum.RU,
        recipient='Jane Doe',
        secondary_line='',
        city='MOSCOW',
        state='MOSCOW G',
        postal_code='115569'
    )
]

result = intl_verifications_controller.bulk_intl_verifications(
    content_type,
    addresses
)
```

## Example Response *(as JSON)*

```json
{
  "addresses": [
    {
      "id": "intl_ver_c7cb63d68f8d6",
      "recipient": null,
      "primary_line": "370 WATER ST",
      "secondary_line": "",
      "last_line": "SUMMERSIDE PE C1N 1C4",
      "country": "CA",
      "coverage": "SUBBUILDING",
      "deliverability": "deliverable",
      "status": "LV4",
      "components": {
        "primary_number": "370",
        "street_name": "WATER ST",
        "city": "SUMMERSIDE",
        "state": "PE",
        "postal_code": "C1N 1C4"
      },
      "object": "intl_verification"
    }
  ],
  "errors": false
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error | [`Domains0Error1Exception`](../../doc/models/domains-0-error-1-exception.md) |


# Intl Verification

Verify an international (except US or US territories) address _with a live API key_. Requests to this endpoint with a test API key will return a dummy response based on the primary line you input.

```python
def intl_verification(self,
                     body,
                     x_lang_output=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`object`](../../doc/models/object-enum.md) | Body, Required | - |
| `x_lang_output` | [`XLangOutput1Enum`](../../doc/models/x-lang-output-1-enum.md) | Header, Optional | * `native` - Translate response to the native language of the country in the request<br>* `match` - match the response to the language in the request<br><br>Default response is in English. |

## Response Type

[`IntlVerification`](../../doc/models/intl-verification.md)

## Example Usage

```python
body = jsonpickle.decode('{"recipient":"Harry Zhang","primary_line":"370 Water St","secondary_line":"","city":"Summerside","state":"Prince Edward Island","postal code":"C1N 1C4","country":"CA"}')

result = intl_verifications_controller.intl_verification(body)
```

## Example Response *(as JSON)*

```json
{
  "id": "intl_ver_c7cb63d68f8d6",
  "recipient": null,
  "primary_line": "370 WATER ST",
  "secondary_line": "",
  "last_line": "SUMMERSIDE PE C1N 1C4",
  "country": "CA",
  "coverage": "SUBBUILDING",
  "deliverability": "deliverable",
  "status": "LV4",
  "components": {
    "primary_number": "370",
    "street_name": "WATER ST",
    "city": "SUMMERSIDE",
    "state": "PE",
    "postal_code": "C1N 1C4"
  },
  "object": "intl_verification"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error | [`Domains0Error1Exception`](../../doc/models/domains-0-error-1-exception.md) |

