
# Single Line Address Intl

## Structure

`SingleLineAddressIntl`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address` | `str` | Required | The entire address in one string (e.g., "370 Water St C1N 1C4").<br>**Constraints**: *Maximum Length*: `500` |
| `country` | [`CountryExtendedEnum`](../../doc/models/country-extended-enum.md) | Required | - |

## Example (as JSON)

```json
{
  "address": "address6",
  "country": "CY"
}
```

