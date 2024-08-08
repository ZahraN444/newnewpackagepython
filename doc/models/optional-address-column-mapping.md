
# Optional Address Column Mapping

## Structure

`OptionalAddressColumnMapping`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address_line_2` | `str` | Required | The column header from the csv file that should be mapped to the optional field "address_line2" |
| `company` | `str` | Required | The column header from the csv file that should be mapped to the optional field "company" |
| `address_country` | `str` | Required | The column header from the csv file that should be mapped to the optional field "address_country" |

## Example (as JSON)

```json
{
  "address_line2": "address_line28",
  "company": "company4",
  "address_country": "address_country2"
}
```

