
# Optional Address Columns

The mapping of column headers in your file to Lob-optional fields for the resource created. See our <a href="https://help.lob.com/print-and-mail/building-a-mail-strategy/campaign-or-triggered-sends/campaign-audience-guide#optional-columns-3" target="_blank">Campaign Audience Guide</a> for additional details.

## Structure

`OptionalAddressColumns`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address_line_2` | `str` | Required | The column header from the csv file that should be mapped to the optional field "address_line2" |
| `company` | `str` | Required | The column header from the csv file that should be mapped to the optional field "company" |
| `address_country` | `str` | Required | The column header from the csv file that should be mapped to the optional field "address_country" |

## Example (as JSON)

```json
{
  "address_line2": "secondary_line",
  "company": "company",
  "address_country": "country,"
}
```

