# US Autocompletions

```python
us_autocompletions_controller = client.us_autocompletions
```

## Class Name

`USAutocompletionsController`


# Autocompletion

Given an address prefix consisting of a partial primary line, as well as optional input of city, state, and zip code, this functionality returns up to 10 full US address suggestions. Not all of them will turn out to be valid addresses; they'll need to be [verified](#operation/verification_us).

```python
def autocompletion(self,
                  content_type,
                  address_prefix,
                  case=None,
                  valid_addresses=False,
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
| `case` | [`Case1Enum`](../../doc/models/case-1-enum.md) | Query, Optional | Casing of the verified address. Possible values are `upper` and `proper` for uppercased (e.g. "PO BOX") and proper-cased (e.g. "PO Box"), respectively. Only affects `primary_line`, `city`, and `state`. Default casing is `upper`. |
| `valid_addresses` | `bool` | Query, Optional | Possible values are `true` and `false`. If false, not all of the suggestions in the response will be valid addresses; they'll need to be verified in order to determine the deliverability. The valid_addresses flag will greatly reduce the number of keystrokes needed before reaching an intended address. |
| `city` | `str` | Form, Optional | An optional city input used to filter suggestions. Case insensitive and does not match partial abbreviations. |
| `state` | `str` | Form, Optional | An optional state input used to filter suggestions. Case insensitive and does not match partial abbreviations. |
| `zip_code` | `str` | Form, Optional | An optional ZIP Code input used to filter suggestions. Matches partial entries. |
| `geo_ip_sort` | `bool` | Form, Optional | If `true`, sort suggestions by proximity to the IP set in the `X-Forwarded-For` header. |

## Response Type

[`UsAutocompletions`](../../doc/models/us-autocompletions.md)

## Example Usage

```python
content_type = ContentTypeEnum.ENUM_APPLICATIONXWWWFORMURLENCODED

address_prefix = 'address_prefix8'

valid_addresses = False

result = us_autocompletions_controller.autocompletion(
    content_type,
    address_prefix,
    valid_addresses=valid_addresses
)
```

## Example Response *(as JSON)*

```json
{
  "id": "us_auto_a3ac97bcfbb2460ab20c",
  "suggestions": [
    {
      "primary_line": "185 BAYSIDE VILLAGE PL",
      "city": "SAN FRANCISCO",
      "state": "CA",
      "zip_code": "94107"
    },
    {
      "primary_line": "185 BRANNAN ST",
      "city": "SAN FRANCISCO",
      "state": "CA",
      "zip_code": "94107"
    },
    {
      "primary_line": "185 BONIFACIO ST",
      "city": "SAN FRANCISCO",
      "state": "CA",
      "zip_code": "94107"
    },
    {
      "primary_line": "185 BLAIR TER",
      "city": "SAN FRANCISCO",
      "state": "CA",
      "zip_code": "94107"
    },
    {
      "primary_line": "185 BLUXOME ST",
      "city": "SAN FRANCISCO",
      "state": "CA",
      "zip_code": "94107"
    },
    {
      "primary_line": "210 KING ST",
      "city": "SAN FRANCISCO",
      "state": "CA",
      "zip_code": "94107"
    },
    {
      "primary_line": "185 BRYANT ST",
      "city": "SAN FRANCISCO",
      "state": "CA",
      "zip_code": "94107"
    }
  ],
  "object": "us_autocompletion"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error | [`Domains0Error1Exception`](../../doc/models/domains-0-error-1-exception.md) |

