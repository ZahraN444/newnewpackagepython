
# Creative Base

## Structure

`CreativeBase`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mfrom` | [`object`](../../doc/models/object-enum.md) | Optional | - |
| `description` | `str` | Optional | An internal description that identifies this resource. Must be no longer than 255 characters.<br>**Constraints**: *Maximum Length*: `255` |
| `metadata` | `Dict[str, str]` | Optional | Use metadata to store custom information for tagging and labeling back to your internal systems. Must be an object with up to 20 key-value pairs. Keys must be at most 40 characters and values must be at most 500 characters. Neither can contain the characters `"` and `\`. i.e. '{"customer_id" : "NEWYORK2015"}' Nested objects are not supported.  See [Metadata](#section/Metadata) for more information. |

## Example (as JSON)

```json
{
  "from": {
    "key1": "val1",
    "key2": "val2"
  },
  "description": "description6",
  "metadata": {
    "key0": "metadata3",
    "key1": "metadata2",
    "key2": "metadata1"
  }
}
```

