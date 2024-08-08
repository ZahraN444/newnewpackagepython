
# Card Order

## Structure

`CardOrder`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `date_created` | `datetime` | Required | A timestamp in ISO 8601 format of the date the resource was created. |
| `date_modified` | `datetime` | Required | A timestamp in ISO 8601 format of the date the resource was last modified. |
| `deleted` | `bool` | Optional | Only returned if the resource has been successfully deleted. |
| `object` | `str` | Required | Value is resource type. |
| `id` | `str` | Optional | Unique identifier prefixed with `co_`.<br>**Constraints**: *Pattern*: `^co_[a-zA-Z0-9]+$` |
| `card_id` | `str` | Optional | Unique identifier prefixed with `card_`.<br>**Constraints**: *Pattern*: `^card_[a-zA-Z0-9]+$` |
| `status` | [`Status2Enum`](../../doc/models/status-2-enum.md) | Optional | - |
| `inventory` | `float` | Optional | The inventory of the card order.<br>**Default**: `0` |
| `quantity_ordered` | `float` | Optional | The quantity of cards ordered<br>**Default**: `0` |
| `unit_price` | `float` | Optional | The unit price for the card order.<br>**Default**: `0` |
| `cancelled_reason` | `str` | Optional | The reason for cancellation. |
| `availability_date` | `datetime` | Optional | A timestamp in ISO 8601 format of the date the resource was created. |
| `expected_availability_date` | `datetime` | Optional | The fixed deadline for the cards to be printed. |

## Example (as JSON)

```json
{
  "date_created": "2016-03-13T12:52:32.123Z",
  "date_modified": "2016-03-13T12:52:32.123Z",
  "object": "object8",
  "inventory": 0.0,
  "quantity_ordered": 0,
  "unit_price": 0,
  "deleted": false,
  "id": "id4",
  "card_id": "card_id0",
  "status": "depleted"
}
```

