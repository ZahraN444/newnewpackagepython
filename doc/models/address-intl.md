
# Address Intl

## Structure

`AddressIntl`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `date_created` | `datetime` | Required | A timestamp in ISO 8601 format of the date the resource was created. |
| `date_modified` | `datetime` | Required | A timestamp in ISO 8601 format of the date the resource was last modified. |
| `deleted` | `bool` | Optional | Only returned if the resource has been successfully deleted. |
| `object` | `str` | Required, Constant | Value is resource type.<br>**Default**: `'address'` |
| `id` | `str` | Required | Unique identifier prefixed with `adr_`.<br>**Constraints**: *Pattern*: `^adr_[a-zA-Z0-9]+$` |
| `description` | `str` | Optional | An internal description that identifies this resource. Must be no longer than 255 characters.<br>**Constraints**: *Maximum Length*: `255` |
| `name` | `str` | Required | Either `name` or `company` is required, you may also add both. Must be no longer than 40 characters. If both `name` and `company` are provided, they will be printed on two separate lines above the rest of the address.<br>**Constraints**: *Maximum Length*: `40` |
| `company` | `str` | Required | Either `name` or `company` is required, you may also add both. Must be no longer than 40 characters. If both `name` and `company` are provided, they will be printed on two separate lines above the rest of the address. This field can be used for any secondary recipient information which is not part of the actual mailing address (Company Name, Department, Attention Line, etc).<br>**Constraints**: *Maximum Length*: `40` |
| `phone` | `str` | Optional | Must be no longer than 40 characters.<br>**Constraints**: *Maximum Length*: `40` |
| `email` | `str` | Optional | Must be no longer than 100 characters.<br>**Constraints**: *Maximum Length*: `100` |
| `metadata` | `Dict[str, str]` | Optional | Use metadata to store custom information for tagging and labeling back to your internal systems. Must be an object with up to 20 key-value pairs. Keys must be at most 40 characters and values must be at most 500 characters. Neither can contain the characters `"` and `\`. i.e. '{"customer_id" : "NEWYORK2015"}' Nested objects are not supported.  See [Metadata](#section/Metadata) for more information. |
| `address_line_1` | `str` | Required | **Constraints**: *Maximum Length*: `200` |
| `address_line_2` | `str` | Optional | **Constraints**: *Maximum Length*: `200` |
| `address_city` | `str` | Optional | **Constraints**: *Maximum Length*: `200` |
| `address_state` | `str` | Optional | Will be returned as a full string<br>**Constraints**: *Maximum Length*: `200` |
| `address_zip` | `str` | Optional | Optional postal code.<br>**Constraints**: *Maximum Length*: `40` |
| `address_country` | [`AddressCountry1Enum`](../../doc/models/address-country-1-enum.md) | Required | **Constraints**: *Maximum Length*: `200` |

## Example (as JSON)

```json
{
  "date_created": "2016-03-13T12:52:32.123Z",
  "date_modified": "2016-03-13T12:52:32.123Z",
  "object": "address",
  "id": "id8",
  "name": "name8",
  "company": "company2",
  "address_line1": "address_line18",
  "address_country": "SENEGAL",
  "deleted": false,
  "description": "description2",
  "phone": "phone2",
  "email": "email8",
  "metadata": {
    "key0": "metadata5",
    "key1": "metadata6",
    "key2": "metadata7"
  }
}
```

