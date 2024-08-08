
# Inline Address Us Chk 1

## Structure

`InlineAddressUsChk1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `str` | Optional | An internal description that identifies this resource. Must be no longer than 255 characters.<br>**Constraints**: *Maximum Length*: `255` |
| `name` | `str` | Optional | Either `name` or `company` is required, you may also add both. Must be no longer than 40 characters. If both `name` and `company` are provided, they will be printed on two separate lines above the rest of the address.<br>**Constraints**: *Maximum Length*: `40` |
| `company` | `str` | Optional | Either `name` or `company` is required, you may also add both. Must be no longer than 40 characters. If both `name` and `company` are provided, they will be printed on two separate lines above the rest of the address. This field can be used for any secondary recipient information which is not part of the actual mailing address (Company Name, Department, Attention Line, etc).<br>**Constraints**: *Maximum Length*: `40` |
| `address_line_1` | `str` | Optional | The primary number, street name, and directional information.<br>**Constraints**: *Maximum Length*: `50` |
| `address_line_2` | `str` | Optional | An optional field for address unit information. Total string sum of this plus `address_line1` may not exceed 50 characters.<br>**Constraints**: *Maximum Length*: `50` |
| `address_city` | `str` | Optional | **Constraints**: *Maximum Length*: `200` |
| `address_state` | `str` | Optional | 2 letter state short-name code<br>**Constraints**: *Pattern*: `^[a-zA-Z]{2}$` |
| `address_zip` | `str` | Optional | Must follow the ZIP format of `12345` or ZIP+4 format of `12345-1234`.<br>**Constraints**: *Pattern*: `^\d{5}(-\d{4})?$` |
| `phone` | `str` | Optional | Must be no longer than 40 characters.<br>**Constraints**: *Maximum Length*: `40` |
| `email` | `str` | Optional | Must be no longer than 100 characters.<br>**Constraints**: *Maximum Length*: `100` |
| `address_country` | [`object`](../../doc/models/object-enum.md) | Optional | - |
| `metadata` | `Dict[str, str]` | Optional | Use metadata to store custom information for tagging and labeling back to your internal systems. Must be an object with up to 20 key-value pairs. Keys must be at most 40 characters and values must be at most 500 characters. Neither can contain the characters `"` and `\`. i.e. '{"customer_id" : "NEWYORK2015"}' Nested objects are not supported.  See [Metadata](#section/Metadata) for more information. |

## Example (as JSON)

```json
{
  "description": "description4",
  "name": "name4",
  "company": "company4",
  "address_line1": "address_line18",
  "address_line2": "address_line26"
}
```

