
# All Checks

## Structure

`AllChecks`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `object` | `str` | Optional | Value is resource type. |
| `next_url` | `str` | Optional | Url of next page of items in list. |
| `previous_url` | `str` | Optional | Url of previous page of items in list. |
| `count` | `int` | Optional | number of resources in a set |
| `total_count` | `int` | Optional | Indicates the total number of records. Provided when the request specifies an "include" query parameter |
| `data` | [`List[Check]`](../../doc/models/check.md) | Optional | list of checks |

## Example (as JSON)

```json
{
  "object": "object0",
  "next_url": "next_url2",
  "previous_url": "previous_url0",
  "count": 194,
  "total_count": 226
}
```

