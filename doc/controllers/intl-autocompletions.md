# Intl Autocompletions

```python
intl_autocompletions_controller = client.intl_autocompletions
```

## Class Name

`IntlAutocompletionsController`


# Intl Autocompletions

Given an address prefix consisting of a partial primary line and country, as well as optional input of city, state, and zip code, this functionality returns up to 10 full International address suggestions. Not all of them will turn out to be valid addresses; they'll need to be [verified](#operation/intl_verification).

```python
def intl_autocompletions(self,
                        content_type,
                        address_prefix,
                        country,
                        x_lang_output=None,
                        city=None,
                        state=None,
                        zip_code=None,
                        geo_ip_sort=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `content_type` | [`ContentTypeEnum`](../../doc/models/content-type-enum.md) | Header, Required | - |
| `address_prefix` | `str` | Form, Required | Only accepts numbers and street names in an alphanumeric format. |
| `country` | [`CountryExtendedEnum`](../../doc/models/country-extended-enum.md) | Form, Required | - |
| `x_lang_output` | [`XLangOutput1Enum`](../../doc/models/x-lang-output-1-enum.md) | Header, Optional | * `native` - Translate response to the native language of the country in the request<br>* `match` - match the response to the language in the request<br><br>Default response is in English. |
| `city` | `str` | Form, Optional | An optional city input used to filter suggestions. Case insensitive and does not match partial abbreviations. |
| `state` | `str` | Form, Optional | An optional state input used to filter suggestions. Case insensitive and does not match partial abbreviations. |
| `zip_code` | `str` | Form, Optional | An optional Zip Code input used to filter suggestions. Matches partial entries. |
| `geo_ip_sort` | `bool` | Form, Optional | If `true`, sort suggestions by proximity to the IP set in the `X-Forwarded-For` header. |

## Response Type

[`IntlAutocompletions`](../../doc/models/intl-autocompletions.md)

## Example Usage

```python
content_type = ContentTypeEnum.ENUM_APPLICATIONXWWWFORMURLENCODED

address_prefix = 'address_prefix8'

country = CountryExtendedEnum.HK

result = intl_autocompletions_controller.intl_autocompletions(
    content_type,
    address_prefix,
    country
)
```

## Example Response *(as JSON)*

```json
{
  "id": "intl_auto_a3ac97bcfbb2460ab20c",
  "suggestions": [
    {
      "primary_number_range": "",
      "primary_line": "340 WATERSTONE PL SE",
      "city": "AIRDRIE",
      "state": "AB",
      "country": "CA",
      "zip_code": "T4B 2G7"
    },
    {
      "primary_number_range": "",
      "primary_line": "340 WATT BLVD SW",
      "city": "EDMONTON",
      "state": "AB",
      "country": "CA",
      "zip_code": "T6X 1R7"
    },
    {
      "primary_number_range": "",
      "primary_line": "340 WATROUS ST",
      "city": "PRINCE GEORGE",
      "state": "BC",
      "country": "CA",
      "zip_code": "V2M 2B6"
    },
    {
      "primary_number_range": "",
      "primary_line": "340 WATERS RD",
      "city": "QUALICUM BEACH",
      "state": "BC",
      "country": "CA",
      "zip_code": "V9K 2B8"
    },
    {
      "primary_number_range": "",
      "primary_line": "SUITE 340, 1510 WATT DR SW",
      "city": "EDMONTON",
      "state": "AB",
      "country": "CA",
      "zip_code": "T6X 2E6"
    },
    {
      "primary_number_range": "",
      "primary_line": "WATERFRONT POINTE WEST SUITE 340, 5212 25 AVE NW",
      "city": "EDMONTON",
      "state": "AB",
      "country": "CA",
      "zip_code": "T6L 6R7"
    },
    {
      "primary_number_range": "",
      "primary_line": "WATERFRONT POINTE EAST SUITE 340, 2520 52 ST NW",
      "city": "EDMONTON",
      "state": "AB",
      "country": "CA",
      "zip_code": "T6L 6S2"
    },
    {
      "primary_number_range": "",
      "primary_line": "WATERSTONE SUITE 340, 6079 MAYNARD WAY NW",
      "city": "EDMONTON",
      "state": "AB",
      "country": "CA",
      "zip_code": "T6R 0S4"
    },
    {
      "primary_number_range": "",
      "primary_line": "WATSON APTS. SUITE 340, 5207 39 ST",
      "city": "RED DEER",
      "state": "AB",
      "country": "CA",
      "zip_code": "T4N 0Z9"
    },
    {
      "primary_number_range": "",
      "primary_line": "WATERS EDGE SUITE 3400..3409, 2600 FERGUSON RD",
      "city": "SAANICHTON",
      "state": "BC",
      "country": "CA",
      "zip_code": "V8M 2C1"
    }
  ],
  "object": "intl_autocompletion"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error | [`Domains0Error1Exception`](../../doc/models/domains-0-error-1-exception.md) |

