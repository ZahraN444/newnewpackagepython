
# Card

## Structure

`Card`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `date_created` | `datetime` | Required | A timestamp in ISO 8601 format of the date the resource was created. |
| `date_modified` | `datetime` | Required | A timestamp in ISO 8601 format of the date the resource was last modified. |
| `deleted` | `bool` | Optional | Only returned if the resource has been successfully deleted. |
| `object` | `str` | Required, Constant | Value is resource type.<br>**Default**: `'card'` |
| `description` | `str` | Required | Description of the card.<br>**Constraints**: *Maximum Length*: `255` |
| `size` | [`Size1Enum`](../../doc/models/size-1-enum.md) | Optional | - |
| `id` | `str` | Required | Unique identifier prefixed with `card_`.<br>**Constraints**: *Pattern*: `^card_[a-zA-Z0-9]+$` |
| `url` | `str` | Required | The signed link for the card.<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `2083` |
| `auto_reorder` | `bool` | Required | True if the cards should be auto-reordered. |
| `reorder_quantity` | `int` | Required | The number of cards to be reordered. |
| `raw_url` | `str` | Required | The raw URL of the card.<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `2083` |
| `front_original_url` | `str` | Required | The original URL of the front template.<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `2083` |
| `back_original_url` | `str` | Required | The original URL of the back template.<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `2083` |
| `thumbnails` | [`List[Thumbnail]`](../../doc/models/thumbnail.md) | Required | - |
| `available_quantity` | `int` | Required | The available quantity of cards. |
| `pending_quantity` | `int` | Required | The pending quantity of cards. |
| `status` | [`ThestatusofthecardEnum`](../../doc/models/thestatusofthecard-enum.md) | Required | - |
| `orientation` | [`OrientationEnum`](../../doc/models/orientation-enum.md) | Required | - |
| `threshold_amount` | `int` | Required | The threshold amount of the card |

## Example (as JSON)

```json
{
  "date_created": "2016-03-13T12:52:32.123Z",
  "date_modified": "2016-03-13T12:52:32.123Z",
  "object": "card",
  "description": "description6",
  "id": "id6",
  "url": "url0",
  "auto_reorder": false,
  "reorder_quantity": 2,
  "raw_url": "raw_url8",
  "front_original_url": "front_original_url0",
  "back_original_url": "back_original_url2",
  "thumbnails": [
    {
      "small": "small8",
      "medium": "medium8",
      "large": "large6"
    }
  ],
  "available_quantity": 22,
  "pending_quantity": 140,
  "status": "processed",
  "orientation": "horizontal",
  "threshold_amount": 124,
  "deleted": false,
  "size": "3.375x2.125"
}
```

