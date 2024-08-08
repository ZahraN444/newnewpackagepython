
# Creative Writable 2

## Structure

`CreativeWritable2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `resource_type` | `str` | Required, Constant | Mailpiece type for the creative<br>**Default**: `'self_mailer'` |
| `campaign_id` | `str` | Required | Unique identifier prefixed with `cmp_`.<br>**Constraints**: *Pattern*: `^cmp_[a-zA-Z0-9]+$` |
| `inside` | [`object`](../../doc/models/object-enum.md) | Required | - |
| `outside` | [`object`](../../doc/models/object-enum.md) | Required | - |
| `details` | [`Details4`](../../doc/models/details-4.md) | Required | - |
| `mfrom` | [`object`](../../doc/models/object-enum.md) | Optional | - |
| `description` | `str` | Optional | An internal description that identifies this resource. Must be no longer than 255 characters.<br>**Constraints**: *Maximum Length*: `255` |
| `metadata` | `Dict[str, str]` | Optional | Use metadata to store custom information for tagging and labeling back to your internal systems. Must be an object with up to 20 key-value pairs. Keys must be at most 40 characters and values must be at most 500 characters. Neither can contain the characters `"` and `\`. i.e. '{"customer_id" : "NEWYORK2015"}' Nested objects are not supported.  See [Metadata](#section/Metadata) for more information. |

## Example (as JSON)

```json
{
  "resource_type": "self_mailer",
  "campaign_id": "campaign_id4",
  "inside": {
    "key1": "val1",
    "key2": "val2"
  },
  "outside": {
    "key1": "val1",
    "key2": "val2"
  },
  "details": {
    "mail_type": "usps_first_class",
    "size": "6x18_bifold",
    "qr_code": {
      "position": "position2",
      "top": "top8",
      "right": "right2",
      "left": "left2",
      "bottom": "bottom4",
      "redirect_url": "String9",
      "width": "width0"
    }
  },
  "from": {
    "key1": "val1",
    "key2": "val2"
  },
  "description": "description4",
  "metadata": {
    "key0": "metadata1",
    "key1": "metadata0",
    "key2": "metadata9"
  }
}
```

