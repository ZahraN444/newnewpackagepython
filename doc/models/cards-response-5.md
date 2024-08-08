
# Cards Response 5

## Structure

`CardsResponse5`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | Unique identifier prefixed with `card_`.<br>**Constraints**: *Pattern*: `^card_[a-zA-Z0-9]+$` |
| `deleted` | `bool` | Optional | Only returned if the resource has been successfully deleted. |

## Example (as JSON)

```json
{
  "id": "id0",
  "deleted": false
}
```

