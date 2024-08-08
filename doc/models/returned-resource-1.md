
# Returned Resource 1

## Structure

`ReturnedResource1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `resource_type` | `str` | Required, Constant | Mailpiece type for the creative<br>**Default**: `'letter'` |
| `details` | [`Details6`](../../doc/models/details-6.md) | Required | - |
| `mfrom` | [`object`](../../doc/models/object-enum.md) | Required | - |
| `description` | `str` | Optional | An internal description that identifies this resource. Must be no longer than 255 characters.<br>**Constraints**: *Maximum Length*: `255` |
| `metadata` | `Dict[str, str]` | Optional | Use metadata to store custom information for tagging and labeling back to your internal systems. Must be an object with up to 20 key-value pairs. Keys must be at most 40 characters and values must be at most 500 characters. Neither can contain the characters `"` and `\`. i.e. '{"customer_id" : "NEWYORK2015"}' Nested objects are not supported.  See [Metadata](#section/Metadata) for more information. |

## Example (as JSON)

```json
{
  "resource_type": "letter",
  "details": {
    "double_sided": true,
    "address_placement": "top_first_page",
    "buckslips": [
      "buckslips2",
      "buckslips3"
    ],
    "cards": [
      "cards7"
    ],
    "custom_envelope": {
      "key1": "val1",
      "key2": "val2"
    },
    "color": false
  },
  "from": {
    "key1": "val1",
    "key2": "val2"
  },
  "description": "description4",
  "metadata": {
    "key0": "metadata9"
  }
}
```

