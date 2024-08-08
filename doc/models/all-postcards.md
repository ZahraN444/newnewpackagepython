
# All Postcards

## Structure

`AllPostcards`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `object` | `str` | Optional | Value is resource type. |
| `next_url` | `str` | Optional | Url of next page of items in list. |
| `previous_url` | `str` | Optional | Url of previous page of items in list. |
| `count` | `int` | Optional | number of resources in a set |
| `total_count` | `int` | Optional | Indicates the total number of records. Provided when the request specifies an "include" query parameter |
| `data` | [`List[Postcard]`](../../doc/models/postcard.md) | Optional | list of postcards |

## Example (as JSON)

```json
{
  "object": "object8",
  "next_url": "next_url4",
  "previous_url": "previous_url8",
  "count": 48,
  "total_count": 116
}
```

