
# Address Fields Intl

## Structure

`AddressFieldsIntl`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address_line_1` | `str` | Required | The primary number, street name, and directional information.<br>**Constraints**: *Maximum Length*: `200` |
| `address_line_2` | `str` | Optional | An optional field containing any information which can't fit into line 1.<br>**Constraints**: *Maximum Length*: `200` |
| `address_city` | `str` | Optional | **Constraints**: *Maximum Length*: `200` |
| `address_state` | `str` | Optional | **Constraints**: *Maximum Length*: `200` |
| `address_zip` | `str` | Optional | Optional postal code.<br>**Constraints**: *Maximum Length*: `40` |

## Example (as JSON)

```json
{
  "address_line1": "address_line18",
  "address_line2": "address_line20",
  "address_city": "address_city8",
  "address_state": "address_state0",
  "address_zip": "address_zip0"
}
```

