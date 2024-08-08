
# Address Editable Intl

## Structure

`AddressEditableIntl`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address_line_1` | `str` | Required | The primary number, street name, and directional information.<br>**Constraints**: *Maximum Length*: `200` |
| `address_line_2` | `str` | Optional | An optional field containing any information which can't fit into line 1.<br>**Constraints**: *Maximum Length*: `200` |
| `address_city` | `str` | Optional | **Constraints**: *Maximum Length*: `200` |
| `address_state` | `str` | Optional | **Constraints**: *Maximum Length*: `200` |
| `address_zip` | `str` | Optional | Optional postal code.<br>**Constraints**: *Maximum Length*: `40` |
| `description` | `str` | Optional | An internal description that identifies this resource. Must be no longer than 255 characters.<br>**Constraints**: *Maximum Length*: `255` |
| `name` | `str` | Required | Either `name` or `company` is required, you may also add both. Must be no longer than 40 characters. If both `name` and `company` are provided, they will be printed on two separate lines above the rest of the address.<br>**Constraints**: *Maximum Length*: `40` |
| `company` | `str` | Required | Either `name` or `company` is required, you may also add both. Must be no longer than 40 characters. If both `name` and `company` are provided, they will be printed on two separate lines above the rest of the address. This field can be used for any secondary recipient information which is not part of the actual mailing address (Company Name, Department, Attention Line, etc).<br>**Constraints**: *Maximum Length*: `40` |
| `phone` | `str` | Optional | Must be no longer than 40 characters.<br>**Constraints**: *Maximum Length*: `40` |
| `email` | `str` | Optional | Must be no longer than 100 characters.<br>**Constraints**: *Maximum Length*: `100` |
| `address_country` | [`CountryExtendedEnum`](../../doc/models/country-extended-enum.md) | Required | - |
| `metadata` | `Dict[str, str]` | Optional | Use metadata to store custom information for tagging and labeling back to your internal systems. Must be an object with up to 20 key-value pairs. Keys must be at most 40 characters and values must be at most 500 characters. Neither can contain the characters `"` and `\`. i.e. '{"customer_id" : "NEWYORK2015"}' Nested objects are not supported.  See [Metadata](#section/Metadata) for more information. |

## Example (as JSON)

```json
{
  "address_line1": "address_line18",
  "address_line2": "address_line26",
  "address_city": "address_city4",
  "address_state": "address_state6",
  "address_zip": "address_zip4",
  "description": "description4",
  "name": "name4",
  "company": "company6",
  "address_country": "NP"
}
```

