
# Cards Response

## Structure

`CardsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `object` | `str` | Optional | Value is resource type. |
| `next_url` | `str` | Optional | Url of next page of items in list. |
| `previous_url` | `str` | Optional | Url of previous page of items in list. |
| `count` | `int` | Optional | number of resources in a set |
| `total_count` | `int` | Optional | Indicates the total number of records. Provided when the request specifies an "include" query parameter |
| `data` | [`List[Card]`](../../doc/models/card.md) | Optional | list of cards |

## Example (as JSON)

```json
{
  "object": "object4",
  "next_url": "next_url6",
  "previous_url": "previous_url6",
  "count": 62,
  "total_count": 102
}
```

