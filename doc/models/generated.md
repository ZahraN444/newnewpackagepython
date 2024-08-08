
# Generated

## Structure

`Generated`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `to` | [`object`](../../doc/models/object-enum.md) | Required | - |
| `carrier` | `str` | Required, Constant | **Default**: `'USPS'` |
| `thumbnails` | [`List[Thumbnail]`](../../doc/models/thumbnail.md) | Optional | - |
| `expected_delivery_date` | `date` | Optional | A date in YYYY-MM-DD format of the mailpiece's expected delivery date based on its `send_date`. |
| `date_created` | `datetime` | Optional | A timestamp in ISO 8601 format of the date the resource was created. |
| `date_modified` | `datetime` | Optional | A timestamp in ISO 8601 format of the date the resource was last modified. |
| `deleted` | `bool` | Optional | Only returned if the resource has been successfully deleted. |

## Example (as JSON)

```json
{
  "to": {
    "key1": "val1",
    "key2": "val2"
  },
  "carrier": "USPS",
  "thumbnails": [
    {
      "small": "small8",
      "medium": "medium8",
      "large": "large6"
    },
    {
      "small": "small8",
      "medium": "medium8",
      "large": "large6"
    }
  ],
  "expected_delivery_date": "2016-03-13",
  "date_created": "2016-03-13T12:52:32.123Z",
  "date_modified": "2016-03-13T12:52:32.123Z",
  "deleted": false
}
```

