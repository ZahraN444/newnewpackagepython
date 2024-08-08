
# Checks Response

## Structure

`ChecksResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | Unique identifier prefixed with `chk_`.<br>**Constraints**: *Pattern*: `^chk_[a-zA-Z0-9]+$` |
| `deleted` | `bool` | Optional | Only returned if the resource has been successfully deleted. |

## Example (as JSON)

```json
{
  "id": "id6",
  "deleted": false
}
```

