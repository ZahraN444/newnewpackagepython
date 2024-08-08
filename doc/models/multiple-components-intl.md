
# Multiple Components Intl

## Structure

`MultipleComponentsIntl`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `recipient` | `str` | Optional | The intended recipient, typically a person's or firm's name.<br>**Constraints**: *Maximum Length*: `500` |
| `primary_line` | `str` | Required | The primary delivery line (usually the street address) of the address.<br>**Constraints**: *Maximum Length*: `200` |
| `secondary_line` | `str` | Optional | The secondary delivery line of the address. This field is typically empty but may contain information if `primary_line` is too long.<br>**Constraints**: *Maximum Length*: `500` |
| `city` | `str` | Optional | **Constraints**: *Maximum Length*: `200` |
| `state` | `str` | Optional | The name of the state. |
| `postal_code` | `str` | Optional | The postal code.<br>**Constraints**: *Maximum Length*: `12` |
| `country` | [`CountryExtendedEnum`](../../doc/models/country-extended-enum.md) | Required | - |

## Example (as JSON)

```json
{
  "recipient": "recipient0",
  "primary_line": "primary_line8",
  "secondary_line": "secondary_line4",
  "city": "city8",
  "state": "state4",
  "postal_code": "postal_code0",
  "country": "CG"
}
```

