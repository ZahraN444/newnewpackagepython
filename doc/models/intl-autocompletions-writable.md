
# Intl Autocompletions Writable

## Structure

`IntlAutocompletionsWritable`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address_prefix` | `str` | Required | Only accepts numbers and street names in an alphanumeric format. |
| `city` | `str` | Optional | An optional city input used to filter suggestions. Case insensitive and does not match partial abbreviations. |
| `state` | `str` | Optional | An optional state input used to filter suggestions. Case insensitive and does not match partial abbreviations. |
| `zip_code` | `str` | Optional | An optional Zip Code input used to filter suggestions. Matches partial entries. |
| `country` | [`CountryExtendedEnum`](../../doc/models/country-extended-enum.md) | Required | - |
| `geo_ip_sort` | `bool` | Optional | If `true`, sort suggestions by proximity to the IP set in the `X-Forwarded-For` header. |

## Example (as JSON)

```json
{
  "address_prefix": "address_prefix4",
  "city": "city6",
  "state": "state2",
  "zip_code": "zip_code0",
  "country": "ET",
  "geo_ip_sort": false
}
```

