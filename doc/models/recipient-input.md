
# Recipient Input

## Structure

`RecipientInput`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `recipient` | `str` | Required | The intended recipient, typically a person's or firm's name.<br>**Constraints**: *Maximum Length*: `500` |
| `primary_line` | `str` | Required | The primary delivery line (usually the street address) of the address.<br>Combination of the following applicable `components`:<br><br>* `primary_number`<br>* `street_predirection`<br>* `street_name`<br>* `street_suffix`<br>* `street_postdirection`<br>* `secondary_designator`<br>* `secondary_number`<br>* `pmb_designator`<br>* `pmb_number`<br>**Constraints**: *Maximum Length*: `500` |
| `secondary_line` | `str` | Optional | The secondary delivery line of the address. This field is typically empty but may contain information if `primary_line` is too long.<br>**Constraints**: *Maximum Length*: `500` |
| `urbanization` | `str` | Optional | Only present for addresses in Puerto Rico. An urbanization refers to an area, sector, or development within a city. See <a href="https://pe.usps.com/text/pub28/28api_008.htm#:~:text=I51.,-4%20Urbanizations&text=In%20Puerto%20Rico%2C%20identical%20street,placed%20before%20the%20urbanization%20name." target="_blank">USPS documentation</a> for clarification.<br>**Constraints**: *Maximum Length*: `500` |
| `city` | `str` | Required | **Constraints**: *Maximum Length*: `200` |
| `state` | `str` | Required | The <a href="https://en.wikipedia.org/wiki/ISO_3166-2:US" target="_blank">ISO 3166-2</a> two letter code or subdivision name for the state. `city` and `state` are required if no `zip_code` is passed.<br>**Constraints**: *Maximum Length*: `50` |
| `zip_code` | `str` | Required | **Constraints**: *Pattern*: `^\d{5}((-)?\d{4})?$` |

## Example (as JSON)

```json
{
  "recipient": "recipient6",
  "primary_line": "primary_line4",
  "secondary_line": "secondary_line0",
  "urbanization": "urbanization6",
  "city": "city4",
  "state": "state0",
  "zip_code": "zip_code8"
}
```

