
# All Letters

## Structure

`AllLetters`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `object` | `str` | Optional | Value is resource type. |
| `next_url` | `str` | Optional | Url of next page of items in list. |
| `previous_url` | `str` | Optional | Url of previous page of items in list. |
| `count` | `int` | Optional | number of resources in a set |
| `total_count` | `int` | Optional | Indicates the total number of records. Provided when the request specifies an "include" query parameter |
| `data` | List[[no_extra_service](../../doc/models/no-extra-service.md) \| [registered](../../doc/models/registered.md) \| [certified](../../doc/models/certified.md)] \| None | Optional | list of letters |

## Example (as JSON)

```json
{
  "object": "object0",
  "next_url": "next_url2",
  "previous_url": "previous_url0",
  "count": 230,
  "total_count": 190
}
```

