
# Links Response

## Structure

`LinksResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `count` | `int` | Optional | The number of results in the current response. |
| `limit` | `int` | Optional | How many results to return. |
| `offset` | `int` | Optional | An integer that designates the offset at which to begin returning results. Defaults to 0. |
| `data` | [`List[LinkResponse]`](../../doc/models/link-response.md) | Optional | list of links |

## Example (as JSON)

```json
{
  "count": 230,
  "limit": 86,
  "offset": 182,
  "data": [
    {
      "id": "id0",
      "campaign_id": "campaign_id0",
      "domain_id": "domain_id2",
      "resource_id": "resource_id6",
      "redirect_link": "redirect_link0"
    }
  ]
}
```

