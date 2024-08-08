
# Intl Components

A nested object containing a breakdown of each component of an address.

## Structure

`IntlComponents`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `primary_number` | `str` | Optional | The numeric or alphanumeric part of an address preceding the street name. Often the house, building, or PO Box number. |
| `street_name` | `str` | Optional | The name of the street. |
| `city` | `str` | Optional | **Constraints**: *Maximum Length*: `200` |
| `state` | `str` | Optional | The <a href="https://en.wikipedia.org/wiki/ISO_3166-2" target="_blank">ISO 3166-2</a> two letter code for the state.<br>**Constraints**: *Maximum Length*: `2` |
| `postal_code` | `str` | Optional | The postal code.<br>**Constraints**: *Maximum Length*: `12` |

## Example (as JSON)

```json
{
  "primary_number": "primary_number0",
  "street_name": "street_name6",
  "city": "city0",
  "state": "state6",
  "postal_code": "postal_code2"
}
```

