
# All Addresses

## Structure

`AllAddresses`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `object` | `str` | Optional | Value is resource type. |
| `next_url` | `str` | Optional | Url of next page of items in list. |
| `previous_url` | `str` | Optional | Url of previous page of items in list. |
| `count` | `int` | Optional | number of resources in a set |
| `total_count` | `int` | Optional | Indicates the total number of records. Provided when the request specifies an "include" query parameter |
| `data` | List[[address_us](../../doc/models/address-us.md) \| [address_intl](../../doc/models/address-intl.md)] \| None | Optional | list of addresses |

## Example (as JSON)

```json
{
  "object": "object2",
  "next_url": "next_url0",
  "previous_url": "previous_url2",
  "count": 74,
  "total_count": 90
}
```

